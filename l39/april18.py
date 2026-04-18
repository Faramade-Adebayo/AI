from april12 import generate_response

def run_activity():
    print("ZERO-SHOT, ONE-SHOT & FEW-SHOT LEARNING ACTUIVITY")

    category=input("Enter a category (eg:animal, food,city):").strip()
    item=input("Pleasefillin both fieldstorun the activity.")

    if not category or not item:
        print("Please fill in both fieldstorun the activity.")
        return
    zero_shot=f"Is {item} a {category}? Answeryes or no ."
    print("\n --- ZERO-SHOT LEARNING---")
    print(f"Response :{generate_response(zero_shot,temrature=0.3,max_tokens=1024)}")

    one_shot= f"""Example:
    Category:fruit
    Item:apple
    Answer:Yes, apple isa fruit.

    Now you try :
    Category:{category}
    Item:{item}
    Answer:"""
        print("\n --- ZERO-SHOT LEARNING---")
        print(f"Response :{generate_response(zero_shot,temperature=0.3,max_tokens=1024)}")

        few_shot= f"""Example1:
    Category:fruit
    Item:apple
    Answer:Yes, apple isa fruit.

    Now you try :
    Category:{category}
    Item:{item}
    Answer:"""
        print("\n --- FEW-SHOT LEARNING---")
        print(f"Response :{generate_response(few_shot,temperature=0.3,max_tokens=1024)}")

        creative_prompt=f"""Writeb a one sentence about the given word.
    Example 1: Word:Moon
    Story:The moon winkeed at the lovers as they shared thier first kiss.credits

    Word:{item}
    Story:"""
    print("\n ---CREATOIVE FEW-SHOT EXAMPLE")
    print(f"Response :{generate_response(creative_prompt,temperature=0.7,max_tokens=1024)}")

    
    print("\n--- REFLECTION QUESTIONS ---")
    print("1. How did the responses differ between zero-shot, one-shot, and few-shot?")
    print("2. Which approach gave the most helpful response?")
    print("3. How did the examples influence the model's output?")
if __name__=="__main__":
    run_activity()