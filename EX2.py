from colorama import Style, Fore
colors = [Fore.CYAN, Fore.LIGHTRED_EX, Fore.LIGHTBLUE_EX]

countries = {}
def get_strings():
    while True:
        s = input(f"{colors[0]} Введите строку (оставить пустым для завершения): {Style.RESET_ALL}")
        if not s:
            break
        words = s.split()
        country = words[0]
        cities = words[1:]
        countries[country] = cities


def country_by_city(city):
    for country, cities in countries.items():
        if city in cities:
            print(f"{colors[2]}[✓] {country} {Style.RESET_ALL}")
            return
    print(f"{colors[1]}[!] Город не найден {Style.RESET_ALL}")

if __name__ == '__main__':
    print(f"{colors[0]} Введите строки в формате (<Страна> [Города] {Style.RESET_ALL}")
    get_strings()
    request = input(f"{colors[0]} Введите город для поиска (оставить пустым для завершения): {Style.RESET_ALL}")
    while request:
        country_by_city(request)
        request = input(f"{colors[0]} Введите город для поиска (оставить пустым для завершения): {Style.RESET_ALL}")