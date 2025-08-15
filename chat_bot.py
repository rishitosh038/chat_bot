import random
import time
from datetime import datetime

print("Hello! I'm Jarvis, your friendly assistant.")
print("Type 'bye' anytime to exit the chat.\n")


user_name = None
mood = None

greetings = ["Hi there!", "Hello! How’s your day going?", "Hey! Glad to see you!"]
how_are_you_responses = [
    "I'm doing great, thanks for asking!",
    "Feeling awesome! How about you?",
    "Just a bunch of code, but I feel fantastic!"
]
thanks_responses = [
    "You're welcome!",
    "No problem at all!",
    "Glad I could help!"
]
jokes = [
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "Why did the computer go to therapy? It had too many bytes of sadness.",
    "I told my computer I needed a break… now it won’t stop sending me Kit-Kats!"
]

while True:
    user_input = input("You: ").lower().strip()
    time.sleep(0.3)

    if user_input == "bye":
        print("Bot: Goodbye! Take care and have a wonderful day")
        break

    if user_name is None:
        print("Bot: I don't think we've met yet. What's your name?")
        user_name = input("You: ").strip()
        print(f"Bot: Nice to meet you, {user_name}!")
        continue

    if user_input in ["hi", "hello", "hey"]:
        print(f"Bot: {random.choice(greetings)} {user_name}!")
    
    elif "how are you" in user_input:
        print(f"Bot: {random.choice(how_are_you_responses)}")
        mood = input("Bot: And how are you feeling today? ").lower().strip()
        if "good" in mood or "great" in mood:
            print("Bot: That's wonderful to hear!")
        elif "not" in mood or "bad" in mood:
            print("Bot: Oh no I hope things get better soon.")
        else:
            print("Bot: Got it! Thanks for sharing.")

    elif "time" in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Bot: Right now it's {current_time}")

    elif "joke" in user_input:
        print(f"Bot: {random.choice(jokes)}")

    elif "your name" in user_input:
        print("Bot: I'm ChatBot, but you can call me your virtual buddy")
    
    elif "my name" in user_input:
        print(f"Bot: Your name is {user_name}, of course!")

    elif "thank" in user_input:
        print(f"Bot: {random.choice(thanks_responses)}")

    else:
        print("Bot: Hmm... I’m not sure I understand")
        print("Bot: You can try asking about the time, telling me to tell a joke, or just say hi!")
