from data.get_weather import get_weather as get
from data.simple_weather_action import simple_weather_action as hi

def simple_weather(place)-> None:
    print(get(place).replace('Follow @igor_chubin for wttr.in updates', ""))

if __name__ == '__main__':
    hi()
    simple_weather(input('Введите место:'))


