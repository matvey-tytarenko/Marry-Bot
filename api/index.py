from http.server import BaseHTTPRequestHandler
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
import config


bot = Bot(token=config.VERCEL_API)
dispatcher = Dispatcher(bot, None, workers=0)

def start(update, context):
    update.message.reply_text("Bot starting on Vercel")

dispatcher.add_handler(CommandHandler("start", start))

class Handler(BaseHTTPRequestHandler):
    def POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        update = Update.de_json(eval(body), bot)
        dispatcher.process_update(update)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")