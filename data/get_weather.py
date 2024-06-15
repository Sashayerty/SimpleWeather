from requests import request
def get_weather(place:str) -> str:
    res = request(url=f'http://wttr.in/{place}?Tq', method='GET').text
    print(f'Получены данные для {place}/{place} data received')
    return res