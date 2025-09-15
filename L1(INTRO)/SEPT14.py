print("Hello! I am AI BOT.")

name=input("What is your name?   :")
print("Nice to meet you!", name)

print("How are you feeling today ?(good/bad)  :")
mood=input().lower()

if mood=="good":
    print("I'm glad to hear that !")
elif mood=="bad":
    print("I'm sorry to hear that.Hope things get better soon.")
else:
    print("I see, Sometimes its hard to put your feeling into words.")

print(f"It was nice chatting with you {name}.Goodday!")