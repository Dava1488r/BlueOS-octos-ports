# BlueOS octoʼs ports 🌌📱

[![GitHub Stars](https://img.shields.io/github/stars/Dava1488r/BlueOS-octos-ports?style=flat-square)](https://github.com/Dava1488r/BlueOS-octos-ports/stargazers)
[![GitHub Releases](https://img.shields.io/github/downloads/Dava1488r/BlueOS-octos-ports/total?style=flat-square)](https://github.com/Dava1488r/BlueOS-octos-ports/releases)
[![LineageOS](https://img.shields.io/badge/Base-LineageOS%2024.0%20(Android%2017)-0055ff?style=flat-square)](https://lineageos.org/)
[![BlueOS](https://img.shields.io/badge/Theme-Blue%20Archive%20(BlueOS)-1e90ff?style=flat-square)](https://github.com/GDmio/BlueOS)

> [!NOTE]
> Russian documentation available / Русская версия: [README.ru.md](README.ru.md)

Collection of native, ready-to-flash ports of **BlueOS 0.8.1** (Blue Archive themed Android OS based on **LineageOS 24.0 / Android 17**) created and maintained by **octo**.

Each port includes fully functioning native BlueOS components:
- **SystemUI & Lockscreen**: Blue Archive Sensei UI, Arona/Plana live animations, Blue status icons.
- **Launcher3QuickStep**: Custom BlueOS icon packs, Arona search widgets, MomoTalk integration.
- **BlueOS Settings**: Themed preferences, character customization hub, live sound engine.
- **Native BlueOS Audio & Bootanimation**: Sensei voice lines, MomoTalk notification chimes, Blue Archive startup animation.

---

## 📱 Supported Devices & Download Hub

| Device | Codename | Platform | Port Status | Ready ZIP (Releases) | Guide |
|---|---|---|:---:|:---:|:---:|
| **Redmi Note 8T / 8** | `willow` / `ginkgo` | Qualcomm Snapdragon 665 | ✅ Booted & Verified | [Download ZIP (1.74 GB)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-willow) | [Guide](Redmi%20Note%208t/INSTALL.md) |
| **POCO X3 Pro** | `vayu` / `bhima` | Qualcomm Snapdragon 860 | ✅ Ready to flash | [Download ZIP (1.76 GB)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-vayu) | [Guide](Poco%20X3%20Pro/INSTALL.md) |
| **Google Pixel 7** | `panther` | Google Tensor G2 | ✅ Ready to flash | [Download ZIP (1.43 GB)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-panther) | [Guide](Pixel%207/INSTALL.md) |
| **Google Pixel 7 Pro** | `cheetah` | Google Tensor G2 | ✅ Ready to flash | [Download ZIP (1.45 GB)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-cheetah) | [Guide](Pixel%207pro/INSTALL.md) |
| **Google Pixel 7a** | `lynx` | Google Tensor G2 | ✅ Ready to flash | [Download ZIP (1.45 GB)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-lynx) | [Guide](Pixel%207a/INSTALL.md) |
| **POCO M5** | `rock` / `stone` | MediaTek Helio G99 | 🔨 Building ROM | Coming soon | [Guide](Poco%20M5/INSTALL.md) |
| **POCO F7** | `onyx` | Qualcomm Snapdragon 8s Gen 4 | 🔨 Packaging Trees & OSS Kernel | Coming soon | [Guide](Poco%20F7/INSTALL.md) |
| **Redmi 7A** | `pine` / `mi439` | Qualcomm Snapdragon 439 | 🔨 Preparing (2GB RAM Profile) | Coming soon | [Guide](Redmi%207a/INSTALL.md) |

---

## 📂 Repository Structure

- [`/Redmi Note 8t/`](Redmi%20Note%208t/) — Port files, flashable package links, and step-by-step install guide for Redmi Note 8T (`willow`) & Redmi Note 8 (`ginkgo`).
- [`/Poco X3 Pro/`](Poco%20X3%20Pro/) — Dynamic partition package, fastboot recovery images, and guide for POCO X3 Pro (`vayu` / `bhima`).
- [`/Pixel 7/`](Pixel%207/) — Virtual A/B OTA recovery package, fastboot partitions, and guide for Google Pixel 7 (`panther`).
- [`/Pixel 7pro/`](Pixel%207pro/) — Virtual A/B OTA recovery package, fastboot partitions, and guide for Google Pixel 7 Pro (`cheetah`).
- [`/Pixel 7a/`](Pixel%207a/) — Virtual A/B OTA recovery package, fastboot partitions, and guide for Google Pixel 7a (`lynx`).
- [`/Poco M5/`](Poco%20M5/) — MediaTek Helio G99 native port files and install guide for POCO M5 (`rock` / `stone`).
- [`/Poco F7/`](Poco%20F7/) — LineageOS 24.0, OSS kernel, Leica camera integration, and guide for POCO F7 (`onyx`).
- [`/Redmi 7a/`](Redmi%207a/) — 2GB RAM optimized build, ZRAM profile, and guide for Redmi 7A (`pine`).

---

## ⚡ Quick Flashing Instructions

All packages are compiled for fast and clean installation via either Custom Recovery (OrangeFox / TWRP) or Fastboot + ADB Sideload:

1. **Unlock Bootloader**: Ensure your device's bootloader is unlocked.
2. **Flash Recovery Partitions**: Flash matching `boot.img` (and `init_boot.img` / `dtbo.img` / `vendor_boot.img` on Pixels) via fastboot.
3. **Format Data**: Perform a factory reset (Format Data / ext4/f2fs clean wipe).
4. **Flash BlueOS ZIP**: Use `adb sideload BlueOS-0.8.1-<device>-20261108.zip` or install from SD Card / USB OTG.
5. **Reboot system** and welcome to Kivotos! 🌸

Detailed instructions with exact terminal commands are available in each device's subfolder.

---

## 🔗 Credits & Upstream
- BlueOS upstream: [GDmio/BlueOS](https://github.com/GDmio/BlueOS)
- Base Android: [LineageOS Project](https://github.com/LineageOS)
- Character assets and media: © NEXON Games & Yostar / Blue Archive
