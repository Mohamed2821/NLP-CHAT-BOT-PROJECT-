
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm doing great!", "All good!", "Feeling smart today!"],
    "bye": ["Goodbye!", "See you soon!", "Take care!"],
    "default": ["Sorry, I didn't understand that.", "Can you rephrase?", "Interesting! Tell me more."]
}

def chatbot_reply(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    reply = chatbot_reply(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
