print("🤖 Welcome to AI Study Assistant!")
print("Ask me anything or type 'bye' to exit.")

while True:
    msg = input("\nYou: ").lower()

    if "hello" in msg or "hi" in msg:
        print("Bot: Hello! Ready to learn something new? 😊")

    elif "your name" in msg:
        print("Bot: I am your AI Study Assistant!")

    elif "python" in msg:
        print("Bot: Python is a simple and popular programming language.")

    elif "artificial intelligence" in msg or "what is ai" in msg:
        print("Bot: AI is the ability of machines to perform tasks that require human intelligence.")

    elif "computer" in msg:
        print("Bot: A computer is an electronic device that processes data.")

    elif "motivate" in msg or "motivation" in msg:
        print("Bot: Believe in yourself! Every expert was once a beginner. 🌟")

    elif "joke" in msg:
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs! 😂")

    elif "thank" in msg:
        print("Bot: You're welcome! Happy learning!")

    elif "bye" in msg:
        print("Bot: Goodbye! Keep learning and keep growing! 👋")
        break

    else:
        print("Bot: Sorry, I don't know that yet. Ask me something else!")