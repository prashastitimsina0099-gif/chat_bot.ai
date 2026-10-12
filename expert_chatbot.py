
import time

print("=" * 45)
print("       EXPERT RULE-BASED CHATBOT")
print("=" * 45)
print("Welcome! I am your virtual assistant.")
print("Ask me questions and I will try to help.")
print("Type 'bye' to exit after the 2-minute demo.")
print("=" * 45)

start_time = time.time()
minimum_duration = 120  # 120 seconds = 2 minutes

while True:
    user_input = input("\nYou: ").lower().strip()
    elapsed_time = time.time() - start_time

    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        print("Bot: Hello! How can I help you today?")

    elif "your name" in user_input or "who are you" in user_input:
        print("Bot: I am Expert Chatbot, created using Python.")

    elif "how are you" in user_input:
        print("Bot: I am doing great! Thanks for asking.")

    elif "python" in user_input:
        print("Bot: Python is a popular programming language used in AI, automation, and web development.")

    elif "artificial intelligence" in user_input or "machine learning" in user_input:
        print("Bot: Artificial intelligence helps computers perform tasks that normally require human intelligence.")

    elif "chatbot" in user_input:
        print("Bot: A chatbot communicates with users using predefined rules or AI models.")

    elif "programming" in user_input or "coding" in user_input:
        print("Bot: Programming means writing instructions that computers can execute.")

    elif "date" in user_input or "time" in user_input:
        print("Bot: The current date and time is:", time.strftime("%Y-%m-%d %H:%M:%S"))

    elif "thank" in user_input:
        print("Bot: You're welcome! Happy to help.")

    elif "help" in user_input:
        print("Bot: Try asking about Python, AI, machine learning, coding, or chatbots.")

    elif "bye" in user_input or "goodbye" in user_input:
        if elapsed_time < minimum_duration:
            remaining = int(minimum_duration - elapsed_time)
            print(f"Bot: Your 2-minute demo is not finished yet.")
            print(f"Please continue testing for about {remaining} more seconds.")
        else:
            print("Bot: Goodbye! Thanks for chatting.")
            break

    elif user_input == "":
        print("Bot: Please enter a question.")

    else:
        print("Bot: I don't know that yet. Try asking about Python, AI, or coding.")

    # Display the elapsed time for the demonstration
    elapsed = int(time.time() - start_time)
    print(f"[Demo running: {elapsed // 60}m {elapsed % 60}s]")
