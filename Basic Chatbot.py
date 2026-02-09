def simple_chatbot():
    print("Chatbot: Hello! I am a basic bot. (Type 'bye' to exit)")
    
    while True:
        # 1. Get user input and convert to lowercase for easy matching
        user_input = input("You: ").lower().strip()
        
        # 2. Rule-based responses using if-elif-else
        if user_input == "hello" or user_input == "hi":
            print("Chatbot: Hi there! How can I help you?")
            
        elif user_input == "how are you" or user_input == "how are you?":
            print("Chatbot: I'm just a script, but I'm functioning perfectly! Thanks!")
            
        elif "name" in user_input:
            print("Chatbot: I don't have a name, I'm just Task 4.")
            
        elif user_input == "bye" or user_input == "goodbye":
            print("Chatbot: Goodbye! Have a nice day.")
            break # Exit the loop
            
        else:
            print("Chatbot: I'm sorry, I don't understand that command yet.")

if __name__ == "__main__":
    simple_chatbot()