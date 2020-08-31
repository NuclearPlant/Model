import telebot
from datetime import datetime
from datetime import timedelta
from datetime import time
import math
import time

bot = telebot.TeleBot('870369247:AAEZwx6__BaRmz-ivxkZO-_WCoYz7lMny5E')

#@bot.message_handler(commands=['leysan_end_of_working_day_timer'])
@bot.message_handler(content_types=["text"])
def start_message(message):
    if message.text == "/leysan_end_of_working_day_timer":
        bot.send_message(message.chat.id,"Во сколько ты пришла, {}?".format(message.from_user.first_name))
    now = datetime.now()
    #now = datetime(2020, 8, 31, 18, 30, 2)
    end_of_day = datetime (now.year, now.month, now.day, 18, 30)
    bot.send_message(message.chat.id,"Точное время {}:{}".format(now.hour,now.minute))
    if end_of_day > now:
        left = end_of_day - now
        hour = left.seconds // 3600
        minutes = math.ceil((left.seconds / 60) - hour*60)
        text_left = 'осталось'
        text_hour = ' часов '
        text_minutes = ' минут'
        min_mod = minutes % 10
        if hour >= 8 and minutes > 0:
            bot.send_message(message.chat.id,"Ужас, ты что, уже на работе?")
            time.sleep(10)
        elif hour == 0:
            text_hour = ''
            hour = ''
            if minutes % 10 == 1 and minutes != 11:
                text_left = 'осталась'
                text_minutes = ' минута'
        elif hour == 1:
            text_hour = ' час '
            text_left = 'остался'
        elif 2 <= hour <= 4:
            text_hour = ' часа '
        if minutes == 0:
            text_minutes = ''
        elif minutes % 10 == 1 and minutes != 11:
                text_minutes = ' минута'
        elif 2 <= min_mod <= 4 and minutes != 12 and minutes != 13 and minutes != 14:
            text_minutes = ' минуты'
        bot.send_message(message.chat.id,"До конца рабочего дня {} {}{}{}{}".format(text_left,hour,text_hour,minutes,text_minutes))
    
    elif end_of_day < now:
        left = now - end_of_day
        hour = left.seconds // 3600
        minutes = math.floor((left.seconds / 60) - hour*60)
        text_hour = ' часов '
        if hour == 0:
            text_hour = ''
            hour = ''
        elif hour == 1:
            text_hour = ' час '
        elif 2 <= hour <= 4:
            text_hour = ' часа '
        text_minutes = ' минут '
        min_mod = minutes % 10
        if minutes == 0:
            text_minutes = ''
            minutes = ''
        elif minutes % 10 == 1 and minutes != 11:
            text_minutes = ' минуту '
        elif 2 <= min_mod <= 4 and minutes != 12 and minutes != 13 and minutes != 14:
            text_minutes = ' минуты '
        if end_of_day.hour == now.hour and end_of_day.minute == now.minute:
            bot.send_message(message.chat.id,"Пора домой, пока-пока!")
        else:
            bot.send_message(message.chat.id,"Ты чего ещё не дома? Рабочий день закончился {}{}{}{}назад!".format(hour,text_hour,minutes,text_minutes))

    elif end_of_day == now:
        bot.send_message(message.chat.id,"Пора домой, пока-пока!")
        

bot.polling(none_stop = True) 
