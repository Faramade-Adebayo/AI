import requests
from PIL import Image 
from io import BytesIO
from config import November_22

API_URL="https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"

def generate_image_to_text(prompt:str)-> Image.Image:
    headers={"Authorization": f"Bearer{November_22}"}
    payload={"input": prompt}

    try:
        response=requests.post(API_URL,headers=headers,json=payload,timeout=30)
        response.raise_for_status()

        if 'image' in response.headers.get('Content-type',''):
            image = Image.open(BytesIO(response.content))
            return image 
        else:
            raise Exception("The response is not an image.It might be an error message.")
    except requests.exception.aRequestException as e:
        raise Exception(f"Request failed: {e}")
def main():
    """Main loop for use"""
    print("Welcome to the Tex-To-Image Generator!")
    print("Type'exit' to quit the program.\n")

    while True:
        prompt=input("Enter a description for the imaage you want to generate:\n").strip()
        if prompt.lower()== "exit":
            print("Goodbye!")
            break
            
        print("\nGenerating Image....\n")
        try:
            image=generate_image_to_text(prompt)
            image.show()

            save_option=input("Do you want to save this image ? (yes/no):").strip().lower()

            if save_option =="yes":
                file_name=input("Enter a name for the image file (without extension):").strip() or "generate_image"
                file_name="".join(c for c in file_name if c.isalnum() or c in ('_','-')).rstrip()
                image.save(f"{file_name}.png")
                print(f"Image saved as {file_name},png\n")
        except Exception as e :
            print(f"An error occurred:{e}\n")
if __name__='__main__':
        main()
        