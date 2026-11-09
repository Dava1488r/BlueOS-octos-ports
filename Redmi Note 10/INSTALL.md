# Clean Installation Guide for BlueOS 0.8.1 on Redmi Note 10 4G (`mojito` / `sunny`) 🌸

Step-by-step installation instructions for **BlueOS 0.8.1** (Android 17 / LineageOS 24.0 base) on **Xiaomi Redmi Note 10 4G**.

---

## ⚠️ Important Notes

- Installing a custom ROM wipes internal storage. **Backup all critical data** before proceeding.
- Bootloader must be unlocked via official Xiaomi Mi Unlock tool.
- Ensure device battery is charged to at least 50%.
- This build is 64-bit only (legacy 32-bit apps will not run).

---

## 🛠 Prerequisites

1. Install ADB and Fastboot drivers on your PC.
2. Download the release files:
   - `BlueOS-0.8.1-mojito-20261109.zip` — ROM package
   - `boot.img` — Kernel image
   - `dtbo.img` — Device tree overlay
   - `vendor_boot.img` — Vendor boot image

---

## 🚀 Installation Steps

### Step 1: Boot into Fastboot Mode
1. Power off the phone.
2. Hold **Volume Down + Power** buttons until the FASTBOOT logo appears.
3. Connect the phone to your PC with a USB cable.

### Step 2: Flash Boot Partitions via Fastboot
Open a terminal in the folder containing your downloaded files:
```bash
# Verify device connection
fastboot devices

# Flash boot partitions
fastboot flash boot boot.img
fastboot flash dtbo dtbo.img
fastboot flash vendor_boot vendor_boot.img

# Reboot to Recovery
fastboot reboot recovery
```

### Step 3: Format Data
1. In your recovery (TWRP / OrangeFox / PBRP / Lineage Recovery), navigate to **Wipe** / **Factory Reset**.
2. Select **Format Data** (type `yes`) to remove encryption and wipe user data.

### Step 4: Flash BlueOS ROM
1. In Recovery, select **Apply update** -> **Apply from ADB** (or copy zip to storage/OTG and flash directly).
2. From your computer, run:
```bash
adb sideload BlueOS-0.8.1-mojito-20261109.zip
```
3. Wait until the sideload completes (`Step 2/2` or `Total xfer: 1.00x`).

### Step 5: Reboot
1. Select **Reboot system now**.
2. Initial boot will take 2-3 minutes.
3. Welcome to Kivotos, Sensei! 🌸
