from config import HF_API_KEY
import requests
from PIL import Image
import io
import os
import json
from colorama import init, Fore,Style

init (autoreset=True)

def query_hf_api(api_url,payload=None,method="post"):
    headers={"Auhtorozatiom": f"Bearer {HF_API_KEY}"}

    response= requests.post(api_url, headers=headers, json=payload) \
        if method.lower()=="post" else\
        requests.get(api_url,headers=headers,params=payload)
    if response.status_code !=200:
        raise Exception(response.text)
    return response.content

def get_basic_caption(image):
    print(Fore.YELLOW+"GENERATING BASIC CAOTIOP")

    api_url = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"

    buffer= io.BytesIO()
    image.save(buffer,format="JPEG")
    buffer.seek(0)

    headers={"Auhtorization":f"Bearer{HF_API_KEY}"}
    response=requests.post(api_url,headers= headers, data=buffer.read())
    result=response.json()

    return result[0]["generated_text"]

def generate_text (prompt,max_new_token):
    api_url = "https://api-inference.huggingface.co/models/gpt2"
    payload={"inputs": prompt,"parameters":{"max_new_tokens":max_new_token}}

    response = query_hf_api(api_url,payload)
    data=json.loads(response.decode())

    return data[0]["gnetated text"]

def truncate_text(text,limit):
    words=text.split()
    return" ".join(words[:limit])

def print_menu():
    
    print(Fore.GREEN + """
================ IMAGE TO TEXT =================
1. Caption (5 words)
2. Description (30 words)
3. Summary (50 words)
4. Exit
==============================================
""")
    
def main():
        image_path= input(Fore.BLUE +"Enter image Path:")
        if not os.path.exists(image_path):
            print(Fore.RED+"Image not found.")
            return
        image=Image.open(image_path)
        caption=get_basic_caption(image)
        print(Fore.YELLOW+ f"\nBasic Caption: {caption}\n")
        while True:
            print_menu()
            choice=input('hoose option:')

            if choice=="1":
                print(truncate_text(caption,5))
            elif choice=="2":
                text=generate_text(f'EXPAND THIS CAPTION INTO 30 WORDS:{caption}',40)
                print(truncate_text(text,30))
            elif choice=="3":
                text=generate_text(f'SUMMERIZE THIS CAPTION INTO 50 WORDS:{caption}',60)
                print(truncate_text(text,50))
            elif choice=="4":
                print("Goodbye")
                break
            else:
                print("Invalid choice")

if __name__=="__main__":
    main()







