from flask import Flask, render_template, request, jsonify
import util

app = Flask(__name__, template_folder='templates')

@app.route('/')
def hello():
    return render_template("index.html")

@app.route("/get_response", methods=['GET', 'POST'])
def get_response():
    user_message = request.form['userMessage']

    print(user_message)

    response = jsonify({
        "bot_msg" : util.generate_answer(user_message)
    })
    response.headers.add("Access-control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    app.run(debug=True)