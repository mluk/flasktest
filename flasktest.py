from flask import Flask

wurst = Flask(__name__)

@wurst.route("/")
def index():
    return "Wurssst"

if __name__=="__main__":
    wurst.run(host="http://mluk.com/", port=8080)