from PIL import Image
import requests
import io
import os

HF_APT_KEY="."

def generate_caption(image):
    url = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
    headers={"Authorization":f"Bearers{HF_APT_KEY}"}

    buffer= io.BytesIO()
    image.save(buffer,format="JPEG")
    buffer.seek(0)

    response=requests.post(url,headers=headers,data=buffer.read())
    results=response.json()

    return results[0]["generated_text"]

def truncate_text(text,words):
    return "".join(text.split()[:words])

def menu():
    print("""
          1.Caption (5 words)
          2.Description(30 words)

          3.Exit
          """          )

def main():
    image_path=input("Enter image path:")

    if not os.path.exists(image_path):
        print("Image nit found")
        return
    
    image=Image.open(image_path)
    caption=generate_caption(image)

    print("\nBasic Caption", caption)

    while True:
        menu()
        choice = input("Choose option:")

        if choice=="1":
            print("Caption",truncate_text(caption,5))
        elif choice=="2":
            print("Description",truncate_text(caption,30))
        elif choice=="3":
            print("Good bye")
            break
        else:
            print("invalid choice")

main()


