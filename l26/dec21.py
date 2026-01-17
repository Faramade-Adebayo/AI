import requests 
from PIL import Image ,ImageEnhance, ImageFilter
from io import BytesIO
from config import November_22

def generate_image_from_text(prompt):
    API_URL="https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
    headers={"Authorizaion": f"Bearers:{November_22}"}
    payload={"inputs":prompt}

    response=requests.post(API_URL,header=headers, jspon=payload)
    if response.status_code == 200:
        image=Image.open(BytesIO(response.content))
        return image
    else:
        raise Exception(f"Request failed with arus code{response.status_code}:{response.text}"
        )
def post_process_image(image):
    enhancer=ImageEnhance.Brightness(image)
    bright_image= enhancer.enhance(1.2)
    enhancer=ImageEnhance.Brightness(bright_image)
    contrast_image= enhancer.enhance(1.3)

    soft_focus_image=contrast_image.filter(ImageFilter.GaussianBlur(radius=2))
    return soft_focus_image
def main():
    print("Welcome to the Post Processing Magic Workshop!!!!!")
    print("This program will generate and image form text and applies post processing effets .")
    print("Typr 'exit' to quit.\n")

    while True:
        user_input=input("Enter a descritionfor the image (or 'exit )to quit")
        if user_input.lower()=='exit':
            print("Goodbye!")
            break
        try:
            print("\nGenerating image.......")
            image= generate_image_from_text(user_input)
            print("Applying post precessing effects ..../n")
            processed_image=post_process_image(image)
            processed_image.show()

            save_option=input("Do you want tot save the photo (yes/n): ").strip().lower()
            if save_option=="yes":
                file_name= input("Enter a name for the image file(without extension):").strip()
                processed_image.save(f"{file_name}.png")
                print(f"Image save as {file_name}.png\n")
            print("-"* 80 +"\n")
        except Exception as  e:
            print(f"An error occured:{e}\n")
if __name__=="__main__":
    main()



