print("Hello dear player")

playing = input("Do you want to play a quiz game? ")

if playing.lower() != "yes":
    print("Alright then...")
    quit()

print("Good! Let's play!")
score = 0

answer = input(
    "A cross between a horse and a zebra is called a 'Hobra' | True or False? ")
if answer.lower() == "false":
    print("Correct! ")
    score += 1
    print("A male zebra and a female horse is called a 'zorse', and a female zebra and a male horse is called a 'zonkey' ")
else:
    print("Wrong! ")
    print("A male zebra and a female horse is called a 'zorse', and a female zebra and a male horse is called a 'zonkey' ")

answer = input("The black box in a plane is black | True or False? ")
if answer.lower() == "false":
    print("Correct! ")
    score += 1
    print("They're actually orange ")
else:
    print("Wrong! ")
    print("They're actually orange ")

answer = input(
    "The star sign Aquarius is represented by a tiger | True or False? ")
if answer.lower() == "true":
    print("Correct! ")
    score += 1
    print("-.- ")
else:
    print("Wrong! ")
    print("Y U NO UNDERSTAND ASIAN?? ")

answer = input("Marrakesh is the capital of Morocco | True or False? ")
if answer.lower() == "false":
    print("Correct! ")
    score += 1
    print("It's Rabat! ")
else:
    print("Wrong! ")
    print("It's Rabat! ")

answer = input("M&M stands for Mars and Moordale | True or False? ")
if answer.lower() == "false":
    print("Correct! ")
    score += 1
    print("M&M stands for Mars and Murrie ")
else:
    print("Wrong! ")
    print("M&M stands for Mars and Murrie ")

answer = input("Monaco is the smallest country in the world | True or False? ")
if answer.lower() == "false":
    print("Correct! ")
    score += 1
    print("Vatican City is, with only 0.44 sq.km ")
else:
    print("Wrong! ")
    print("Vatican City is, with only 0.44 sq.km ")

answer = input("Australia is wider than the moon | True or False? ")
if answer.lower() == "true":
    print("Correct! ")
    score += 1
    print("The moon sits at 3400km in diameter, while Australia's diameter from east to west is almost 4000km ")
else:
    print("Wrong! ")
    print("The moon sits at 3400km in diameter, while Australia's diameter from east to west is almost 4000km ")

answer = input("Coffee is made from berries | True or False? ")
if answer.lower() == "true":
    print("Correct! ")
    score += 1
    print("When coffee berries turn from green to bright red in colour, this indicaties ripeness and they are picked, processed, and dried, before being roasted and turned into coffee ")
else:
    print("Wrong! ")
    print("When coffee berries turn from green to bright red in colour, this indicaties ripeness and they are picked, processed, and dried, before being roasted and turned into coffee ")

answer = input("An octopus has three hearts | True or False? ")
if answer.lower() == "true":
    print("Correct! ")
    score += 1
    print("An octopus has one main, systemic heart to pumps blood around its body. The two additional hearts are responsible for pumping blood over each of its gills ")
else:
    print("Wrong! ")
    print("An octopus has one main, systemic heart to pumps blood around its body. The two additional hearts are responsible for pumping blood over each of its gills ")

answer = input(
    "In the English language there is no word that rhymes with orange | True or False? ")
if answer.lower() == "true":
    print("Correct! ")
    score += 1
    print("Eminem might think that there are words that rhyme with orange but, he is wrong ")
else:
    print("Wrong! ")
    print("Eminem might think that there are words that rhyme with orange but, he is wrong ")

print("You got " + str(score) + " questions correct! ")
print("You got " + str((score / 10) * 100) + "% ")
