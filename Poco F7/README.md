# BlueOS for POCO F7 (`onyx`) 🌸

[![Status](https://img.shields.io/badge/Port_Status-Building-orange?style=flat-square)]()
[![Android](https://img.shields.io/badge/OS-Android%2017%20(LineageOS%2024.0)-blue?style=flat-square)]()
[![Platform](https://img.shields.io/badge/SoC-Qualcomm%20Snapdragon%208s%20Gen%204%20(SM8735)-red?style=flat-square)]()
[![Kernel](https://img.shields.io/badge/Kernel-OSS%20Kernel%20(SM8735)-green?style=flat-square)]()
[![Camera](https://img.shields.io/badge/Camera-Leica%20Camera%20Stack-red?style=flat-square)]()

Native port of **BlueOS 0.8.1** (Blue Archive themed Android OS based on **LineageOS 24.0 / Android 17**) for **Xiaomi POCO F7 / Redmi Turbo 4 Pro** (`onyx`).

Features:
- **Upstream Base**: LineageOS 24.0 (Android 17) maintained by `@grewal` (Adarsh Grewal) / `@stuff_and_things` (`xiaomi-onyx-dev`).
- **Open-Source Kernel**: Official OSS Kernel compiled from `android_kernel_xiaomi_sm8735`.
- **Integrated Leica Camera**: Full hardware-accelerated Leica camera pipeline, HDR, portrait bokeh, 4K/8K 60fps video capture.
- **BlueOS Kivotos Shell**: Custom Sensei SystemUI, Arona lockscreen widgets, MomoTalk messenger sound engine.

---

## 📥 Downloads

| File | Size | Description | Link |
|---|---|---|---|
| **BlueOS-0.8.1-onyx-20261108.zip** | ~1.6 GB | Flashable Virtual A/B OTA Recovery Package | [Download from GitHub Releases](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-onyx) |
| **boot.img** | 64 MB | Kernel boot partition | [Download boot.img](https://github.com/Dava1488r/BlueOS-octos-ports/releases/download/v0.8.1-onyx/boot.img) |
| **init_boot.img** | 8 MB | Ramdisk partition | [Download init_boot.img](https://github.com/Dava1488r/BlueOS-octos-ports/releases/download/v0.8.1-onyx/init_boot.img) |
| **vendor_boot.img** | 64 MB | Vendor boot partition | [Download vendor_boot.img](https://github.com/Dava1488r/BlueOS-octos-ports/releases/download/v0.8.1-onyx/vendor_boot.img) |
| **dtbo.img** | 16 MB | Device Tree Blob Overlay | [Download dtbo.img](https://github.com/Dava1488r/BlueOS-octos-ports/releases/download/v0.8.1-onyx/dtbo.img) |
| **SHA256SUMS** | 1 KB | Verification checksums | [View Checksums](https://github.com/Dava1488r/BlueOS-octos-ports/releases/download/v0.8.1-onyx/SHA256SUMS) |

---

## 📖 Installation Instructions
- 🇷🇺 [Русская инструкция по установке](INSTALL.ru.md)
- 🇬🇧 [English Installation Guide](INSTALL.md)

---

## ⚙️ Hardware Specifications
- **SoC**: Qualcomm Snapdragon 8s Gen 4 (SM8735, TSMC 4nm)
- **CPU**: 1x Cortex-X4 @ 3.0 GHz + 4x Cortex-A720 @ 2.8 GHz + 3x Cortex-A520 @ 2.0 GHz
- **GPU**: Adreno 735
- **Camera Stack**: 50 MP Sony IMX / Light Fusion with Leica Summilux lens integration
- **Display**: 6.67" 1.5K OLED, 120Hz, Dolby Vision, HDR10+
