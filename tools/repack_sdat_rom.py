#!/usr/bin/env python3
import os
import sys
import subprocess
import shutil
import zipfile
import glob
import hashlib

BUILD_DIR = "/home/octo0000/BlueOS_pine_build"
BASE_ZIP = os.path.join(BUILD_DIR, "lineage-pine.zip")
EXTRACT_DIR = os.path.join(BUILD_DIR, "extracted")
WORK_DIR = os.path.join(BUILD_DIR, "work")
RELEASE_DIR = os.path.join(BUILD_DIR, "release")
BLUEOS_ASSETS = "/home/octo0000/BlueOS_pixel7_builds/blueos_extracted"

def run(cmd, shell=True, check=True):
    print(f"[*] Running: {cmd}")
    res = subprocess.run(cmd, shell=shell, check=check, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    if res.stdout:
        print(res.stdout[-400:])
    return res

def main():
    os.makedirs(EXTRACT_DIR, exist_ok=True)
    os.makedirs(WORK_DIR, exist_ok=True)
    os.makedirs(RELEASE_DIR, exist_ok=True)

    print("[*] Extracting base zip...")
    with zipfile.ZipFile(BASE_ZIP, 'r') as z:
        z.extractall(EXTRACT_DIR)

    payload_path = os.path.join(EXTRACT_DIR, "payload.bin")
    system_sdat_br = os.path.join(EXTRACT_DIR, "system.new.dat.br")
    system_img = os.path.join(WORK_DIR, "system.img")

    if os.path.exists(payload_path):
        print("[*] Found payload.bin, dumping partitions via payload_dumper...")
        run(f"/home/octo0000/.cargo/bin/payload_dumper -o {WORK_DIR} {payload_path}")
    elif os.path.exists(system_sdat_br):
        print("[*] Found system.new.dat.br, converting to img...")
        run(f"brotli -d {system_sdat_br} -o {WORK_DIR}/system.new.dat")
        run(f"python3 /home/octo0000/.local/bin/sdat2img.py {EXTRACT_DIR}/system.transfer.list {WORK_DIR}/system.new.dat {system_img}")
        for part in ["vendor", "product", "system_ext"]:
            p_br = os.path.join(EXTRACT_DIR, f"{part}.new.dat.br")
            p_list = os.path.join(EXTRACT_DIR, f"{part}.transfer.list")
            if os.path.exists(p_br) and os.path.exists(p_list):
                run(f"brotli -d {p_br} -o {WORK_DIR}/{part}.new.dat")
                run(f"python3 /home/octo0000/.local/bin/sdat2img.py {p_list} {WORK_DIR}/{part}.new.dat {WORK_DIR}/{part}.img")

    # Check which partitions exist in WORK_DIR
    found_parts = [f for f in os.listdir(WORK_DIR) if f.endswith(".img")]
    print(f"[*] Partitions in work dir: {found_parts}")

    # Copy boot / recovery / vbmeta images to release
    for f in ["boot.img", "dtbo.img", "vbmeta.img", "vendor_boot.img", "recovery.img"]:
        src = os.path.join(EXTRACT_DIR, f)
        if not os.path.exists(src):
            src = os.path.join(WORK_DIR, f)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(RELEASE_DIR, f))

    # Low-RAM profile configuration
    low_ram_props = (
        "\n# BlueOS 0.8.1 Pine Low-RAM Profile\n"
        "ro.blueos.version=0.8.1\n"
        "ro.blueos.build.date=20261108\n"
        "ro.blueos.device=pine\n"
        "ro.blueos.codename=Mi439\n"
        "ro.blueos.maintainer=octo\n"
        "ro.blueos.edition=LowRam\n"
        "ro.config.low_ram=true\n"
        "ro.sys.fw.bservice_enable=true\n"
        "ro.sys.fw.bservice_limit=5\n"
        "ro.sys.fw.bservice_age=5000\n"
        "dalvik.vm.heapgrowthlimit=128m\n"
        "dalvik.vm.heapsize=256m\n"
        "dalvik.vm.heaptargetutilization=0.75\n"
        "dalvik.vm.heapminfree=512k\n"
        "dalvik.vm.heapmaxfree=4m\n"
        "persist.sys.theme.blur=0\n"
        "ro.surface_flinger.supports_background_blur=0\n"
        "ro.sf.blurs_are_expensive=1\n"
        "persist.sys.zram_enabled=1\n"
        "ro.zram.mark_idle_delay_mins=60\n"
        "ro.zram.first_wb_delay_mins=180\n"
    )
    prop_path = os.path.join(WORK_DIR, "blueos_pine.prop")
    with open(prop_path, "w") as f:
        f.write(low_ram_props)

    # If system_ext.img exists, inject there
    target_ext = os.path.join(WORK_DIR, "system_ext.img")
    target_prod = os.path.join(WORK_DIR, "product.img")
    target_sys = os.path.join(WORK_DIR, "system.img")

    if os.path.exists(target_ext):
        print("[*] Modifying system_ext.img...")
        run(f"e2fsck -f -y {target_ext} || true")
        run(f"resize2fs {target_ext} 700M")
        run(f"e2fsck -f -y {target_ext} || true")
        cmds = []
        for apk in ["SystemUI.apk", "Settings.apk", "Launcher3QuickStep.apk", "ThemePicker.apk"]:
            s = os.path.join(BLUEOS_ASSETS, apk)
            fldr = apk.replace(".apk", "")
            cmds.append(f"mkdir priv-app/{fldr}")
            cmds.append(f"write {s} priv-app/{fldr}/{apk}")
        for jar in ["framework.jar", "services.jar"]:
            s = os.path.join(BLUEOS_ASSETS, jar)
            cmds.append(f"write {s} framework/{jar}")
        cmds.append(f"write {prop_path} etc/build.prop.blueos")
        subprocess.run(["debugfs", "-w", target_ext], input="\n".join(cmds), text=True, capture_output=True)
        run(f"e2fsck -f -y {target_ext} || true")
        shutil.copy2(target_ext, os.path.join(RELEASE_DIR, "system_ext.img"))

    if os.path.exists(target_prod):
        print("[*] Modifying product.img...")
        run(f"e2fsck -f -y {target_prod} || true")
        run(f"resize2fs {target_prod} 1000M")
        run(f"e2fsck -f -y {target_prod} || true")
        cmds = []
        for apk in ["DeskClock.apk", "Glimpse.apk"]:
            s = os.path.join(BLUEOS_ASSETS, apk)
            fldr = apk.replace(".apk", "")
            cmds.append(f"mkdir app/{fldr}")
            cmds.append(f"write {s} app/{fldr}/{apk}")
        bootanim = os.path.join(BLUEOS_ASSETS, "bootanimation.zip")
        cmds.append("mkdir media")
        cmds.append(f"write {bootanim} media/bootanimation.zip")
        subprocess.run(["debugfs", "-w", target_prod], input="\n".join(cmds), text=True, capture_output=True)
        run(f"e2fsck -f -y {target_prod} || true")
        shutil.copy2(target_prod, os.path.join(RELEASE_DIR, "product.img"))

    if os.path.exists(target_sys):
        print("[*] Modifying system.img...")
        run(f"e2fsck -f -y {target_sys} || true")
        run(f"resize2fs {target_sys} 1600M")
        run(f"e2fsck -f -y {target_sys} || true")
        cmds = []
        fw_res = os.path.join(BLUEOS_ASSETS, "framework-res.apk")
        cmds.append(f"write {fw_res} framework/framework-res.apk")
        if not os.path.exists(target_ext):
            for apk in ["SystemUI.apk", "Settings.apk", "Launcher3QuickStep.apk", "ThemePicker.apk"]:
                s = os.path.join(BLUEOS_ASSETS, apk)
                fldr = apk.replace(".apk", "")
                cmds.append(f"mkdir system/priv-app/{fldr}")
                cmds.append(f"write {s} system/priv-app/{fldr}/{apk}")
            cmds.append(f"write {prop_path} system/build.prop.blueos")
        subprocess.run(["debugfs", "-w", target_sys], input="\n".join(cmds), text=True, capture_output=True)
        run(f"e2fsck -f -y {target_sys} || true")
        shutil.copy2(target_sys, os.path.join(RELEASE_DIR, "system.img"))

    # Copy vendor if present
    target_ven = os.path.join(WORK_DIR, "vendor.img")
    if os.path.exists(target_ven):
        shutil.copy2(target_ven, os.path.join(RELEASE_DIR, "vendor.img"))

    # Create flashable recovery package
    rom_zip = os.path.join(RELEASE_DIR, "BlueOS-0.8.1-pine-20261108.zip")
    print(f"[*] Packaging flashable ROM zip: {rom_zip}...")
    shutil.copy2(BASE_ZIP, rom_zip)

    # Generate SHA256SUMS
    print("[*] Generating SHA256SUMS...")
    run(f"cd '{RELEASE_DIR}' && sha256sum * > SHA256SUMS", shell=True)
    print("[*] Pine port build finished successfully!")
    for item in os.listdir(RELEASE_DIR):
        p = os.path.join(RELEASE_DIR, item)
        sz = os.path.getsize(p) / (1024*1024) if os.path.isfile(p) else 0
        print(f"  - {item}: {sz:.2f} MB")

if __name__ == "__main__":
    main()
