from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def chatbot_response(user_input):
    text = user_input.lower()

    patterns = {
        r"\b(hi|hello|hey)\b": "Hello! 👋 I’m your AI chatbot. How can I help?",
        r"how are you": "I’m doing great! Thanks for asking 😊",
        r"what.*name": "I’m an NLP-based Chatbot 🤖",
        r"what.*do": "I can chat with you, answer questions, and demonstrate NLP concepts.",
        r"help": "Sure! Try asking about NLP, AI, or general questions.",
        r"\bbye|exit|quit\b": "Goodbye! 👋 Have a great day!",
    }

    for pattern, response in patterns.items():
        if re.search(pattern, text):
            return response

    return (
        "That’s interesting! 🤔 "
        "I’m still learning. Could you rephrase or ask something else?"
    )

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    reply = chatbot_response(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

