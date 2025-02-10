import requests
API_key="141710af2113bab9f55ef73e1bcd33d5"

def get_data(place,forecast_days):
    url=f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}&units=metric"
    responce=requests.get(url)
    data=responce.json()
    filtered_data=data["list"]
    nr_values=8*forecast_days
    filtered_data=filtered_data[:nr_values]
    return filtered_data

if __name__=="__main__":
    print(get_data(place="TOKYO",forecast_days=3))  