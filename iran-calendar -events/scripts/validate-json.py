import glob
import json
import os
import sys

def validate_repository():
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    json_files = glob.glob(os.path.join(data_dir, "*.json"))

    if not json_files:
        print("❌ خطایی رخ داد: فایلی در پوشه data پیدا نشد.")
        sys.exit(1)

    seen_ids = set()
    total_events = 0
    errors = []

    expected_months = {f"{i:02d}" for i in range(1, 13)}

    for file_path in json_files:
        filename = os.path.basename(file_path)
        print(f"🔍 در حال بررسی {filename} ...")

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            errors.append(f"[{filename}] خطای سینتکس JSON: {e}")
            continue

        if not isinstance(data, dict):
            errors.append(f"[{filename}] ریشه فایل باید یک آبجکت (dict) باشد.")
            continue

        for month, events in data.items():
            if month not in expected_months:
                errors.append(f"[{filename}] کلید ماه نامعتبر است: {month} (باید بین 01 تا 12 باشد)")

            if not isinstance(events, list):
                errors.append(f"[{filename}] مقدار ماه {month} باید یک آرایه (list) باشد.")
                continue

            for event in events:
                total_events += 1
                event_id = event.get("id")

                # بررسی فیلدهای اجباری
                if not event_id:
                    errors.append(f"[{filename}] یک رویداد در ماه {month} فاقد id است: {event}")
                elif event_id in seen_ids:
                    errors.append(f"[{filename}] شناسه تکراری پیدا شد: {event_id}")
                else:
                    seen_ids.add(event_id)

                if "title" not in event:
                    errors.append(f"[{filename}] رویداد '{event_id}' فاقد title است.")

                # بررسی فیلد روز
                day_field = "hijri_day" if "religious" in filename else "day"
                day_val = event.get(day_field)
                if not isinstance(day_val, int) or not (1 <= day_val <= 31):
                    errors.append(f"[{filename}] روز نامعتبر برای رویداد '{event_id}': {day_val}")

    if errors:
        print("\n❌ خطاهای شناسایی‌شده:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print(f"\n✅ تمام فایل‌ها معتبر هستند! مجموعاً {total_events} مناسبت یکتا با موفقیت ثبت و تایید شد.")

if __name__ == "__main__":
    validate_repository()