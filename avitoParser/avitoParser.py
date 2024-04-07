import requests
from bs4 import BeautifulSoup as bs
import socks
import socket
import os

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}

urlSelected = input("Введите ссылку на поиск авито\n")

# Пример прокси SOCKS5
socks.set_default_proxy(socks.SOCKS4, "1.4.192.248", 4145)
socket.socket = socks.socksocket

req = requests.get(urlSelected, headers=headers, verify=False)
print(req.status_code)

if req.status_code == 200:
    print("К сайту подключился, скачиваю код страницы")
    
    src = req.text
    
    # Сохраняем HTML-код страницы в файл
    with open("page.html", "w", encoding="utf-8") as file:
        file.write(src)
    print("HTML-код страницы успешно сохранен в файле 'page.html'")
    os.system("python havefile.py")
else:
    print("Ошибка при загрузке страницы. Код ответа:", req.status_code)