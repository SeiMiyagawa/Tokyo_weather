from types import CoroutineType
import requests
from bs4 import BeautifulSoup 

cities = [["千代田区", "4410/13101/"], ["中央区", "4410/13102/"], \
         ["港区", "4410/13103/"], ["新宿区", "4410/13104/"], \
         ["文京区", "4410/13105/"], ["台東区", "4410/13106/"], \
         ["墨田区", "4410/13107/"], ["江東区", "4410/13108/"], \
         ["品川区", "4410/13109/"], ["目黒区", "4410/13110/"], \
         ["大田区", "4410/13111/"], ["世田谷区", "4410/13112/"], \
         ["渋谷区", "4410/13113/"], ["中野区", "4410/13114/"], \
         ["杉並区", "4410/13115/"], ["豊島区", "4410/13116/"], \
         ["北区", "4410/13117/"], ["荒川区", "4410/13118/"], \
         ["板橋区", "4410/13119/"], ["練馬区", "4410/13120/"], \
         ["足立区", "4410/13121/"], ["葛飾区", "4410/13122/"], \
         ["江戸川区", "4410/13123/"], \
         ["八王子市", "4410/13201/"], ["立川市", "4410/13202/"], \
         ["武蔵野市", "4410/13203/"], ["三鷹市", "4410/13204/"], \
         ["青梅市", "4410/13205/"], ["府中市", "4410/13206/"], \
         ["昭島市", "4410/13207/"], ["調布市", "4410/13208/"], \
         ["町田市", "4410/13209/"], ["小金井市", "4410/13210/"], \
         ["小平市", "4410/13211/"], ["日野市", "4410/13212/"], \
         ["東村山市", "4410/13213/"], ["国分寺市", "4410/13214/"], \
         ["国立市","4410/13215/"], ["福生市", "4410/13218/"], \
         ["狛江市", "4410/13219/"], ["東大和市", "4410/13220/"], \
         ["清瀬市", "4410/13221/"], ["東久留米市", "4410/13222/"], \
         ["武蔵村山市", "4410/13223/"], ["多摩市", "4410/13224/"], \
         ["稲城市", "4410/13225/"], ["羽村市", "4410/13227/"], \
         ["あきる野市", "4410/13228/"], ["西東京市", "4410/13229/"], \
         ["瑞穂町", "4410/13303/"], ["日の出町", "4410/13305/"], \
         ["檜原村", "4410/13307/"], ["奥多摩町", "4410/13308/"], \
         ["大島町", "4410/13361/"], ["利島村", "4410/13162/"], \
         ["新島村", "4410/13161/"], ["神津島村", "4410/13164/"], \
         ["三宅村", "4410/13181/"], ["御蔵島村", "4410/13182/"], \
         ["八丈町", "4410/13401/"], ["青ヶ島村", "4410/13402/"], \
         ["小笠原村", "4410/13421/"]]

url = 'https://tenki.jp/forecast/3/16/'

res = requests.get(url)

bs  = BeautifulSoup(res.content, "html.parser")

correct = False

while not correct:
    input_name = input("東京都の市区町村名を入力してください：")
    for city in cities:
        if input_name == city[0]:
            url += city[1]
            correct = True    
    if correct:
        today_data = bs.find(class_="today-weather")
        tomorrow_data = bs.find(class_="tomorrow-weather")
        today_weather = today_data.p.string
        tomorrow_weather = tomorrow_data.p.string
        today_temp = today_data.div.find(class_="date-value-wrap")
        tomorrow_temp = tomorrow_data.div.find(class_="date-value-wrap")
        today_temp = today_temp.find_all("dd")
        today_temp_max = today_temp[0].span.string
        today_temp_max_diff = today_temp[1].string
        today_temp_min = today_temp[2].span.string
        today_temp_min_diff = today_temp[3].string
        tomorrow_temp = tomorrow_temp.find_all("dd")
        tomorrow_temp_max = tomorrow_temp[0].span.string
        tomorrow_temp_max_diff = tomorrow_temp[1].string
        tomorrow_temp_min = tomorrow_temp[2].span.string
        tomorrow_temp_min_diff = tomorrow_temp[3].string
        today_react = ""
        tomorrow_react = ""
        s = ":sunny:"
        c = ":cloud:"
        r = ":umbrella_with_rain_drops:"
        if "晴" in today_weather:
            today_react += s
        if "曇" in today_weather:
            today_react += c
        if "雨" in today_weather:
            today_react += r
        if "晴" in tomorrow_weather:
            tomorrow_react += s
        if "曇" in tomorrow_weather:
            tomorrow_react += c
        if "雨" in tomorrow_weather:
            tomorrow_react += r
        today = []
        tomorrow = []
        re_title = f'東京都{input_name}の天気'
        re_today = ""
        re_tomorrow = ""
        today.append("今日")
        today.append("天気：{}".format(today_weather) + today_react)
        today.append("最高気温：{}".format(today_temp_max,today_temp_max_diff))
        today.append("最低気温：{}".format(today_temp_min,today_temp_min_diff))
        tomorrow.append("明日")
        tomorrow.append("天気: {}".format(tomorrow_weather) + tomorrow_react)
        tomorrow.append("最高気温：{}".format(tomorrow_temp_max,tomorrow_temp_max_diff))
        tomorrow.append("最低気温：{}".format(tomorrow_temp_min,tomorrow_temp_min_diff))
        for i in today:
            re_today += "\n"
            re_today += i
        for j in tomorrow:
            re_tomorrow += "\n"
            re_tomorrow += j
        print()
        print(re_title)
        print(re_today)
        print(re_tomorrow)
    else:
        print()
        print("正しい市区町村名を入力してください。")
        print()