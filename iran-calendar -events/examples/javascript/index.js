const fs = require('fs');
const path = require('path');

// مسیردهی پویا به پوشه data
const DATA_DIR = path.resolve(__dirname, '../../data');

/**
 * خواندن فایل‌های JSON به صورت ایمن
 * @param {string} filename 
 * @returns {object}
 */
function loadJson(filename) {
  const filePath = path.join(DATA_DIR, filename);
  try {
    const rawData = fs.readFileSync(filePath, 'utf-8');
    return JSON.parse(rawData);
  } catch (error) {
    console.error(`⚠️ خطا در خواندن فایل ${filename}:`, error.message);
    return {};
  }
}

/**
 * ادغام مناسبت‌های ملی و بین‌المللی برای یک ماه خورشیدی
 * @param {string} month شماره ماه دو رقمی ('01' تا '12')
 * @param {boolean} holidaysOnly فیلتر کردن فقط تعطیلات رسمی
 * @returns {Array} آرایه‌ای از مناسبت‌ها مرتب‌شده بر اساس روز
 */
function getSolarMonthEvents(month, holidaysOnly = false) {
  const nationalData = loadJson('national-events.json');
  const internationalData = loadJson('international-events.json');

  const nationalEvents = (nationalData[month] || []).map(event => ({
    ...event,
    calendar_type: 'solar_national'
  }));

  const internationalEvents = (internationalData[month] || []).map(event => ({
    ...event,
    calendar_type: 'gregorian_mapped'
  }));

  let merged = [...nationalEvents, ...internationalEvents];

  if (holidaysOnly) {
    merged = merged.filter(event => event.is_holiday);
  }

  // مرتب‌سازی بر اساس روز ماه
  return merged.sort((a, b) => (a.day || 0) - (b.day || 0));
}

/**
 * دریافت مناسبت‌های یک ماه قمری
 * @param {string} lunarMonth شماره ماه قمری دو رقمی ('01' تا '12')
 * @returns {Array}
 */
function getHijriEvents(lunarMonth) {
  const religiousData = loadJson('religious-events.json');
  const events = religiousData[lunarMonth] || [];
  return events.sort((a, b) => (a.hijri_day || 0) - (b.hijri_day || 0));
}

// ========================
// دمو و اجرای تستی در کنسول
// ========================
console.log('='.repeat(55));
console.log('📅 دموی جاوااسکریپت (Node.js) تقویم مناسبت‌ها');
console.log('='.repeat(55));

// مثال ۱: رویدادهای ماه فروردین (01)
const farvardinEvents = getSolarMonthEvents('01');
console.log('\n📌 مناسبت‌های ماه فروردین:');
farvardinEvents.forEach(ev => {
  const badge = ev.is_holiday ? '🔴 [تعطیل]' : '⚪';
  const source = ev.calendar_type === 'solar_national' ? 'ملی' : 'بین‌المللی';
  console.log(`روز ${String(ev.day).padStart(2, '0')} | ${badge} (${source}) ${ev.title}`);
});

// مثال ۲: مناسبت‌های ماه محرم (01 قمری)
console.log('\n📌 مناسبت‌های ماه محرم:');
const muharramEvents = getHijriEvents('01');
muharramEvents.forEach(ev => {
  console.log(`روز ${String(ev.hijri_day).padStart(2, '0')} محرم | ${ev.title}`);
});

// اکسپورت توابع برای استفاده در پکیج‌ها یا فریم‌ورک‌ها (React / Vue / Express)
module.exports = {
  getSolarMonthEvents,
  getHijriEvents
};