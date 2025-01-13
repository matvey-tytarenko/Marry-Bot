from flask import Flask
import telegram

app = Flask(__name__)

@app.route('/hook', methods=['POST'])
def webhook():
    telegram.main()
    return 'Ok'

if __name__ == '__main__':
    app.run(port=5000)