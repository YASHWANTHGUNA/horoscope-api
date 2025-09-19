import requests
from bs4 import BeautifulSoup
from core import cache

@cache.cached()
def get_horoscope_by_day(zodiac_sign: int, day: str):
    """Fetches the daily horoscope text."""
    if not "-" in day:
        url = f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
    else:
        day_formatted = day.replace("-", "")
        url = f"https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign={zodiac_sign}&laDate={day_formatted}"
    
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    
    # Return horoscope text only if found
    if data and data.p:
        return data.p.text
    return None

@cache.cached()
def get_horoscope_by_week(zodiac_sign: int):
    """Fetches the weekly horoscope text."""
    url = f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-weekly.aspx?sign={zodiac_sign}"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})

    # Return horoscope text only if found
    if data and data.p:
        return data.p.text
    return None

@cache.cached()
def get_horoscope_by_month(zodiac_sign: int):
    """Fetches the monthly horoscope text."""
    url = f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-monthly.aspx?sign={zodiac_sign}"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    
    # Return horoscope text only if found
    if data and data.p:
        return data.p.text
    return None