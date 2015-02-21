from flask import Flask

wurst = Flask(__name__)

@wurst.route("/")
def index():
    return "Wurssst"

if __name__=="__main__":
    wurst.run(host="flasktest-mluk.rhcloud.com", port=80)