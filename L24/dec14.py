import requests
from colorama import Fore,Style,init

init(autoreset=True)

HF_API_KEY="YOUR_HUGGING_FACE_API_KEY"

DEFAULT_MODEL= "google\peagasus-xsum"

def buld_api_url(model_name):
    """Builds the huggung face API using model name."""
    return f"https"

def query(payload,model_name=DEFAULT_MODEL):
    """Sends aPOST request to the Hugging Fcae API"""
    api_url=buld_api_url(model_name)
    headers= {"Authorization": f"Bearer {HF_API_KEY}"}
    response = requests.post(api_url,headers=headers,json=payload)
    return response.json()

def summerize_text(text,min_length,max_length,model_name=DEFAULT_MODEL):
    """Sends text to the API  and returns the summerized text"""
    payload={"inputs":text,
             "parameters":{"min_length":min_length,
                           "max_length":max_length}}
    print(Fore.BLUE+Style.BRIGHT+ f"\n Perfoming AI summerization using model:{model_name}.....")
    results=query(payload,model_name)

    if isinstance(results,list) and len(results)> 0 and "summary_text":
        return results[0]["summary_text"]
    else:
        print(Fore.RED + "Error in summerization response:")
        print(results)
        return None
    
if __name__=="__main__":
    print(Fore.YELLOW +Style.BRIGHT +'Hi there what is your name?')

    user_name=input("Your name:").strip()

    if not user_name:
        user_name="User"

        print(Fore.GREEN+ f",Welcome ,{user_name}.;ets give your text some AI magic")
        print(Fore.YELLOW + Style.BRIGHT+"n Please enter the text you want to summerize:"   )
        user_text=input().strip()
        if not user_text=input().strip()
    if not user_text:
        print(Fore.RED+"No text provided .Exiting program.")
        exit()

    print(Fore.YELLOW+"n Enter the mdoel name you want to use ")
    print("(e.g. facebooks/bart-large.com)")
    model_choice=input("Model name(levae blank for defaults)").strip()

    if not model_choice:
        model_choice=DEFAULT_MODEL

    print(Fore.YELLOW +"n Choose your summarizaiton style:")
    print("1 Standard Summary(Quick and conscise)")
    print("2 Enhanced  Summary(Detaield)")


    style_choice=input('Enter 1 or 2 ').strip()

    if style_choice=="2":
        min_length= 80
        max_length=200
        print(Fore.BLUE + "Usinf enhanced summerization settings............")
    else:
        min_length=50
        max_length=150
        print(Fore.BLUE+ "Usind standard summerization settings -----------------")

    summary= summerize_text(
        user_text,
        min_length,
        max_length,
        model_name=model_choice
    )
    
    if summary:
        print(Fore.GREEN + Style.BRIGHT + f"\n Ai Summerizer Output for {user_name}:")
        print(Fore.GREEN + summary)
    else:
        print(Fore.RED+ "Failed to generate summary.")