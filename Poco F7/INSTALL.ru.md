# Инструкция по установке BlueOS 0.8.1 на POCO F7 (`onyx`) 🌸

Полное руководство по прошивке **BlueOS 0.8.1** (Android 17 / LineageOS 24.0) с поддержкой **OSS ядра SM8735** и **камеры Leica** для смартфона **Xiaomi POCO F7 / Redmi Turbo 4 Pro (`onyx`)**.

---

## 🛠 Требования к установке
1. Разблокированный загрузчик (**Bootloader Unlocked**).
2. Компьютер с установленными драйверами ADB и Fastboot.
3. Скачанные файлы релиза:
   - `BlueOS-0.8.1-onyx-20261108.zip`
   - `boot.img`
   - `init_boot.img`
   - `vendor_boot.img`
   - `dtbo.img`

---

## 🚀 Пошаговая прошивка

### Шаг 1: Перевод в режим Fastboot
Выключите телефон, затем зажмите клавиши **Громкость Вниз + Питание** до появления логотипа FASTBOOT на экране. Подключите устройство к ПК кабелем.

### Шаг 2: Прошивка разделов ядра и рекавери
В терминале на компьютере выполните:
```bash
# Проверка обнаружения смартфона
fastboot devices

# Прошивка всех необходимых разделов
fastboot flash boot boot.img
fastboot flash init_boot init_boot.img
fastboot flash vendor_boot vendor_boot.img
fastboot flash dtbo dtbo.img

# Перезагрузка в кастомное рекавери
fastboot reboot recovery
```

### Шаг 3: Очистка данных (Factory Reset)
В меню рекавери:
1. Выберите пункт **Factory Reset** -> **Format data / factory reset**.
2. Подтвердите форматирование. Это удалит шифрование старой прошивки.

### Шаг 4: Установка BlueOS через ADB Sideload
1. В меню рекавери выберите **Apply update** -> **Apply from ADB**.
2. На компьютере выполните команду:
   ```bash
   adb sideload BlueOS-0.8.1-onyx-20261108.zip
   ```
3. Дождитесь завершения процесса (на экране появится `Total xfer: 1.00x` или `Script succeeded: result was 1.000000`).

### Шаг 5: Загрузка в систему
В главном меню рекавери нажмите **Reboot system now**.
Первая загрузка займет около 2-3 минут. Добро пожаловать в Кивотос на вашем POCO F7! 🌸
