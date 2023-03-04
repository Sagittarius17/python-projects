import random

# Define some pre-programmed responses
greetings = ['hello', 'hi', 'hey']
questions = ['how are you', 'how are you doing', 'what\'s up']
responses = ['I\'m fine, thanks', 'I\'m doing well, how about you?', 'Not much, just chatting with you']

# Define a function to handle user input and generate responses
def respond_to_message(message):
    message = message.lower()
    
    # Check if the message is a greeting
    if message in greetings:
        return random.choice(greetings).capitalize()
    
    # Check if the message is a question
    elif message in questions:
        return random.choice(responses)
    
    # If the message doesn't match any pre-programmed responses
    else:
        return "I'm sorry, I don't understand what you're saying"

# Test the chatbot
while True:
    message = input('You: ')
    response = respond_to_message(message)
    print('Bot:', response)
