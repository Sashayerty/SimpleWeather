# SimpleWeather - это приложение с простым UI, которое показывает погоду.
```bash
      _____ _                 _   __          __        _   _               
     / ____(_)               | |  \ \        / /       | | | |              
    | (___  _ _ __ ___  _ __ | | __\ \  /\  / /__  __ _| |_| |__   ___ _ __ 
     \___ \| | '_ ` _ \| '_ \| |/ _ \ \/  \/ / _ \/ _` | __| '_ \ / _ \ '__|
     ____) | | | | | | | |_) | |  __/\  /\  /  __/ (_| | |_| | | |  __/ |   
    |_____/|_|_| |_| |_| .__/|_|\___| \/  \/ \___|\__,_|\__|_| |_|\___|_|   
                       | |                                                  
                       |_|

```
Приложение еще не сделано до конца.
1. API, которое я использую: [wttr.in](https://github.com/chubin/wttr.in)
2. Интерфейс приложения сделан с помощью QTDesigner. (Я не дизайнер)
3. Backend написан на Python.
# Строение проектика:
```bash
SIMPLEWEATHER/
├── data/
│   ├── get_weather.py
│   ├── simple_weather_action.py
├── templates/
│   └── weather.py
├── main.py
├── place.json
├── requirements.txt
├── simple_weather_console.py
```
# Назначение и использование файлов:
Расскажу только про 2 файла:
- main.py
- simple_weather_console.py
## main.py - основная программа с UI
## simple_weather_console.py - консольная программа
