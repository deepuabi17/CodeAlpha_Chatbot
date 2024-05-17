from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I assist you today?"]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot. How can I help you?"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you. How about you?"]
    ],
    [
        r"sorry (.*)",
        ["No need to apologize.", "It's alright."]
    ],
    [
        r"quit",
        ["Goodbye! Take care."]
    ],
    [
        r"(.*)",
        ["I'm here to help. Could you please provide more details?", "I'm listening. What would you like to talk about?"]
    ]
]

# Create a ChatBot instance
def chatbot():
    print("Hi, I'm ChatBot! How can I assist you today? Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input("You: ")
        response = chat.respond(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    chatbot()

