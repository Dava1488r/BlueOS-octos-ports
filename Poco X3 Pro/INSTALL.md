# Clean Installation Guide for BlueOS 0.8.1 on POCO X3 Pro (`vayu` / `bhima`) 🌸

Step-by-step installation instructions for **BlueOS 0.8.1** (Android 17 / LineageOS 24.0 base) on **Xiaomi POCO X3 Pro**.

---

## ⚠️ Important Notes
- Installing a custom ROM will wipe internal storage. **Backup all important files before proceeding!**
- Bootloader must be unlocked via official Mi Flash Unlock.
- Ensure battery level is at least 50%.

---

## 🛠 Prerequisites
1. Install ADB and Fastboot drivers on your PC.
2. Download release files:
   - `BlueOS-0.8.1-vayu-20261108.zip` — Recovery ROM package
   - `boot.img` — Kernel image
   - `dtbo.img` — Device tree blob overlay
   - `recovery.img` — BlueOS Recovery image
   - `vbmeta.img` — Verified boot metadata

---

## 🚀 Installation Steps

### Step 1: Boot into Fastboot Mode
1. Power off the phone.
2. Press and hold **Volume Down + Power** buttons until the FASTBOOT logo appears.
3. Connect the phone to your PC via a USB cable.

### Step 2: Flash Boot Partitions via Fastboot
Open a terminal in the folder containing your downloaded files:
```bash
# Verify connection
fastboot devices

# Disable AVB verification
fastboot --disable-verity --disable-verification flash vbmeta vbmeta.img

# Flash boot, dtbo, and recovery
fastboot flash boot boot.img
fastboot flash dtbo dtbo.img
fastboot flash recovery recovery.img

# Reboot into Recovery
fastboot reboot recovery
```

### Step 3: Format Data
1. In Recovery, navigate to **Factory Reset**.
2. Select **Format data / factory reset** and confirm.

### Step 4: Flash BlueOS ROM
1. In Recovery, select **Apply update** -> **Apply from ADB**.
2. On your computer, run:
```bash
adb sideload BlueOS-0.8.1-vayu-20261108.zip
```
3. Wait until completion (`Step 2/2` or `Total xfer: 1.00x`).

### Step 5: Reboot System
1. Select **Reboot system now**.
2. The initial boot may take 2-3 minutes.
3. Welcome to Kivotos, Sensei! 🌸
