import requests 
from config import November_22
def classify_text(text):
    API_URL=""
    headers={"Authorization": f"Bearer{November_22}"}
    payload={"inputs": text}
    response=requests.post(API_URL,header=headers,json=payload)
    return response.json()
if __name__=="__main__":
    sample_text="I love using Hugging Fcae APIS!"
    result=classify_text(sample_text)
    print(result)


