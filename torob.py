


# import requests
# from bs4 import BeautifulSoup
# import json

# print("خوش آمدید...")

# # بررسی اتصال اینترنت
# try:
#     requests.get("https://www.torob.com/", timeout=2)
# except (requests.ConnectionError, requests.Timeout):
#     print("اینترنت شما تمام شده است...")
# else:
#     urls = [
#         "https://torob.com/browse/175/%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D9%88-%DA%A9%D8%A7%D9%84%D8%A7%DB%8C-%D8%AF%DB%8C%D8%AC%DB%8C%D8%AA%D8%A7%D9%84/"
#     ]

#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
#     }

#     all_products = []

#     for url in urls:
#         fetch = requests.get(url, headers=headers)
#         if fetch.status_code == 200:
#             print(f"محتوا از {url} با موفقیت دریافت شد.")
#             soup = BeautifulSoup(fetch.text, 'html.parser')
#             products = soup.find_all('div', class_='desktopProductCard_card__Yvahe')

#             # چاپ محتوای HTML برای بررسی
#             print(soup.prettify())  # این خط برای بررسی وجود عنصر قیمت است.

#             for product in products:
#                 title_element = product.find('h2', class_='desktopProductCard_product-name__qSDp9')
#                 price_element = product.find('span', class_='desktopProductCard_product-price-text__folP0')  # اصلاح کلاس قیمت اگر لازم است
#                 image_element = product.find('img')
                
#                 title = title_element.get_text(strip=True) if title_element else "عنوان موجود نیست"

#                 # بررسی وجود قیمت
#                 if price_element:
#                     price = price_element.get_text(strip=True)
#                 else:
#                     price = "قیمت موجود نیست"
#                     print("قیمت در این محصول یافت نشد.")  # پیام خطا برای عیب‌یابی

#                 # انتخاب تصویر با کیفیت بالاتر از srcset
#                 image_url = image_element.get('srcset', '').split(',')[1].split()[0] if image_element else "تصویر موجود نیست"

#                 # اضافه کردن محصول به لیست
#                 all_products.append({
#                     "product": title,
#                     "price": price,
#                     "image_url": image_url
#                 })

#             with open("Phone.json", "w", encoding="utf-8") as file:
#                 json.dump(all_products, file, ensure_ascii=False, indent=4)

#             print("داده‌ها با موفقیت در فایل Phone.json ذخیره شدند.")
#         else:
#             print(f"محتوا از {url} با موفقیت دریافت نشد. کد وضعیت: {fetch.status_code}")

#         print(f"تعداد محصولات پیدا شده: {len(products)}")



import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
r = requests.get("https://www.geeksforgeeks.org/python-programming-language/")

# Create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(r.content, "html.parser")

# Find the div with class "entry-content"
s = soup.find("div", class_="entry-content")

# Find all paragraph tags within that div
content = s.find_all("p")

# Print the text of each paragraph
for paragraph in content:
    print(paragraph.get_text())