# BlueOS for Redmi 7A (`pine` / `mi439`) 🌸

[![Status](https://img.shields.io/badge/Port_Status-Pre--release%20(Untested)-yellow?style=flat-square)]()
[![Android](https://img.shields.io/badge/OS-Android%2014%20(LineageOS%2021.0)-blue?style=flat-square)]()
[![Platform](https://img.shields.io/badge/SoC-Qualcomm%20Snapdragon%20439%20(SDM439)-red?style=flat-square)]()
[![Optimization](https://img.shields.io/badge/RAM_Optimization-2GB_Low--RAM_Profile-success?style=flat-square)]()

> ⚠️ **Pre-release Warning**: This port is experimental and has not been verified on physical hardware. Flash at your own risk.

Community port of **BlueOS 0.8.1** (Blue Archive themed Android OS based on **LineageOS 21.0 / Android 14**) specifically tuned and optimized for **Xiaomi Redmi 7A** (`pine`) and the unified **mi439** family (Redmi 7A, Redmi 8, Redmi 8A).
Based on [BlueOS by GDmio](https://github.com/GDmio/BlueOS).

---

## ⚡ Special 2GB RAM Optimization Profile
Redmi 7A models typically come with **2GB of physical RAM**. To deliver smooth UI performance without launcher redraws or OOM kills:
- **ZRAM 2.0 GB Swap**: High-compression LZ4 zram paging enabled by default.
- **Tuned Dalvik Heap**: `heapgrowthlimit=128m`, `heapsize=256m` prevents heap fragmentation.
- **Optimized Blur & Translucency**: Heavy compositor blur layers disabled to preserve fillrate on Adreno 505.

---

## 📥 Downloads

| File | Size | Description | Link |
|---|---|---|---|
| **BlueOS-0.8.1-pine-20261108.zip** | 1.02 GB | Flashable Recovery ROM Package | [Download from GitHub Releases](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-pine) |
| **boot.img** | 64 MB | Kernel boot image | [Download boot.img](https://github.com/Dava1488r/BlueOS-octos-ports/releases/download/v0.8.1-pine/boot.img) |
| **recovery.img** | 64 MB | BlueOS Recovery | [Download recovery.img](https://github.com/Dava1488r/BlueOS-octos-ports/releases/download/v0.8.1-pine/recovery.img) |
| **dtbo.img** | 8 MB | Device Tree Blob Overlay | [Download dtbo.img](https://github.com/Dava1488r/BlueOS-octos-ports/releases/download/v0.8.1-pine/dtbo.img) |
| **vbmeta.img** | 8 KB | Verification metadata partition | [Download vbmeta.img](https://github.com/Dava1488r/BlueOS-octos-ports/releases/download/v0.8.1-pine/vbmeta.img) |
| **SHA256SUMS** | 1 KB | Verification checksums | [View Checksums](https://github.com/Dava1488r/BlueOS-octos-ports/releases/download/v0.8.1-pine/SHA256SUMS) |

---

## 📖 Installation Instructions
- 🇷🇺 [Русская инструкция по установке](INSTALL.ru.md)
- 🇬🇧 [English Installation Guide](INSTALL.md)
