
import jdatetime
from pytrends.request import TrendReq
import pandas as pd



pytrends = TrendReq(hl='fa-IR', tz=210)
keywords = ["اسباب بازی"]




start_date = jdatetime.date(1400, 1, 1).togregorian()  # تبدیل به میلادی
end_date = pd.Timestamp.today()
timeframe = f"{start_date.strftime('%Y-%m-%d')} {end_date.strftime('%Y-%m-%d')}"



pytrends.build_payload(keywords, timeframe=timeframe, geo='IR')
trend_data = pytrends.interest_over_time()



monthly_trend = trend_data.resample('M').mean()
monthly_trend.index = monthly_trend.index.map(
    lambda x: jdatetime.date.fromgregorian(date=x).strftime('%Y-%m (%B)')
)



max_value = monthly_trend[keywords[0]].max()
normalized_trend = monthly_trend.copy()
normalized_trend[keywords[0]] = (monthly_trend[keywords[0]] / max_value) * 100  # نرمالیزه شده 0-100نرمالیزه شده 0-100



print("\nروند ماهانه از ۱۴۰۰ تا امروز:")
print(normalized_trend.drop(columns=['isPartial'], errors='ignore'))

print(f"\nبیشترین میزان جستجو: {max_value:.2f} مربوط به ماه:")
trend_
print(monthly_trend[monthly_trend[keywords[0]] == max_value].index[0])




suggestions = pytrends.suggestions("اسباب بازی")
suggestions_df = pd.DataFrame(suggestions)
print("\nپیشنهادهای جستجوی مرتبط:")
print(suggestions_df)




geo_data = pytrends.interest_by_region(resolution='REGION')
top_cities = geo_data.sort_values(by="اسباب بازی", ascending=False).head(10)
print("\nشهرهای با بیشترین جستجو:")
print(top_cities)



plt.figure(figsize=(14, 8))



# نمودار روند زمانی
plt.subplot(2, 2, 1)
trend_data['اسباب بازی'].plot(title='روند جستجوی "اسباب بازی" در یک سال اخیر')
plt.ylabel('میزان جستجو (نسبی)')


# نمودار ماهانه
plt.subplot(2, 2, 2)
monthly_trend['اسباب بازی'].plot(kind='bar', title='میانگین جستجوی ماهانه')
plt.xticks(rotation=45)



# نمودار جغرافیایی
plt.subplot(2, 2, 4)
top_cities['اسباب بازی'].plot(kind='barh', title='شهرهای پرجستجو')
plt.tight_layout()
plt.show()



monthly_trend.to_csv('monthly_trend.csv', encoding='utf-8-sig')
print("\nنتایج در فایل monthly_trend.csv ذخیره شد.")

