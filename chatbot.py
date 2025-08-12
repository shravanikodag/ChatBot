def chatbot_response(user_input):
    user_input=user_input.lower()
    if "hii" in user_input or "hello" in user_input or "hey" in user_input:
        return "Hello! How can i assist you today?"
    elif "how are you" in user_input:
        return "I am just a bot,your friendly chatbot."
    elif "what is your name" in user_input:
        return "I am chatbot, your bestfriend. "
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! have a nice day!"
    else:
        return "I am not sure how to response to that. "
print("PyBot: Hello! Type bye or exit when needed. ")

while True:
    user_message=input("Message: ")
    bot_reply=chatbot_response(user_message)
    print("Chatbot:",bot_reply)

    if "bye" in user_message.lower() or "exit" in user_message.lower():
        break
    
