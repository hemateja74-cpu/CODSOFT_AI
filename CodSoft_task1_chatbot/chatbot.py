import re

# Define rules as patterns and responses
rules = {
    r"(hello|hi|hey)": "Hello! 👋 How can I help you today?",
    r"(how are you|how's it going)": "I'm doing great, thanks for asking! 😊",
    r"(your name|who are you)": "I'm CODSOFT Chatbot 🤖, here to assist you.",
    r"(bye|exit|quit)": "Goodbye! 👋 Have a nice day!",
    r"(help|support)": "Sure! I can answer greetings, tell my name, or say goodbye.",
    r"(time|date)": "I don’t have a clock yet ⏰, but you can check your system time."
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    for pattern, response in rules.items():
        if re.search(pattern, user_input):
            return response
    return "Sorry, I don't understand that yet. 🙈"

# Main loop
print("CODSOFT Chatbot (Advanced) is ready! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot:", response)
    if re.search(r"(bye|exit|quit)", user_input.lower()):
        break
