questions = [
    ["Who is Shah Rukh Khan? ", "WWE Wrestler", "Actor", "Plumber", "Singer", 2],
    ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Lisbon", 3],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Saturn", 2],
    ["Who wrote 'Romeo and Juliet'?", "Mark Twain", "Charles Dickens", "William Shakespeare", "Jane Austen", 3],
    ["What is the largest mammal in the world?", "Elephant", "Blue Whale", "Giraffe", "Great White Shark", 2]
]
i=0
prices = [100, 200, 300, 400, 500]
for i, question in enumerate(questions):
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    a = int(input("Your answer. 1 for a, 2 for b, 3 for c, 4 for d: "))

    if a == question[5]:
        print("Correct!")
    else:
        print("Wrong!")
        print(f"the correct answer is {question[5]}")
        break
    print(f"YOU WON {prices[i]}")
    i += 1