# BlueOS 0.8.1 Installation Guide for POCO F7 (`onyx`) 🌸

Official installation guide for **BlueOS 0.8.1** (Android 17 / LineageOS 24.0 base) featuring **SM8735 OSS Kernel** and **Leica Camera** support on **Xiaomi POCO F7 / Redmi Turbo 4 Pro (`onyx`)**.

---

## 🛠 Prerequisites
1. Unlocked bootloader (**Bootloader Unlocked**).
2. Host computer with working ADB & Fastboot platform tools.
3. Downloaded release package files:
   - `BlueOS-0.8.1-onyx-20261108.zip`
   - `boot.img`
   - `init_boot.img`
   - `vendor_boot.img`
   - `dtbo.img`

---

## 🚀 Step-by-Step Installation

### Step 1: Fastboot Mode
Power off the phone completely, then press and hold **Volume Down + Power** buttons until the FASTBOOT screen appears. Connect the phone to your PC via USB.

### Step 2: Flash Kernel & Recovery Partitions
```bash
# Check device communication
fastboot devices

# Flash boot and recovery partitions
fastboot flash boot boot.img
fastboot flash init_boot init_boot.img
fastboot flash vendor_boot vendor_boot.img
fastboot flash dtbo dtbo.img

# Reboot into Recovery mode
fastboot reboot recovery
```

### Step 3: Format Data
In recovery menu:
1. Select **Factory Reset** -> **Format data / factory reset**.
2. Confirm the operation to wipe encryption metadata.

### Step 4: Sideload BlueOS
1. Select **Apply update** -> **Apply from ADB**.
2. On your computer terminal:
   ```bash
   adb sideload BlueOS-0.8.1-onyx-20261108.zip
   ```
3. Wait for progress to reach 100% and report success.

### Step 5: Boot BlueOS
Select **Reboot system now** in recovery.
First boot takes around 2-3 minutes. Enjoy BlueOS on your POCO F7! 🌸
