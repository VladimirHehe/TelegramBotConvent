import requests
from bs4 import BeautifulSoup as BS


class Exchange:
    """Класс конвертации"""

    def __init__(self, amount, src, dst):
        self.amount = amount
        self.src = src
        self.dst = dst

    def exchange(self):
        url = f"https://www.xe.com/currencyconverter/convert/?Amount={self.amount}&From={self.src}&To={self.dst}"
        content = requests.get(url).content
        soup = BS(content, "html.parser")
        exchange_rate_html = soup.find_all("p")[2]
        result = exchange_rate_html.text
        return result


class Value_Open_courses:
    """Конвертация на рубль, для функции /current """

    def __init__(self, ):
        self.amount = 0
        self.src = None
        self.dst = None

    def USD_to_RUB(self):
        self.amount = 1
        self.src = 'USD'
        self.dst = 'RUB'
        url = f"https://www.xe.com/currencyconverter/convert/?Amount={self.amount}&From={self.src}&To={self.dst}"
        content = requests.get(url).content
        soup = BS(content, "html.parser")
        USD_RUB = soup.find_all("p")[2]
        result = USD_RUB.text[:5]
        return result

    def EUR_to_RUB(self):
        self.amount = 1
        self.src = 'EUR'
        self.dst = 'RUB'
        url = f"https://www.xe.com/currencyconverter/convert/?Amount={self.amount}&From={self.src}&To={self.dst}"
        content = requests.get(url).content
        soup = BS(content, "html.parser")
        EUR_RUB = soup.find_all("p")[2]
        result = EUR_RUB.text[:5]
        return result

    def CNY_to_RUB(self):
        self.amount = 1
        self.src = 'CNY'
        self.dst = 'RUB'
        url = f"https://www.xe.com/currencyconverter/convert/?Amount={self.amount}&From={self.src}&To={self.dst}"
        content = requests.get(url).content
        soup = BS(content, "html.parser")
        CNY_RUB = soup.find_all("p")[2]
        result = CNY_RUB.text[:5]
        return result

    def BYN_to_RUB(self):
        self.amount = 1
        self.src = "BYN"
        self.dst = 'RUB'
        url = f"https://www.xe.com/currencyconverter/convert/?Amount={self.amount}&From={self.src}&To={self.dst}"
        content = requests.get(url).content
        soup = BS(content, "html.parser")
        BYN_RUB = soup.find_all("p")[2]
        result = BYN_RUB.text[:5]
        return result

    def TRY_to_RUB(self):
        self.amount = 1
        self.src = "TRY"
        self.dst = 'RUB'
        url = f"https://www.xe.com/currencyconverter/convert/?Amount={self.amount}&From={self.src}&To={self.dst}"
        content = requests.get(url).content
        soup = BS(content, "html.parser")
        TRY_RUB = soup.find_all("p")[2]
        result = TRY_RUB.text[:5]
        return result


class Bot_Exception(Exception):
    """Класс ошибок"""

    pass


