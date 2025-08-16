# quiz_game.py

def quiz():
    print("🎮 Welcome to the Python Quiz Game!")
    name = input("Enter your name: ")
    print(f"\nHello {name}, let's start the quiz! 🚀")

    questions = {
        "1. What is the capital of France?": "b",
        "2. Which language is used for web apps?": "c",
        "3. Who developed Python?": "a",
        "4. Which one is a fruit?": "b",
    }

    options = [
        ["a. Berlin", "b. Paris", "c. Madrid"],
        ["a. C++", "b. Java", "c. Python"],
        ["a. Guido van Rossum", "b. Elon Musk", "c. Mark Zuckerberg"],
        ["a. Potato", "b. Apple", "c. Carrot"],
    ]

    score = 0
    q_num = 0

    for q, ans in questions.items():
        print("\n" + q)
        for opt in options[q_num]:
            print(opt)

        user_ans = input("Enter your answer (a/b/c): ").lower()

        if user_ans == ans:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong!")

        q_num += 1

    print(f"\n{name}, your final score is {score}/{len(questions)} 🎉")

    if score == len(questions):
        print("🏆 Excellent! You got all answers right!")
    elif score >= 2:
        print("👍 Good job, keep practicing!")
    else:
        print("😅 Don’t worry, try again!")

if __name__ == "__main__":
    quiz()
