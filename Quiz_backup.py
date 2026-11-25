print("===== PYTHON QUIZ APPLICATION =====")

score = 0

questions = [
    {
        "question": "1. Which language is used in AI?",
        "options": ["a) HTML", "b) Python", "c) CSS"],
        "answer": "b"
    },
    {
        "question": "2. Which function displays output?",
        "options": ["a) print()", "b) input()", "c) scan()"],
        "answer": "a"
    },
    {
        "question": "3. Which symbol is used for comments?",
        "options": ["a) @", "b) #", "c) $"],
        "answer": "b"
    },
    {
        "question": "4. Which data type stores numbers?",
        "options": ["a) int", "b) str", "c) list"],
        "answer": "a"
    },
    {
        "question": "5. Which loop repeats code?",
        "options": ["a) if", "b) else", "c) for"],
        "answer": "c"
    }
]

for q in questions:

    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    answer = input("Enter your answer: ").lower()

    if answer == q["answer"]:
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer!")

print("\n===== QUIZ RESULT =====")
print("Your Score:", score, "/ 5")

if score >= 3:
    print("Good Job!")
else:
    print("Keep Practicing!")

input("\nPress Enter to Exit...")