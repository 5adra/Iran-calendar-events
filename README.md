# Persian (Jalali) Calendar Events & Holidays Dataset
### دیتابیس مناسبت‌ها و تعطیلات تقویم خورشیدی، میلادی و قمری

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![JSON Validated](https://img.shields.io/badge/JSON-Validated-success.svg)](#-data-validation)

*(Scroll down for English version)*

یک مجموعه داده استاندارد، منسجم و سبک در قالب JSON شامل رویدادهای ملی و باستانی خورشیدی، مناسبت‌های بین‌المللی میلادی و مناسبت‌های مذهبی قمری جهت استفاده در تقویم‌ها، بات‌های تلگرام، نرم‌افزارهای مدیریت زمان و سرویس‌های مختلف.

---

## 📁 ساختار پوشه‌بندی مخزن (Project Structure)

```text
persian-calendar-events/
├── data/
│   ├── national-events.json        # مناسبت‌های ثابت خورشیدی، باستانی و تعطیلات ملی
│   ├── international-events.json   # مناسبت‌های بین‌المللی همراه با تاریخ دقیق میلادی
│   └── religious-events.json       # مناسبت‌های مذهبی تقویم قمری
├── examples/
│   ├── python/
│   │   └── merge_events.py         # اسکریپت نمونه پایتون برای ادغام و فیلتر داده‌ها
│   └── javascript/
│       └── index.js                # اسکریپت نمونه Node.js برای خواندن رویدادها
├── scripts/
│   └── validate_json.py            # اسکریپت اعتبارسنجی سینتکس و بررسی یکتایی idها
├── LICENSE
└── README.md
```

---

## 📊 ساختار داده‌ها (Data Schemas)

تمام فایل‌های داده با کلیدهای دورقمی مربوط به شماره ماه (`"01"` تا `"12"`) سازمان‌دهی شده‌اند. فیلدهای اصلی به این شکل هستند:

* `id`: شناسه انگلیسی یکتا برای استفاده در کدهای فرانت‌اند و دیتابیس.
* `title`: عنوان رسمی مناسبت.
* `type`: نوع و دسته‌بندی رویداد (به جدول زیر مراجعه کنید).
* `day` / `hijri_day`: شماره روز در ماه مربوطه.
* `is_holiday`: وضعیت تعطیلی رسمی در تقویم کشور (`true` / `false`).
* `gregorian_date`: تاریخ دقیق و ثابت میلادی (فقط در فایل بین‌المللی).

> **نکته درباره سال‌های کبیسه و قمری:** نگاشت روزهای فایل بین‌المللی بر مبنای سال‌های عادی است و ممکن است در سال‌های کبیسه ۱ روز جابه‌جا شود. مناسبت‌های قمری نیز در تقویم خورشیدی چرخشی هستند اما تاریخ قمری آن‌ها همیشه ثابت است.

---

## 🏷️ راهنمای انواع رویدادها (Event Types Reference)

| مقدار فیلد `type` | دسته‌بندی فارسی | توضیحات و کاربرد | نمونه رویدادها |
| :--- | :--- | :--- | :--- |
| **`celebration`** | جشن و شادباش | جشن‌های ملی، باستانی، اعیاد مذهبی و روزهای سرور | جشن نوروز، سده، یلدا |
| **`commemoration`** | بزرگداشت و یادمان | گرامیداشت مشاهیر، ادبا، دانشمندان و چهره‌های تاریخی | بزرگداشت فردوسی، حافظ |
| **`official`** | رویداد رسمی | وقایع تاریخی معاصر، رخدادهای تقویمی رسمی کشور | روز ملی شدن صنعت نفت |
| **`international`** | بین‌المللی و جهانی | مناسبت‌ها و روزهای جهانی سازمان ملل و یونسکو | روز جهانی زنان، روز جهانی صلح |
| **`mourning`** | سوگواری و شهادت | ایام سوگواری، رحلت و شهادت بزرگان دینی | تاسوعا، عاشورا، شب قدر |

---

## 🚀 نحوه استفاده سریع (Quick Start)

### با پایتون (Python):
```bash
python examples/python/merge_events.py
```

### با جاوااسکریپت (Node.js):
```bash
node examples/javascript/index.js
```

---

## 🤝 مشارکت (Contributing)

برای اضافه کردن رویداد جدید یا رفع باگ:
۱. پروژه را Fork کنید.
۲. تغییرات خود را در یک شاخه جدید (`feature/add-new-event`) اعمال کنید.
۳. حتماً اسکریپت `python scripts/validate_json.py` را اجرا کنید تا از صحت داده‌ها مطمئن شوید.
۴. یک Pull Request ثبت کنید.

---

<br><br>

# 🇬🇧 English Documentation

A lightweight, standardized, and structured JSON dataset for Persian (Jalali) calendar events, covering national, ancient, international, and lunar religious occasions. Ideal for calendar apps, scheduling tools, and bots.

## 📊 Data Schemas

All files use a monthly-keyed JSON object where keys represent month indices (`"01"` to `"12"`).

* **`national-events.json`**: Fixed Persian solar events (National holidays, ancient festivals).
* **`international-events.json`**: International events mapped to default Jalali days, including the exact `gregorian_date`. *(Note: Expect a ±1 day shift during leap years).*
* **`religious-events.json`**: Islamic events mapped across Lunar Hijri months.

### Object Fields:
* `id` (string): Unique slug identifier.
* `title` (string): Event name in Persian.
* `type` (string): Event category (`celebration`, `commemoration`, `official`, `international`, `mourning`).
* `day` / `hijri_day` (integer): Day of the month.
* `is_holiday` (boolean): `true` if it is an official national holiday in Iran.

## 🤝 Contributing
Contributions are highly appreciated! 
1. Fork the repository.
2. Create a new branch.
3. Validate your JSON formatting by running `python scripts/validate_json.py`.
4. Submit a Pull Request.

## 📄 License
This project is licensed under the [MIT License](LICENSE).
