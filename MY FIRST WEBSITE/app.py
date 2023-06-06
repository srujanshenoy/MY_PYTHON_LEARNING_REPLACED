from flask import Flask, render_template
from views import views

app = Flask(__name__)
app.register_blueprint(__name__, views)

if __name__ == "__main__":
    app.run(debug=True, port=8888)



