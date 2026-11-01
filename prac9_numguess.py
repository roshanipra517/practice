print("Number Guessing Intelligent Agent")
print("Think of a number between 1 and 100.")

low = 1
high = 100

while low <= high:

    guess = (low + high) // 2

    print("\nMy guess is:", guess)
    feedback = input("Enter higher, lower or correct: ").lower()

    if feedback == "higher":
        low = guess + 1

    elif feedback == "lower":
        high = guess - 1

    elif feedback == "correct":
        print("Great! I guessed your number correctly.")
        break

    else:
        print("Invalid input! Please enter higher, lower or correct.")

else:
    print("No number found. Please check your feedback.")