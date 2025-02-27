import requests
import json

# URL API
url = "https://api.torob.com/v4/base-product/details-log-click/"
params = {
    "source": "next_desktop",
    "discover_method": "browse",
    "_bt__experiment": "",
    "prk": "d050a4d4-2df4-4101-b6ac-7a984fb03d38",
    "is_adv": "",
    "rank": 37,
    "search_id": "6722905e3b87a1ffe178620a",
    "suid": "6722902428921a313dfc87f3"  # شناسه محصول
}

# ارسال درخواست
response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()  # دریافت پاسخ در قالب JSON
    print(json.dumps(data, indent=4))  # چاپ کل پاسخ JSON

    # استخراج قیمت از داده‌ها
    if "data" in data and "current_price" in data["data"]:
        price = data["data"]["current_price"]
    else:
        price = "قیمت موجود نیست"

    print("قیمت محصول:", price)
else:
    print("درخواست موفقیت‌آمیز نبود:", response.status_code)
