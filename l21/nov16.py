import requests
url="https://uselessfacts.jsph.pl/random.json?language=en"

def get_random_fact():
    response =requests.get(url)

    if response.status_code==200:
        fact_data=response.json()
        print(f"Did you know?{fact_data['text']}")

    else:
        print("Failed to fetch data")
while True:

    user_input=input("Press Enter button to get a random fact")
    if user_input.lower().strip()=='q':
        print("Goodbye!")
        break
    get_random_fact()