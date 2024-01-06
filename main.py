import os.path
from datetime import datetime
import json
import os
from flask import Flask, render_template, request

app = Flask (__name__)
DB_FILE_NAME = "db.json"
all_messages= []#создали пустой список для хранения сообщений

def load_messages():
    if not os.path.exists(DB_FILE_NAME) or not os.path.getsize(DB_FILE_NAME)> 0:
        return []
    with open(DB_FILE_NAME, "r") as file:
        data =json.load(file)
        return data.get("messages",[])

all_messages= load_messages()

#формат хранения сообщения
def add_message(author,text):# def -создание фнукции, внутри собки аргументы которые передаем внутрь функции, нужно добавлять табуляцию
    message = {
        'author': author , # имя
        'text': text,# текст сообщения
        'time':  datetime.now().strftime('%H:%M:%S')  # текущее время
    }
    all_messages.append(message)
    save_message()
def save_message():
    all_messages_data ={
        "messages": all_messages
    }
    with open("db.json","w") as file:
        json.dump(all_messages_data, file)

@app.route("/")
def main_page():
    return "Hello my friend"
@app.route("/chat")
def chat_page():
    return render_template("form.html")
@app.route("/get_messages")
def get_messages():
    print("Отдаем все сообщения")
    return {"messages": all_messages}

@app.route("/send_message")
def send_message():
    name = request.args.get("name")
    text = request.args.get("text")
    print(f"пользователь '{name}'   пишет   '{text}'")
    add_message(name,text)
    return "ok"

if __name__ == '__main__':
    app.run(host= '0.0.0.0',port=8080)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
