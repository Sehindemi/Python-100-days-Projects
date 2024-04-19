names = names_string.split(", ")

total_number = len(names)
random_person = random.randint(0,total_number - 1)
person = names[random_person]

print(f"{person} is going to buy the meal today!")