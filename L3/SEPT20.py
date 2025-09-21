import re
import random
from colorama import Fore, init

init(autoret=True)

destinations={"Beaches":["Bali","Maldivises",'Phucket'],
              "Mountains":["Swiss Alos","Olomu Rock","Himilayas"],
              "Cities": ["Lagos","Abuja","Torono"]}

jokes=[
    "Why don't programmers like nature? Too many bugs!",

    "Why did the computer go to the doctor? Because it had a virus!",

    "Why do travelers always feel warm? Because of all their hot spots!"
]
def normalize_input(text):
    return re.sub(r"s+","", text.strip().lower())

def recommend():
    print({Fore.CYAN}+ "TravelBot Beaches , mountains , or cities?")
    preference = input (Fore.YELLOW +"You:")
    preference= normalize_input(preference)

    if preference in destination :
        suggestion= random.choice(destinition[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.GREEN + "TravelBot : Do you like it ?(Yes/No)")
        answer= input (Fore.GREEN + "You :").lower()
        if answer == "yes":
            print(Fore.GREEN +f"TravelBot: Aweosme, Enjoy!{suggestion}")
        elif answer == "no":
            print(Fore.RED +"TravelBot : Let's try another ")
            recommend()
        else :
            print(Fore.RED + "TravelBot:I'll suggets another ")
    else:
        print(Fore.RED + "TravelBot: Sorry , I dont have that type of destination")
        show_help()