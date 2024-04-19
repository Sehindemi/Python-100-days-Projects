print("The Love Calculator is calculating your score...")
name1 = input("What is your name?") # What is your name?
name2 = input("What is your lovers name?") # What is their name?

name = name1+name2
name = name.lower()

t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
first_digit = t + r + u + e

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")
second_digit = l + o + v + e

new_score = int(str(first_digit) + str(second_digit))

if (new_score < 10) or (new_score > 90):
    print(f"Your score is {new_score}, you go together like coke and mentos.")
elif (new_score >= 40) and (new_score <= 50):
    print(f"Your score is {new_score}, you are alright together.")
else:
    print(f"Your score is {new_score}.")