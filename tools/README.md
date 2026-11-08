# BlueOS Porting & Repacking Pipeline 🛠️

This directory contains the actual scripts used to create the community ports in **BlueOS octo's ports**.

## How the Ports are Created

Building a custom ROM completely from source requires an official LineageOS 24.0 device tree, vendor blobs, and kernel sources for each device. Because several devices (such as POCO M5 on Helio G99 or POCO F7 on SM8735) do not have official LineageOS 24.0 trees, these ports were created using a **binary ROM repacking & system overlay injection pipeline**:

1. **Donor / Base ROM**:
   A base LineageOS ROM for the target device is downloaded and verified.
2. **Partition Extraction**:
   - **Virtual A/B (Payload)**: `payload.bin` is extracted using `payload_dumper` into raw ext4/erofs image files (`system.img`, `system_ext.img`, `product.img`, `vendor.img`, `boot.img`, etc.).
   - **Sparse DAT (sdat)**: `system.new.dat.br` is decompressed via `brotli` and converted to raw ext4 images using `sdat2img.py`.
3. **Filesystem Resizing & BlueOS Component Injection**:
   - Filesystems are expanded via `resize2fs` to allocate space for BlueOS assets.
   - Using `debugfs` or loop mounts, the BlueOS 0.8.1 system apps and assets are injected:
     - `system_ext/priv-app/SystemUI/SystemUI.apk`
     - `system_ext/priv-app/Settings/Settings.apk`
     - `system_ext/priv-app/Launcher3QuickStep/Launcher3QuickStep.apk`
     - `system_ext/priv-app/ThemePicker/ThemePicker.apk`
     - `product/media/bootanimation.zip`
     - `product/app/DeskClock/DeskClock.apk`, `Glimpse.apk`
     - BlueOS system properties in `build.prop.blueos`:
       `ro.blueos.version=0.8.1`, `ro.blueos.build.type=COMMUNITY_PORT`
4. **Verified Boot (AVB) Patching**:
   - Custom unsigned partitions require dm-verity and verification to be disabled to avoid bootloops.
   - `avbtool make_vbmeta_image --flags 2 --set_verification_disabled_flag --set_hashtree_disabled_flag` generates patched `vbmeta.img`.
5. **Repacking**:
   - **Payload OTA**: Repacked using `payload_packer` into flashable OTA zips with `META-INF/com/google/android/update-binary`.
   - **Dynamic / Fastboot images**: Provided alongside the zip for fastboot flashing.

## Included Scripts

- [`repack_pixel_payload.py`](repack_pixel_payload.py): Automated tool for Virtual A/B devices (Google Pixel 7 series, POCO X3 Pro).
- [`repack_sdat_rom.py`](repack_sdat_rom.py): Automated tool for sparse `system.new.dat.br` devices (Redmi Note 8T, Redmi 7A).

## Prerequisites

- Linux (Ubuntu/Debian)
- `python3`, `e2fsprogs` (`resize2fs`, `e2fsck`, `debugfs`)
- `payload_dumper`, `payload_packer`
- `brotli`, `sdat2img`
