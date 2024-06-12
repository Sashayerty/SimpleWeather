from data.get_weather import get_weather as get
from data.simple_weather_action import simple_weather_action as hi

def simple_weather(place):
    print(get(place))

def main():
    if __name__ == '__main__':
        hi()
        simple_weather(input('Введите место:'))

main()

