import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

city_name = "Pune"
API_key = "9dba861a1bfdaecc9a72dac8088b9873"

url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_key}&units=metric"


response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    forecast_data = []

    for item in data["list"]:
        forecast_data.append({
            "DateTime": item["dt_txt"],
            "Temperature": item["main"]["temp"],
            "Humidity": item["main"]["humidity"]
        })

    df = pd.DataFrame(forecast_data)

    df["DateTime"] = pd.to_datetime(df["DateTime"])

    print(df.head())

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
sns.lineplot(data=df, x="DateTime", y="Temperature")
plt.title(f"5-Day Temperature Forecast for {city_name}")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.subplot(2, 1, 2)
sns.lineplot(data=df, x="DateTime", y="Humidity")
plt.title(f"5-Day Humidity Forecast for {city_name}")
plt.ylabel("Humidity (%)")
plt.xlabel("Date & Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()