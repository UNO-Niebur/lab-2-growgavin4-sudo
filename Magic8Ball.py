# Magic8Ball.py
# Name: Gavin Grow
# Date: 2/1/26
# Assignment: Magic 8 Ball

import random

def main():
    answers = [
        "It is decidedly so",
        "It is certain",
        "Without a doubt",
        "Yes definitely",
        "You may rely on it",
        "As I see it, yes",
        "Most likely",
        "Outlook good",
        "Yes",
        "Signs point to yes",
        "Reply hazy, try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful"
    ]

    print("Magic 8 Ball")
    while True:
        question = input("What is your question? (or type 'quit' to exit): ").strip()
        if not question:
            print("Please type a question or 'quit' to exit.")
            continue
        if question.lower() == "quit":
            break

        response = random.choice(answers)
        print(f"You asked: {question}")
        print(f"Magic 8 Ball says: {response}\n")

    input("Press Enter to exit...")

if __name__ == '__main__':
    main()
