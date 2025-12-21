from flask import Flask
import asyncio
import time


app = Flask(__name__)


@app.route('/')
def home():
    return 'Это главаная страница.'

@app.route('/about')
def aboute():
    return 'Здесь будет информация об авторе сайта.'

@app.route('/blog')
def blog():
    return 'Это блог с заметками о работе и увлечениях.'

if __name__ == '__main__':
    app.run()