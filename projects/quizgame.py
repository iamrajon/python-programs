"""
This is simple quiz game in python
"""

print("Welcome to Computer Science quiz game!")

playing = input("Do You want to play?(yes/no): ")

if playing.lower() != "yes":
    quit()

print("okay! let's play:)")
score = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does API stands for? ")
if answer.lower() == "application programming interface":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

print("------------------------------------------")
print(f"Your total score is: {score}")
print(f"your total percentage is: {(score/4)*100}%")
print("you got " + str(score) + " questions correct! ")

