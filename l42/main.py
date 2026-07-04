from hf import generate_response
def get_essay_details():
    print("\n=== AI Writing Assistant ===\n")
    topic =input("What is the topic of the essay?").strip()
    essay_type=input("What type of essay are you writing:").strip()
    lenghts=["300 Words","900 Words","1200 Words","2000 Words"]
    print("Select essay word count:")
    for i, l in enumerate (length, 1):print(f"{1}) {l}")
    try:
        idx=int(input(">").strip())
        length=lenghts[idx - 1] if 1 <= idx <= len(lenghts) else "300 words"
    except ValueError:
        length="300 Words"
    target_audience=input("Target audience (e.g ,Hiugh School Students):").strip()
    return {"topic":topic, "essay_type": essay_type,  "lenght":length,"target_audience":target_audience}

def generate_essay_content(details):
    try:
        temp=float(input("Enter temperature(0.1 structured, 0.7 cretaive):").strip())
        if not (0.0<= temp <= 1.0): raise ValueError
    except ValueError:
        print("Ivalid temeprature.Usiong 0.3")
        temp=0.3

    intro_p = f"Write an introduction for an {details['essay_type']} essay about \
    {details['topic']} on the topic of {details['length']}."
    intro = generate_response(intro_p, temperature=temp, max_tokens=1024)
    print("\n=== Generated Introduction ===\n")
    print(intro)

    print("\nWould you like the body written as a full draft or step-by-step?")
    print("1) Full draft\n2) Step-by-step")
    choice = input("> ").strip()
    if choice == "1":
        body_p = f"Write a full body for an essay on {details['topic']} with the stance of {details['target_audience']}."
        body = generate_response(body_p, temperature=temp, max_tokens=1024)
        print("\n=== Generated Full Body ===\n")
        print(body)
    else:
        step_p = f"Write step-by-step arguments for an essay on {details['topic']}. Provide evidence and reasoning."
        body_step = generate_response(step_p, temperature=temp, max_tokens=1024)
        print("\n=== Generated Step-by-Step Body ===\n")
        print(body_step)

    concl_p = f"Write a conclusion for an {details['essay_type']} essay about {details['topic']} with the stance of {details['target_audience']}."
    concl = generate_response(concl_p, temperature=temp, max_tokens=1024)
    print("\n=== Generated Conclusion ===\n")
    print(concl)

def feedback_and_refinement():
    try:
        rating = int(input("\nRate satisfaction (1-5): ").strip())
        if rating < 1 or rating > 5: raise ValueError
    except ValueError:
        print("Invalid rating. Using 3.")
        rating = 3

    if rating != 5:
        feedback = input("Provide feedback (tone, structure, etc.): ").strip()
        print(f"\nThank you for your feedback: {feedback}")
    else:
        print("\nThank you! The essay looks good.")

def run_activity():
    print("\nWelcome to the AI Writing Assistant!")
    details = get_essay_details()
    if not details["topic"] or not details["essay_type"]:
        print("Please provide at least a topic and essay type to continue.")
        return
    generate_essay_content(details)
    feedback_and_refinement()

if __name__ == "__main__":
    run_activity()
