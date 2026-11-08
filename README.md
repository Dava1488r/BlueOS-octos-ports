# BlueOS octoʼs ports 🌌📱

[![GitHub Stars](https://img.shields.io/github/stars/Dava1488r/BlueOS-octos-ports?style=flat-square)](https://github.com/Dava1488r/BlueOS-octos-ports/stargazers)
[![GitHub Releases](https://img.shields.io/github/downloads/Dava1488r/BlueOS-octos-ports/total?style=flat-square)](https://github.com/Dava1488r/BlueOS-octos-ports/releases)
[![LineageOS](https://img.shields.io/badge/Base-LineageOS-0055ff?style=flat-square)](https://lineageos.org/)
[![BlueOS](https://img.shields.io/badge/Based_on-BlueOS%20by%20GDmio-1e90ff?style=flat-square)](https://github.com/GDmio/BlueOS)

> [!IMPORTANT]
> **Attribution:** Based on [BlueOS by GDmio](https://github.com/GDmio/BlueOS). See [NOTICE](NOTICE) for license information.
> Russian documentation available / Русская версия: [README.ru.md](README.ru.md)

Collection of community ports and installation packages of **BlueOS 0.8.1** (Blue Archive themed Android OS based on **LineageOS**) maintained by **octo**.

Each port incorporates BlueOS Kivotos UI styling adapted for the target device:
- **SystemUI & Lockscreen**: Kivotos theme styling, custom status bar icons, clock and halo accents.
- **Launcher3QuickStep**: BlueOS themed launcher and icon pack.
- **ThemePicker & Settings**: Custom BlueOS color palette, themed preference categories, and BlueOS branding.
- **Custom Assets Import**: BlueOS includes built-in support for importing your own game models, sounds, and wallpapers on-device (see [ASSETS.md](ASSETS.md)). No copyrighted game files are included in the ROM packages.
- **Repack Pipeline**: Full scripts showing how ROM images are unpacked, patched, and rebuilt are available in [`tools/`](tools/).

---

## 📱 Supported Devices & Download Hub

> ⚠️ **Note on Port Status**: Only **Redmi Note 8T** has been verified and booted on physical hardware. All other builds are marked as **Pre-release / Experimental** and have not been tested on real physical devices. Flash at your own risk!

| Device | Codename | Platform Base | Port Status | Ready ZIP (Releases) | Guide |
|---|---|---|:---:|:---:|:---:|
| **Redmi Note 8T / 8** | `willow` / `ginkgo` | Qualcomm SDM665 (LineageOS 24.0 / A17) | ✅ Booted & Verified | [Download ZIP (1.74 GB)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-willow) | [Guide](Redmi%20Note%208t/INSTALL.md) |
| **POCO X3 Pro** | `vayu` / `bhima` | Qualcomm SD860 (LineageOS 23.2 / A16) | ⚠️ Pre-release (Untested) | [Download ZIP (1.76 GB)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-vayu) | [Guide](Poco%20X3%20Pro/INSTALL.md) |
| **Google Pixel 7** | `panther` | Google Tensor G2 (LineageOS 24.0 / A17) | ⚠️ Pre-release (Untested) | [Download ZIP (1.43 GB)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-panther) | [Guide](Pixel%207/INSTALL.md) |
| **Google Pixel 7 Pro** | `cheetah` | Google Tensor G2 (LineageOS 24.0 / A17) | ⚠️ Pre-release (Untested) | [Download ZIP (1.45 GB)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-cheetah) | [Guide](Pixel%207pro/INSTALL.md) |
| **Google Pixel 7a** | `lynx` | Google Tensor G2 (LineageOS 24.0 / A17) | ⚠️ Pre-release (Untested) | [Download ZIP (1.45 GB)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-lynx) | [Guide](Pixel%207a/INSTALL.md) |
| **POCO M5** | `rock` / `stone` | MediaTek Helio G99 (LineageOS 24.0 / A17) | ⚠️ Pre-release (Untested) | [Download ZIP (1.1 GB)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-rock) | [Guide](Poco%20M5/INSTALL.md) |
| **POCO F7** | `onyx` | Qualcomm SM8735 (OSS Kernel, LineageOS 24.0) | ⚠️ Pre-release (Untested) | [Download ZIP (1.05 GB)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-onyx) | [Guide](Poco%20F7/INSTALL.md) |
| **Redmi 7A** | `pine` / `mi439` | Qualcomm SDM439 (LineageOS 21.0 / A14, 2GB) | ⚠️ Pre-release (Untested) | [Download ZIP (1.02 GB)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-pine) | [Guide](Redmi%207a/INSTALL.md) |

---

## 📂 Repository Structure

- [`/Redmi Note 8t/`](Redmi%20Note%208t/) — Port files, flashable package links, and step-by-step install guide for Redmi Note 8T (`willow`) & Redmi Note 8 (`ginkgo`).
- [`/Poco X3 Pro/`](Poco%20X3%20Pro/) — Dynamic partition package, fastboot recovery images, and guide for POCO X3 Pro (`vayu` / `bhima`).
- [`/Pixel 7/`](Pixel%207/) — Virtual A/B OTA recovery package, fastboot partitions, and guide for Google Pixel 7 (`panther`).
- [`/Pixel 7pro/`](Pixel%207pro/) — Virtual A/B OTA recovery package, fastboot partitions, and guide for Google Pixel 7 Pro (`cheetah`).
- [`/Pixel 7a/`](Pixel%207a/) — Virtual A/B OTA recovery package, fastboot partitions, and guide for Google Pixel 7a (`lynx`).
- [`/Poco M5/`](Poco%20M5/) — MediaTek Helio G99 port files and install guide for POCO M5 (`rock` / `stone`).
- [`/Poco F7/`](Poco%20F7/) — LineageOS 24.0 with SM8735 OSS kernel port files and guide for POCO F7 (`onyx`).
- [`/Redmi 7a/`](Redmi%207a/) — Low-RAM 2GB profile build (LineageOS 21.0 base) and guide for Redmi 7A (`pine`).
- [`/tools/`](tools/) — ROM repacking, payload extraction, and image injection scripts.
- [`ASSETS.md`](ASSETS.md) / [`ASSETS.ru.md`](ASSETS.ru.md) — Guide for importing custom Blue Archive character assets on-device.
- [`NOTICE`](NOTICE) — Upstream attribution and licensing.

---

## ⚡ Quick Flashing Instructions

All packages are compiled for installation via Custom Recovery (OrangeFox / TWRP / Lineage Recovery) or Fastboot + ADB Sideload:

1. **Unlock Bootloader**: Ensure your device's bootloader is unlocked.
2. **Flash Recovery Partitions**: Flash matching `boot.img` (and `init_boot.img` / `dtbo.img` / `vendor_boot.img` where applicable) via fastboot.
3. **Format Data**: Perform a factory reset (Format Data / wipe).
4. **Flash BlueOS ZIP**: Use `adb sideload BlueOS-0.8.1-<device>-20261108.zip` or install from recovery.
5. **Reboot system** and enjoy!

Detailed instructions with exact terminal commands are available in each device's subfolder.

---

## 🔗 Credits & Upstream
- **BlueOS Upstream**: [GDmio/BlueOS](https://github.com/GDmio/BlueOS) — Original BlueOS design, theme engine, and concept.
- **Base Android**: [LineageOS Project](https://github.com/LineageOS)
- **Character assets & media**: © NEXON Games & Yostar / Blue Archive.
