# BlueOS 0.8.1 Installation Guide for Redmi 7A (`pine` / `mi439`) 🌸

Step-by-step installation instructions for the memory-optimized **BlueOS 0.8.1** on **Xiaomi Redmi 7A (`pine`)** and unified **mi439** hardware (Redmi 7A, Redmi 8, Redmi 8A).

---

## ⚡ 2GB RAM Optimization Profile
This build features tailored kernel and Dalvik tweaks designed for budget devices with 2GB RAM:
- **ZRAM 2.0 GB** swap configured with fast LZ4 compression.
- **Tuned Dalvik Heap limits** (`heapgrowthlimit=128m`) to eliminate memory pressure.
- **Lightweight Compositor Settings**: Disables heavy real-time GPU blurs on Adreno 505.

---

## 🛠 Prerequisites
1. Unlocked bootloader via Mi Flash Unlock.
2. Custom recovery installed (**OrangeFox** or **TWRP** for `pine`).
3. Downloaded ROM package: `BlueOS-0.8.1-pine-20261108.zip`.

---

## 🚀 Step-by-Step Installation

1. Boot into Custom Recovery (hold **Volume Up + Power**).
2. Go to **Wipe** -> tap **Format Data** and confirm by typing `yes`.
3. In **Advanced Wipe**, wipe:
   - `Dalvik / ART Cache`
   - `Cache`
   - `System`
   - `Vendor`
   - `Data`
4. Sideload the ROM package via ADB:
   ```bash
   adb sideload BlueOS-0.8.1-pine-20261108.zip
   ```
   *(Or flash directly from a MicroSD card via Install menu).*
5. When installation completes, tap **Reboot System**.
6. Initial boot takes roughly 3 to 5 minutes. Welcome to Kivotos on Redmi 7A! 🌸
