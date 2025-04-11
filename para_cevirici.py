#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 23:28:30 2025

@author: ceydaaygun
"""

import requests

while True:
    amount = input("Çevirmek istediğin miktarı gir: ")
    from_currency = input("Hangi para biriminden? (Örn: EUR): ").upper()
    to_currency = input("Hangi para birimine? (Örn: USD): ").upper()

    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
    response = requests.get(url)
    data = response.json()

    if "rates" not in data:
        print("Hatalı para birimi girdiniz. Lütfen tekrar deneyin.")
    else:
        converted_amount = data['rates'][to_currency]
        date = data['date']  # Tarih bilgisi
        print(f"\nDöviz kuru tarihi: {date}")
        print(f"{amount} {from_currency} = {converted_amount} {to_currency}\n")

    again = input("Başka bir işlem yapmak ister misin? (e/h): ").lower()
    if again != "e":
        print("Görüşmek üzere!")
        break