import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN}💥🕵️: Welcome to Sentiment Spy! {Style.RESET_ALL}")

user_name=input("f{Fore.MAGENTA}Please Enter your name :{Style.REST_ALL}").strip()
if not user_name:
    user_name="Mystery Agent"

conversation_history=[]

print(f"\n{Fore.CYAN}Hello Agent {user_name}!")
print(f("Type a Sentence and I will analyze your sentences with TextBlob and show you the sentiment"))
print(f"Type {Fore.YELLOW} 'reset'{Fore.CYAN} 'History' {Fore.CYAN}." f"{Fore .YELLOW}'Exit' {Fore.CYAN}to quit )(Style.RESET_ALL \n")

while True:
    user_input= input (f"{Fore.Green}>>  (Style.RESET_ALL)").strip()

    if not user_input:
        print(f"{Fore.RED} Please enter some text or a valid command.{Style.RESET_ALL}")

    if user_input.lower() == "exit":
        print (f"\n{Fore.BLUE} Existing Sentiment Spy.Farewell, Agent {user_name} {Style.RESET_ALL} ") break
    
    elif user_input.lower == "reset":
        conversation_history.clear()
        print (f"{Fore.CYAN }")
