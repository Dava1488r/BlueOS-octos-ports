# Clean Installation Guide for BlueOS 0.8.1 on Samsung Galaxy A71 4G (`a71`) 🌸

Step-by-step installation instructions for **BlueOS 0.8.1** (Android 16 / LineageOS 23.2 base) on **Samsung Galaxy A71 4G** (`SM-A715F`).

---

## ⚠️ Important Warnings

- Flashing custom firmware trips **KNOX** (0x1 permanently) and wipes internal storage.
- **Backup all critical data** (photos, contacts, 2FA tokens) before starting.
- Ensure device battery is charged to at least 60%.
- Ensure OEM Unlocking is enabled and bootloader is fully unlocked in Samsung Download Mode.

---

## 🛠 Prerequisites

1. **Samsung USB Drivers** installed on your PC (Windows) or `heimdall` / `adb` / `fastboot` on Linux/macOS.
2. **Odin v3.14.4** (Windows) or **Heimdall CLI** (Linux/macOS).
3. Downloaded files from the BlueOS Release:
   - `BlueOS-0.8.1-a71-20261109.zip` — ROM package
   - `recovery.tar` — Odin-ready recovery package (or `recovery.img`)
   - `vbmeta.img` — Verified Boot disabled metadata

---

## 🚀 Installation Steps

### Step 1: Unlock Bootloader
1. Enable Developer Options: **Settings** -> **About phone** -> tap **Build number** 7 times.
2. In Developer Options, enable **OEM unlocking** and **USB debugging**.
3. Power off the phone. Hold **Volume Up + Volume Down** simultaneously and connect the USB cable to PC until the teal Download Warning screen appears.
4. Long-press **Volume Up** to enter "Device unlock mode" and confirm unlocking (this will factory reset the phone).

### Step 2: Flash Recovery via Odin (Download Mode)
1. Power off device. Hold **Volume Up + Volume Down** and connect USB cable to enter **Download Mode**. Press **Volume Up** once to continue.
2. Open **Odin v3.14.4** on Windows:
   - Ensure the device is recognized (blue `ID:COM` box).
   - In the **Options** tab, **UNCHECK "Auto Reboot"** (Crucial: prevents stock ROM from overwriting recovery on reboot).
   - Click **AP** and select `recovery.tar`.
   - Click **USERDATA** (if flashing vbmeta) or flash `recovery.tar`.
   - Click **Start** and wait for `PASS!`.
3. Unplug cable, then press and hold **Volume Down + Power** for 7 seconds to exit Download Mode. As soon as the screen turns black, immediately hold **Volume Up + Power** until the BlueOS / LineageOS Recovery appears.

### Step 3: Factory Reset / Format Data
1. In BlueOS Recovery, navigate with volume keys and select with power button:
2. Select **Factory Reset** -> **Format data / factory reset**.
3. Confirm formatting.

### Step 4: Sideload BlueOS ROM
1. In Recovery, select **Apply update** -> **Apply from ADB**.
2. Connect USB cable to PC.
3. Open terminal/command prompt and run:
   ```bash
   adb sideload BlueOS-0.8.1-a71-20261109.zip
   ```
4. Wait for the transfer and installation to complete (typically reaches ~47% and prints `Step 2/2` or `Total xfer: 1.00x`).
5. (Optional) If prompted with `Signature verification failed`, select **Yes** to continue installation.

### Step 5: Reboot
1. Select **Reboot system now**.
2. Initial boot will take 2-3 minutes.
3. Welcome to Kivotos! 🌸
