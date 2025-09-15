import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN}💥🕵️: Welcome to Sentiment Spy! {Style.RESET_ALL}")

user_name=input("f{Fore.MAGENTA}Please Enter your name :{Style.REST_ALL}").strip()
if not user_name:
    user_name="Mystery Agent"

conversation_history=[]