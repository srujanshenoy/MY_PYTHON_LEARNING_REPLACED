from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Home Page! No Info"
@app.route('/<user_name>')
def great(username):

    user_data = {
        "age": "",
        "name": "",
        "id": ""
    }

    age = request.args.get('age')
    name = request.args.get('name')
    id = request.args.get('id')

    # if age:
        # user_data["age"] = age

    user_data["age"] = age if age else user_data["age"] = "??"
    user_data["name"] = name if name else user_data["name"] = "??"
    user_data["id"] = id if id else user_data["id"] = "??"
    if id:
        user_data["id"] = id

    return f"hello {username}! your age is {age} and your name is {name}"

if __name__ == "__main__":
    app.run(debug=True)