# BlueOS octoʼs ports 🌌📱 (Сборник портов BlueOS от octo)

[![GitHub Stars](https://img.shields.io/github/stars/Dava1488r/BlueOS-octos-ports?style=flat-square)](https://github.com/Dava1488r/BlueOS-octos-ports/stargazers)
[![GitHub Releases](https://img.shields.io/github/downloads/Dava1488r/BlueOS-octos-ports/total?style=flat-square)](https://github.com/Dava1488r/BlueOS-octos-ports/releases)
[![LineageOS](https://img.shields.io/badge/База-LineageOS-0055ff?style=flat-square)](https://lineageos.org/)
[![BlueOS](https://img.shields.io/badge/Основано_на-BlueOS%20by%20GDmio-1e90ff?style=flat-square)](https://github.com/GDmio/BlueOS)

> [!IMPORTANT]
> **Уведомление об авторстве:** Основано на оригинальном проекте [BlueOS от GDmio](https://github.com/GDmio/BlueOS). Лицензия и атрибуция: файл [NOTICE](NOTICE).
> English version / Английская документация: [README.md](README.md)

Сборник неофициальных портов и установочных пакетов **BlueOS 0.8.1** (тематическая кастомная прошивка по мотивам Blue Archive на базе **LineageOS**), адаптированных разработчиком **octo**.

Каждый порт адаптирует оформление и компоненты пользовательского интерфейса BlueOS Kivotos:
- **SystemUI и экран блокировки**: стилизованные иконки статус-бара Kivotos, кастомные акценты часов и нимб на экране блокировки.
- **Launcher3QuickStep**: тема лаунчера и пакет значков BlueOS.
- **Настройки и ThemePicker**: фирменная сине-голубая палитра, брендинг BlueOS в настройках.
- **Импорт персонажей и звуков**: BlueOS поддерживает добавление собственных моделей и аудио прямо на устройстве (подробнее в [ASSETS.ru.md](ASSETS.ru.md) / [ASSETS.md](ASSETS.md)). В сборки прошивки защищенные авторским правом файлы игры не включаются.
- **Скрипты сборки и перепаковки**: исходный пайплайн распаковки образов и инъекции оверлеев выложен в открытом виде в папке [`tools/`](tools/).

---

## 📱 Поддерживаемые устройства и статус портов

> ⚠️ **Важно о статусе портов**: Только **Redmi Note 8T** был лично протестирован и успешно запущен на реальном физическом устройстве. Все остальные сборки помечены как **Pre-release (экспериментальные)** и не тестировались на «живом» железе. Установка на ваш страх и риск!

| Устройство | Кодовое имя | База платформы | Статус порта | Готовый ZIP (Releases) | Инструкция |
|---|---|---|:---:|:---:|:---:|
| **Redmi Note 8T / 8** | `willow` / `ginkgo` | Qualcomm SDM665 (LineageOS 24.0 / A17) | ✅ Проверено на железе | [Скачать ZIP (1.74 ГБ)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-willow) | [Инструкция](Redmi%20Note%208t/INSTALL.ru.md) |
| **POCO X3 Pro** | `vayu` / `bhima` | Qualcomm SD860 (LineageOS 23.2 / A16) | ⚠️ Pre-release (Не тестировался) | [Скачать ZIP (1.76 ГБ)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-vayu) | [Инструкция](Poco%20X3%20Pro/INSTALL.ru.md) |
| **Google Pixel 7** | `panther` | Google Tensor G2 (LineageOS 24.0 / A17) | ⚠️ Pre-release (Не тестировался) | [Скачать ZIP (1.43 ГБ)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-panther) | [Инструкция](Pixel%207/INSTALL.ru.md) |
| **Google Pixel 7 Pro** | `cheetah` | Google Tensor G2 (LineageOS 24.0 / A17) | ⚠️ Pre-release (Не тестировался) | [Скачать ZIP (1.45 ГБ)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-cheetah) | [Инструкция](Pixel%207pro/INSTALL.ru.md) |
| **Google Pixel 7a** | `lynx` | Google Tensor G2 (LineageOS 24.0 / A17) | ⚠️ Pre-release (Не тестировался) | [Скачать ZIP (1.45 ГБ)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-lynx) | [Инструкция](Pixel%207a/INSTALL.ru.md) |
| **POCO M5** | `rock` / `stone` | MediaTek Helio G99 (LineageOS 24.0 / A17) | ⚠️ Pre-release (Не тестировался) | [Скачать ZIP (1.1 ГБ)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-rock) | [Инструкция](Poco%20M5/INSTALL.ru.md) |
| **POCO F7** | `onyx` | Qualcomm SM8735 (OSS ядро, LineageOS 24.0) | ⚠️ Pre-release (Не тестировался) | [Скачать ZIP (1.05 ГБ)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-onyx) | [Инструкция](Poco%20F7/INSTALL.ru.md) |
| **Redmi 7A** | `pine` / `mi439` | Qualcomm SDM439 (LineageOS 21.0 / A14, 2GB) | ⚠️ Pre-release (Не тестировался) | [Скачать ZIP (1.02 ГБ)](https://github.com/Dava1488r/BlueOS-octos-ports/releases/tag/v0.8.1-pine) | [Инструкция](Redmi%207a/INSTALL.ru.md) |

---

## 📂 Структура репозитория

- [`/Redmi Note 8t/`](Redmi%20Note%208t/) — Порт и пошаговая инструкция для Redmi Note 8T (`willow`) и Redmi Note 8 (`ginkgo`).
- [`/Poco X3 Pro/`](Poco%20X3%20Pro/) — Пакет с динамическими разделами и инструкция для POCO X3 Pro (`vayu` / `bhima`).
- [`/Pixel 7/`](Pixel%207/) — Пакет Virtual A/B OTA, fastboot-образы и инструкция для Google Pixel 7 (`panther`).
- [`/Pixel 7pro/`](Pixel%207pro/) — Пакет Virtual A/B OTA, fastboot-образы и инструкция для Google Pixel 7 Pro (`cheetah`).
- [`/Pixel 7a/`](Pixel%207a/) — Пакет Virtual A/B OTA, fastboot-образы и инструкция для Google Pixel 7a (`lynx`).
- [`/Poco M5/`](Poco%20M5/) — Порт на платформу MediaTek Helio G99 для POCO M5 (`rock` / `stone`).
- [`/Poco F7/`](Poco%20F7/) — LineageOS 24.0 с OSS ядром SM8735 для POCO F7 (`onyx`).
- [`/Redmi 7a/`](Redmi%207a/) — Low-RAM сборка (база LineageOS 21.0) для Redmi 7A (`pine`).
- [`/tools/`](tools/) — Скрипты распаковки payload.bin, работы с ext4/sdat и перепаковки ROM.
- [`ASSETS.ru.md`](ASSETS.ru.md) / [`ASSETS.md`](ASSETS.md) — Руководство по загрузке ресурсов Blue Archive на телефоне.
- [`NOTICE`](NOTICE) — Лицензия и атрибуция оригинального проекта.

---

## ⚡ Быстрая инструкция по прошивке

1. **Разблокировка загрузчика**: убедитесь, что Bootloader разблокирован.
2. **Прошивка разделов ядра**: прошейте соответствующие `boot.img` (а также `init_boot.img` / `dtbo.img` / `vendor_boot.img` где требуется) через `fastboot`.
3. **Очистка данных**: выполните Format Data (сброс к заводским настройкам).
4. **Прошивка архива BlueOS**: выполните `adb sideload BlueOS-0.8.1-<device>-20261108.zip` или выберите установку из рекавери.
5. **Перезагрузка в систему**.

Подробные пошаговые инструкции с командами находятся в папке каждого устройства.

---

## 🔗 Благодарности и первоисточники
- **Оригинальный проект BlueOS**: [GDmio/BlueOS](https://github.com/GDmio/BlueOS) — идея, тема и движок BlueOS.
- **Базовая ОС Android**: [LineageOS Project](https://github.com/LineageOS)
- **Игровые ассеты и медиа**: © NEXON Games & Yostar / Blue Archive.
