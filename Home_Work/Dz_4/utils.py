import decimal as dc
import requests


def currency_rates(currency_code = "", url = 'http://www.cbr.ru/scripts/XML_daily.asp'):
    if not (currency_code and url):
        return None
    elif currency_code.isalpha() == False:
        return None
    elif len(currency_code) != 3:
        return None

    currency_code = currency_code.upper()

    response = requests.get(url)
    text = response.text

    find_index_currency_code = text.find(currency_code)
    find_index_value = text.find("Value", find_index_currency_code)

    value_index_a = find_index_value + 6
    value_index_b = text.find("</Value>",find_index_currency_code)

    slise_value = text[value_index_a:value_index_b]

    value = float(slise_value.replace(",", "."))

    value = dc.Decimal(value)
    value = value.quantize(dc.Decimal("1.00"))



    return value