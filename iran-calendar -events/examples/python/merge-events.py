import json
import os
from typing import Dict, List, Optional

# مسیردهی پویا به پوشه data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "data"))


def load_dataset(filename: str) -> Dict[str, List[dict]]:
    """خواندن فایل‌های JSON از پوشه data"""
    filepath = os.path.join(DATA_DIR, filename)
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"⚠️ هشدار: فایل {filename} پیدا نشد.")
        return {}


def merge_solar_events(month: str, holidays_only: bool = False) -> List[dict]:
    """ترکیب رویدادهای ملی و بین‌المللی برای یک ماه خورشیدی مشخص.

    :param month: شماره ماه دو رقمی ('01' تا '12')
    :param holidays_only: فیلتر کردن فقط تعطیلات رسمی
    :return: لیستی از مناسبت‌ها مرتب‌شده بر اساس روز ماه
    """
    national_data = load_dataset("national-events.json")
    international_data = load_dataset("international-events.json")

    merged = []

    # افزودن مناسبت‌های ملی همراه با تگ منبع
    for event in national_data.get(month, []):
        event_copy = event.copy()
        event_copy["calendar_type"] = "solar_national"
        merged.append(event_copy)

    # افزودن مناسبت‌های بین‌المللی همراه با تگ منبع
    for event in international_data.get(month, []):
        event_copy = event.copy()
        event_copy["calendar_type"] = "gregorian_mapped"
        merged.append(event_copy)

    # فیلتر کردن تعطیلات رسمی در صورت نیاز
    if holidays_only:
        merged = [e for e in merged if e.get("is_holiday", False)]

    # مرتب‌سازی رویدادها بر اساس روز ماه خورشیدی
    return sorted(merged, key=lambda x: x.get("day", 0))


def get_all_holidays() -> Dict[str, List[dict]]:
    """استخراج تمام تعطیلات رسمی سال (خورشیدی) تفکیک‌شده بر اساس ماه"""
    national_data = load_dataset("national-events.json")
    holidays_by_month = {}

    for month_key in [f"{i:02d}" for i in range(1, 13)]:
        events = national_data.get(month_key, [])
        holidays = [e for e in events if e.get("is_holiday", False)]
        if holidays:
            holidays_by_month[month_key] = holidays

    return holidays_by_month


if __name__ == "__main__":
    print("=" * 55)
    print("📅 دموی ادغام رویدادهای تقویم خورشیدی و بین‌المللی")
    print("=" * 55)

    # مثال ۱: ادغام مناسبت‌های ماه فروردین (01)
    target_month = "01"
    events_m1 = merge_solar_events(target_month)

    print(f"\n📌 رویدادهای ماه {target_month}:")
    for ev in events_m1:
        badge = "🔴 [تعطیل]" if ev.get("is_holiday") else "⚪"
        source = "ملی" if ev["calendar_type"] == "solar_national" else "بین‌المللی"
        print(f"روز {ev['day']:02d} | {badge} ({source}) {ev['title']}")

    # مثال ۲: لیست تمام تعطیلات رسمی تقویم ملی در طول سال
    print("\n" + "=" * 55)
    print("🛑 لیست تمام تعطیلات تقویم ملی در طول سال:")
    print("=" * 55)
    all_hols = get_all_holidays()
    for m, items in all_hols.items():
        for item in items:
            print(f"ماه {m} / روز {item['day']:02d} : {item['title']}")