import requests
from bs4 import BeautifulSoup as bs
# req = requests.get(urlSelected)
# print(req.status_code)

prices = []  # Список для хранения всех цен

with open("page.html", "r", encoding="utf-8") as file:
    src = file.read()
    soup = bs(src, "html.parser")
    
    meta_prices = soup.find_all('meta', attrs={'itemprop': 'price'})
    
    if meta_prices:
        for meta_price in meta_prices:
            price_content = meta_price['content']  # Получаем содержимое атрибута content
            prices.append(float(price_content))  # Добавляем цену в список, преобразовав её в числовой формат

        if prices:
            average_price = sum(prices) / len(prices)  # Вычисляем среднее значение всех цен
            print("Средняя цена:", average_price)
        else:
            print("Цены не найдены")
    else:
        print("Цены не найдены")