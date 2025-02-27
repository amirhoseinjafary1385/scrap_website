import requests
import BeautifulSoup

r = requests.get("https://www.geeksforgeeks.org/python-programming-language/")

soup = BeautifulSoup(r.content, "html-parser")

s = soup.find("div", class_= "entry-content")
content = s.find_all("p")


for paragraph in content:

    print(paragraph.get_text())