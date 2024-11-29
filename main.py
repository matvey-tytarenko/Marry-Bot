from telebot import *
from g4f.client import Client
from config import API

bot = TeleBot(API)

def get_response(prompt):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{
            "role": "user",
            "content": prompt,
        }]
    )

    try:
        if(prompt.startswith("марина" or "привет")):
            return response.choices[0].message.content
        else:
            return response.choices[0].message.content
    except TypeError as e:
        print(f"Error: {e.message}")
    except ValueError as e:
        print(f"Error: {e.message}")
    except IndexError as e:
        print()

# Create Telegram Bot
@bot.message_handler(commands=['start'])
def start(message):
    text = f"Приветик {message.from_user.first_name} я твоя девушка с которой ты можешь поразговаривать!"
    bot.send_message(message.chat.id, text=text)
    photo = open('hello_picture.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(content_types=['text'])
def messages(message):

    if message.text == "у тебя красивая грудь" or "у тебя красивые сиськи":
        bot.send_message(message.chat.id, "извращенец")
        photo = open('chest.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, get_response(message.text))

bot.polling(non_stop=True)