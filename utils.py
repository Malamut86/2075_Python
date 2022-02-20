import requests


def currency_rates(code: str)-> float:
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    valute_info = response.text
    valute_index = valute_info.find(code.upper())
    if valute_index != -1:
        valute_info = valute_info[valute_index:valute_info.find('</Value>', valute_index)]
        nominal = float(valute_info[valute_info.find('<Nominal>') + 9:
                                    valute_info.find('</Nominal>')].replace(',', '.'))
        result_value = float(valute_info[valute_info.find('<Value>') + 7:].replace(',', '.'))
    else:
        return
    return result_value


print(currency_rates("CHF"),('RYB'))
print(currency_rates("AUD"),('RYB'))
print(currency_rates("GBP"),('RYB'))
print(currency_rates("BYN"),('RYB'))