from telebot import TeleBot
from g4f.client import Client
from config import API
import os
import random

bot = TeleBot(API)

def get_response(prompt):
    client = Client()
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except (TypeError, ValueError, IndexError) as e:
        print(f"Error: {str(e)}")
        return "К сожалению, я не могу сейчас ответить."

# Create Telegram Bot
@bot.message_handler(commands=['start'])
def start(message):
    text = f"Приветик {message.from_user.first_name}, я твоя девушка, с которой ты можешь поразговаривать!"
    bot.send_message(message.chat.id, text=text)
    with open('hello_picture.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

@bot.message_handler(content_types=['text'])
def messages(message):
    chest = ["у тебя красивая грудь", "У тебя красивая грудь", "У тебя красивые сиськи" "у тебя красивые сиськи", "Ты секси", "ты секси"]
    ass = ["У тебя классная попа", "у тебя классная попа", "скинь жопу", "Скинь жопу", "Скинь попу", "скинь попу"]
    cute = ["я тебя люблю", "ты милая", "ты красивая", "ты мне нравишься", "Я тебя люблю", "Ты мне нравишься", "Ты милая", "Ты красивая"]
    randomis = ["bunny.jpg", "black.jpg", "christmass.jpg"]

    if message.text in chest:
        collage = ['chest.jpg', 'sexy.jpg']
        bot.send_message(message.chat.id, "Извращенец!")
        with open(random.choice(collage), 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    elif message.text in cute:
        collage = ['cute.jpg', 'sex.jpg']
        bot.send_message(message.chat.id, "Ой п..п..п..Правда?")
        with open(random.choice(collage), 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "💋")
    elif message.text in ass:
        if message.text.startswith("скинь"):
         bot.send_message(message.chat.id, "Извращенец!")
         with open(random.choice(randomis), "rb") as photo:
             bot.send_photo(message.chat.id, photo)
             bot.send_message(message.chat.id, "❤️")
    else:
        bot.send_message(message.chat.id, get_response(message.text))

def main():
    bot.polling(non_stop=True)

if __name__ == '__main__':
    main();