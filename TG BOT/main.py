import telebot
import wikipedia

wikipedia.set_lang('ru')

from pyowm import OWM
bot = telebot.TeleBot('6329014684:AAFAAHADigGW8Mx16Xtw9iMqTzgj51xuxPs')
OPENWEATHERMAP_API_KEY = '10df59d82a2daeb6a90925fabe950b58'
owm = OWM(OPENWEATHERMAP_API_KEY)

@bot.message_handler(commands = ['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать информацию о городе или погоду в нём? Тогда тебе именно ко мне! '
                                      'команды: /weather [город] - покажет какая погода в городе. /wiki [слово] - покажет тебе короткую информацию о городе или любом слове')

@bot.message_handler(commands = ['help'])
def main(message):
    bot.send_message(message.chat.id,'/weather [город] - покажет погоду в городе. \n'
                                     '/wiki [слово]  - покажет короткую информацию о городе или любом слове')
@bot.message_handler(commands = ['wiki'])
def wiki(message):
    user_input1 = message.text.split(' ', 1)[1] if len(message.text.split(' ', 1)) > 1 else None
    if not user_input1:
        bot.send_message(message.chat.id, "Пожалуйста, укажите слово о котором хотите узнать информацию после команды /wiki.")
        return
    summary = wikipedia.summary(user_input1)
    bot.send_message(message.chat.id, summary)

@bot.message_handler(commands=['weather'])
def weather(message):
    user_input = message.text.split(' ', 1)[1] if len(message.text.split(' ', 1)) > 1 else None

    if not user_input:
        bot.send_message(message.chat.id, "Пожалуйста, укажите город после команды /weather.")
        return

    observation = owm.weather_manager().weather_at_place(user_input)

    if observation is None:
        bot.send_message(message.chat.id, "Не удалось получить данные о погоде.")
        return

    weather = observation.weather

    temperature = weather.temperature('celsius')['temp']
    description = weather.detailed_status

    response = f'Температура в {user_input}: {temperature}°C, {description}'
    bot.send_message(message.chat.id, response)

bot.polling(none_stop = True)