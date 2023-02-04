from flask import *
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!kkkk'


@app.route('/home')
def home():
    return 'Hello, kkkkkk!kkkk'


# @app.route("/user/add", methods=["POST"])
# def add_user():
#     print(request)
#     return user_model.savv(request)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
    # app.run(debug=True)
