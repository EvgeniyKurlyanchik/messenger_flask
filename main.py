
from flask import Flask
app = Flask (__name__)
@app.route("/")
def main_page():
    return "Hello my friend"


if __name__ == '__main__':
    app.run(host= '0.0.0.0',port=8080)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
