from flask import Flask, render_template, request
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient
from datetime import datetime
import process

app = Flask(__name__)

cluster = MongoClient("mongodb+srv://monu:monu@cluster0.srbek.mongodb.net/?retryWrites=true&w=majority")
db = cluster["shop"]
users = db["users"]
orders = db["orders"]

@app.route("/", methods=["get", "post"])

def reply():
    text = request.form.get("Body")
    numbers = request.form.get("From")
    numbers= numbers.replace("whatsapp:", "")
    response = MessagingResponse()
    # msg = response.message(f"Thanks for contacting me. you have sent '{text}' from {numbers[:-2]}")
    # msg1 = "Good Morning"
    # msg.media("https://images.unsplash.com/photo-1616879577377-ca82803b8c8c?ixlib=rb-1.2.1&raw_url=true&q=60&fm=jpg&crop=entropy&cs=tinysrgb&ixid=MnwxMjA3fDB8MHxjb2xsZWN0aW9uLXBhZ2V8MXwxMTcyNjIyfHxlbnwwfHx8fA%3D%3D&auto=format&fit=crop&w=500")
    response.message(process.chatbot_response(text))
   
    return str(response)


if __name__ == "__main__":
    app.run()
