#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests as req

resp = req.get("https://ru.wikipedia.org/wiki/%D0%9A%D0%B8%D0%B2%D0%B8_(%D0%BF%D1%82%D0%B8%D1%86%D1%8B)")

#soup = BeautifulSoup(resp.text, 'html.parser')
# contents = resp.read()
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup.prettify())