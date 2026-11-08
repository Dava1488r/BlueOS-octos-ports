# BlueOS octoʼs ports 🌌📱 (Сборник портов BlueOS от octo)

[![GitHub Stars](https://img.shields.io/github/stars/Dava1488r/BlueOS-octos-ports?style=flat-square)](https://github.com/Dava1488r/BlueOS-octos-ports/stargazers)
[![GitHub Releases](https://img.shields.io/github/downloads/Dava1488r/BlueOS-octos-ports/total?style=flat-square)](https://github.com/Dava1488r/BlueOS-octos-ports/releases)
[![LineageOS](https://img.shields.io/badge/База-LineageOS%2024.0%20(Android%2017)-0055ff?style=flat-square)](https://lineageos.org/)
[![BlueOS](https://img.shields.io/badge/Тема-Blue%20Archive%20(BlueOS)-1e90ff?style=flat-square)](https://github.com/GDmio/BlueOS)

> [!NOTE]
> English version / Английская документация: [README.md](README.md)

Официальный сборник нативных готовых к установке портов **BlueOS 0.8.1** (тематическая прошивка по мотивам игры **Blue Archive** на базе **LineageOS 24.0 / Android 17**), созданных и поддерживаемых разработчиком **octo**.

Каждый порт включает в себя полный набор нативных компонентов BlueOS:
- **SystemUI и экран блокировки**: интерфейс Sensei, живые анимированные модели Arona и Plana на Spine 4.2, кастомные иконки статус-бара.
- **Launcher3QuickStep**: фирменные темы значков приложений, интерактивные виджеты поиска Ароны, интеграция MomoTalk.
- **BlueOS Settings**: стилизованное меню настроек, BlueOS Hub, селектор персонажей и звуковой движок.
- **Звуки и бутанимация**: озвучка системных событий фразами Ароны и Планы, рингтоны и звуки уведомлений MomoTalk, фирменная загрузочная анимация Blue Archive.

---

## 📱 Поддерживаемые устройства и центр загрузки

| Устройство | Кодовое имя | Процессор | Статус порта | Готовый ZIP (Releases) | Инструкция |
|---|---|---|:---:|:---:|:---:|
| **Redmi Note 8T / 8** | `willow` / `ginkgo` | Qualcomm Snapdragon 665 | ✅ Проверено на железе | [Скачать ZIP (1.74 ГБ)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-willow) | [Инструкция](Redmi%20Note%208t/INSTALL.ru.md) |
| **POCO X3 Pro** | `vayu` / `bhima` | Qualcomm Snapdragon 860 | ✅ Готов к прошивке | [Скачать ZIP (1.76 ГБ)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-vayu) | [Инструкция](Poco%20X3%20Pro/INSTALL.ru.md) |
| **Google Pixel 7** | `panther` | Google Tensor G2 | ✅ Готов к прошивке | [Скачать ZIP (1.43 ГБ)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-panther) | [Инструкция](Pixel%207/INSTALL.ru.md) |
| **Google Pixel 7 Pro** | `cheetah` | Google Tensor G2 | ✅ Готов к прошивке | [Скачать ZIP (1.45 ГБ)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-cheetah) | [Инструкция](Pixel%207pro/INSTALL.ru.md) |
| **Google Pixel 7a** | `lynx` | Google Tensor G2 | ✅ Готов к прошивке | [Скачать ZIP (1.45 ГБ)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-lynx) | [Инструкция](Pixel%207a/INSTALL.ru.md) |
| **POCO M5** | `rock` / `stone` | MediaTek Helio G99 | 🔨 В процессе | Скоро | [Инструкция](Poco%20M5/INSTALL.ru.md) |
| **POCO F7** | `onyx` | Qualcomm Snapdragon 8s Gen 4 | 📋 В очереди (OSS ядро) | Дерево найдено | Инструкция |

---

## 📂 Структура проекта

- [`/Redmi Note 8t/`](Redmi%20Note%208t/) — Порт, ссылки на пакеты прошивки и пошаговая инструкция установки для Redmi Note 8T (`willow`) и Redmi Note 8 (`ginkgo`).
- [`/Poco X3 Pro/`](Poco%20X3%20Pro/) — Пакет с динамическими разделами, fastboot-образы и инструкция для POCO X3 Pro (`vayu` / `bhima`).
- [`/Pixel 7/`](Pixel%207/) — Пакет прошивки Virtual A/B OTA, fastboot-образы и инструкция для Google Pixel 7 (`panther`).
- [`/Pixel 7pro/`](Pixel%207pro/) — Пакет прошивки Virtual A/B OTA, fastboot-образы и инструкция для Google Pixel 7 Pro (`cheetah`).
- [`/Pixel 7a/`](Pixel%207a/) — Пакет прошивки Virtual A/B OTA, fastboot-образы и инструкция для Google Pixel 7a (`lynx`).

---

## ⚡ Быстрая инструкция по прошивке

Все пакеты собраны для быстрой и чистой установки через кастомное рекавери (OrangeFox / TWRP) или режим Fastboot + ADB Sideload:

1. **Разблокировка загрузчика**: убедитесь, что Bootloader разблокирован.
2. **Прошивка разделов ядра**: прошейте соответствующие `boot.img` (а также `init_boot.img` / `dtbo.img` / `vendor_boot.img` на Pixel) через `fastboot`.
3. **Очистка данных**: выполните Format Data (сброс к заводским настройкам).
4. **Прошивка архива BlueOS**: выполните `adb sideload BlueOS-0.8.1-<device>-20261108.zip` или выберите установку из памяти/OTG в рекавери.
5. **Перезагрузка в систему**: добро пожаловать в Кивотос! 🌸

Полные инструкции с точными командами терминала смотрите в подпапке каждого устройства.

---

## 🔗 Благодарности и источники
- Оригинальный проект BlueOS: [GDmio/BlueOS](https://github.com/GDmio/BlueOS)
- Базовая ОС: [LineageOS Project](https://github.com/LineageOS)
- Медиа и персонажи: © NEXON Games & Yostar / Blue Archive
