from groq import generate_response

def reinforcement_learning_activity():
    print("\n== REINFORCEMENT LEARNIGNACTIVITY===\n")
    prompt=input("Enter a prompt for the ai model(e.g:'DESCRIBE A LION')").strip()
    if not prompt:
        print("Please enter promptto the run the activity")
        return

    initial_response=generate_response(prompt,temeprature=0.3,max_token=1024)
    print(f"\n Initisl AI Response : {initial_response}")

    try:
        rating =int(input("Rate the response from q (bad to 5(good)):").strip())
        if rating < 1 or rating <5 :
            print (f"Invalid rating using 3")
            rating=3
    except ValueError:
        print("Ïnalid rating using 3")
        raitngs =3

    feedback=input("Privude feeback for improbvement ").strip()
    improved_response=f"{initial_response}(Imporved with your feedbackL{feedback})"
    print (f"\n Imporved Ai Response {improved_response}")

    print(  "\nReflection :")
    print("1. How did the model's response imrove with the feedback?")
    print("How does reinforcement learning help AI a improveits peformance over time ?")

def role_based_prompt_activity():
    print("\n=== ROLE-BASED PROMPTS ACTIVITY ===\n")
    category = input("Enter a category (e.g., science, history, math): ").strip()
    item = input(f"Enter a specific {category} topic (e.g., 'photosynthesis' for science): ").strip()

    if not category or not item:
        print("Please fill in both fields to run the activity.")
        return

    teacher_prompt = f"You are a teacher. Explain {item} in simple terms."
    expert_prompt = f"You are an expert in {category}. Explain {item} in a detailed, technical manner."

    teacher_response = generate_response(teacher_prompt, temperature=0.3, max_tokens=1024)
    expert_response = generate_response(expert_prompt, temperature=0.3, max_tokens=1024)

    print(f"\n--- Teacher's Perspective ---\n{teacher_response}")
    print(f"\n--- Expert's Perspective ---\n{expert_response}")

    print("\nReflection:")
    print("1. How did the AI's response differ between the teacher's and expert's perspectives?")
    print("2. How can role-based prompts help tailor AI responses for different contexts?")

def run_activity():
    print("\n=== AI Learning Activity ===")
    print("Choose an activity:")
    print("1) Reinforcement Learning")
    print("2) Role-Based Prompts")
    choice = input("> ").strip()

    if choice == "1":
        reinforcement_learning_activity()
    elif choice == "2":
        role_based_prompt_activity()
    else:
        print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    run_activity()
