# BlueOS 0.8.1 Installation Guide for POCO M5 (`rock` / `stone`) 🌸

Step-by-step installation guide for **BlueOS 0.8.1** on **Xiaomi POCO M5 / Redmi 11 Prime 4G** (MediaTek Helio G99 / MT6789).

---

## ⚠️ CRITICAL NOTICE: MediaTek Helio G99 Precautions
- MediaTek devices behave differently than Qualcomm Snapdragon devices.
- **NEVER re-lock the bootloader (`fastboot oem lock` or `fastboot flashing lock`) with a custom ROM or custom recovery installed!**
- Flashing unverified low-level preloader partitions can hard-brick MTK devices and require an authorized Xiaomi EDL / Service account.
- Always flash only recovery, boot, vendor_boot, and dynamic system partitions.

---

## 🛠 Prerequisites
1. Unlocked bootloader via official **Mi Unlock** tool.
2. Custom Recovery (**OrangeFox R12.1** or **TWRP** for MT6789 `rock`).
3. Installed `adb` and `fastboot` drivers on your host PC.
4. Download the release files:
   - `BlueOS-0.8.1-rock-20261108.zip` (Flashable Recovery ROM)
   - `vendor_boot.img`
   - `boot.img`
   - `dtbo.img`

---

## 🚀 Step-by-Step Installation

### Step 1: Boot into Fastboot
Power off the device, then hold **Volume Down + Power** until the FASTBOOT screen appears. Connect the phone to your PC via USB.

### Step 2: Flash Recovery Partitions (Fastboot)
```bash
# Verify connection
fastboot devices

# Flash boot and vendor_boot
fastboot flash boot boot.img
fastboot flash vendor_boot vendor_boot.img
fastboot flash dtbo dtbo.img

# Reboot to Recovery
fastboot reboot recovery
```

### Step 3: Format Data
In TWRP / OrangeFox:
1. Tap **Wipe** -> **Format Data**.
2. Type `yes` and confirm.
3. Tap **Back** to the main recovery menu.

### Step 4: Flash BlueOS
Using ADB Sideload:
1. In recovery, select **Advanced** -> **ADB Sideload** and swipe to start.
2. On your computer, run:
   ```bash
   adb sideload BlueOS-0.8.1-rock-20261108.zip
   ```
*(Alternatively, copy the zip file to an SD card or USB-OTG and flash directly from recovery).*

### Step 5: Reboot System
Once flashing completes (returns status 0 / successful):
```bash
adb reboot
```
The first boot takes approximately 2 to 4 minutes. Enjoy BlueOS on your POCO M5! 🌸
