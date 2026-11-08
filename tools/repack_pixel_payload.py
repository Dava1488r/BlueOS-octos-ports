#!/usr/bin/env python3
import sys, os, subprocess, shutil

def run_cmd(cmd, cwd=None, input_data=None):
    print(f"Running: {cmd}")
    p = subprocess.run(cmd, shell=True, cwd=cwd, input=input_data, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.returncode != 0:
        print(f"Command failed (code {p.returncode}):\n{p.stderr.decode(errors='ignore')}")
        raise RuntimeError(f"Failed: {cmd}")
    return p.stdout.decode(errors='ignore')

def process_device(device, model_name, work_dir, zip_path):
    print(f"\n==========================================")
    print(f" Processing {device} ({model_name})")
    print(f"==========================================")
    
    extracted = os.path.join(work_dir, "extracted")
    out_images = os.path.join(work_dir, "out_images")
    payload_dir = os.path.join(work_dir, "payload")
    release_dir = os.path.join(work_dir, "release")
    src = "/home/octo0000/BlueOS_pixel7_builds/blueos_extracted"
    repo = "/home/octo0000/.gemini/antigravity/scratch/BlueOS_port_willow"

    os.makedirs(extracted, exist_ok=True)
    os.makedirs(out_images, exist_ok=True)
    os.makedirs(payload_dir, exist_ok=True)
    os.makedirs(release_dir, exist_ok=True)

    # 1. Unzip
    print("Unpacking OTA zip...")
    run_cmd(f"unzip -q -o {zip_path} -d {extracted}")

    # 2. Extract partitions
    print("Dumping partitions via payload_dumper...")
    payload_bin = os.path.join(extracted, "payload.bin")
    partitions = "boot,dtbo,init_boot,product,pvmfw,system_dlkm,system_ext,system,tzsw,vbmeta,vendor_boot,vendor_dlkm,vendor,vendor_kernel_boot"
    run_cmd(f"/home/octo0000/.cargo/bin/payload_dumper -i {partitions} -o {out_images} {payload_bin}")

    # 3. Modify system_ext.img
    print("Modifying system_ext.img...")
    sys_ext = os.path.join(out_images, "system_ext.img")
    run_cmd(f"e2fsck -f -y {sys_ext} || true")
    run_cmd(f"resize2fs {sys_ext} 700M")
    run_cmd(f"e2fsck -f -y {sys_ext}")
    
    apps = [
        ("priv-app/SystemUI/SystemUI.apk", f"{src}/SystemUI.apk"),
        ("priv-app/Settings/Settings.apk", f"{src}/Settings.apk"),
        ("priv-app/Launcher3QuickStep/Launcher3QuickStep.apk", f"{src}/Launcher3QuickStep.apk"),
        ("priv-app/ThemePicker/ThemePicker.apk", f"{src}/ThemePicker.apk"),
    ]
    for dst, sfile in apps:
        cmds = f"rm {dst}\nwrite {sfile} {dst}\nsif {dst} mode 0100644\nsif {dst} uid 0\nsif {dst} gid 0\n"
        subprocess.run(["debugfs", "-w", sys_ext], input=cmds.encode(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["debugfs", "-w", sys_ext], input=b"rm priv-app/Updater/Updater.apk\nrmdir priv-app/Updater\n", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    run_cmd(f"e2fsck -f -y {sys_ext}")

    # 4. Modify product.img
    print("Modifying product.img...")
    prod = os.path.join(out_images, "product.img")
    run_cmd(f"e2fsck -f -y {prod} || true")
    run_cmd(f"resize2fs {prod} 2400M")
    run_cmd(f"e2fsck -f -y {prod}")
    
    pfiles = [
        ("media/bootanimation.zip", f"{src}/bootanimation.zip"),
        ("app/DeskClock/DeskClock.apk", f"{src}/DeskClock.apk"),
        ("app/Glimpse/Glimpse.apk", f"{src}/Glimpse.apk"),
    ]
    for dst, sfile in pfiles:
        cmds = f"rm {dst}\nwrite {sfile} {dst}\nsif {dst} mode 0100644\nsif {dst} uid 0\nsif {dst} gid 0\n"
        subprocess.run(["debugfs", "-w", prod], input=cmds.encode(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    cmds_assets = f"mkdir etc/blueos\nwrite {repo}/config/assets-files.txt etc/blueos/assets-files.txt\nsif etc/blueos/assets-files.txt mode 0100644\n"
    subprocess.run(["debugfs", "-w", prod], input=cmds_assets.encode(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    run_cmd(f"e2fsck -f -y {prod}")

    # 5. Modify system.img
    print("Modifying system.img...")
    sys_img = os.path.join(out_images, "system.img")
    run_cmd(f"e2fsck -f -y {sys_img} || true")
    run_cmd(f"resize2fs {sys_img} 1500M")
    run_cmd(f"e2fsck -f -y {sys_img}")

    prop_out = subprocess.check_output(["debugfs", "-R", "cat system/build.prop", sys_img]).decode(errors="ignore")
    lines = []
    for line in prop_out.splitlines():
        if line.startswith("ro.build.display.id="):
            lines.append(f"ro.build.display.id=BlueOS-0.8.1-{device}")
        elif line.startswith("ro.product.system.name="):
            lines.append(f"ro.product.system.name=blueos_{device}")
        elif line.startswith("ro.product.system.device="):
            lines.append(f"ro.product.system.device={device}")
        elif line.startswith("ro.product.system.model="):
            lines.append(f"ro.product.system.model={model_name}")
        else:
            lines.append(line)
    lines.append("ro.blueos.version=0.8.1")
    lines.append(f"ro.blueos.device={device}")
    tmp_prop = f"/tmp/{device}_build.prop"
    with open(tmp_prop, "w") as f:
        f.write("\n".join(lines) + "\n")

    sfiles = [
        ("system/framework/framework.jar", f"{src}/framework.jar"),
        ("system/framework/services.jar", f"{src}/services.jar"),
        ("system/framework/framework-res.apk", f"{src}/framework-res.apk"),
        ("system/build.prop", tmp_prop),
    ]
    for dst, sfile in sfiles:
        cmds = f"rm {dst}\nwrite {sfile} {dst}\nsif {dst} mode 0100644\nsif {dst} uid 0\nsif {dst} gid 0\n"
        subprocess.run(["debugfs", "-w", sys_img], input=cmds.encode(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    run_cmd(f"e2fsck -f -y {sys_img}")

    # 6. Repack payload
    print("Generating payload.bin with payload_packer...")
    out_payload_bin = os.path.join(payload_dir, "payload.bin")
    run_cmd(f"/home/octo0000/.cargo/bin/payload_packer -t {out_images} -o {out_payload_bin} --threads 12")

    # 7. Package final OTA zip
    print("Packaging final OTA zip...")
    final_zip = os.path.join(release_dir, f"BlueOS-0.8.1-{device}-20261108.zip")
    run_cmd(f"python3 /home/octo0000/BlueOS_pixel7_builds/package_ota.py {device} CP2A.260605.016 {payload_dir} {extracted} {final_zip}")

    # 8. Copy fastboot images
    print("Copying fastboot images...")
    for img in ["boot.img", "dtbo.img", "init_boot.img", "vendor_boot.img"]:
        src_img = os.path.join(out_images, img)
        if os.path.exists(src_img):
            shutil.copy2(src_img, release_dir)

    # 9. Compute checksums
    print("Computing SHA256SUMS...")
    run_cmd(f"cd {release_dir} && sha256sum * > SHA256SUMS")

    print(f"\nSUCCESS for {device}!")
    print(f"Release files in: {release_dir}")

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: build_pixel.py <device> <model_name> <work_dir> <zip_path>")
        sys.exit(1)
    process_device(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
