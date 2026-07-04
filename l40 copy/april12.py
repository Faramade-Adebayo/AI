from hf import generate_response
import time 

def temperature_prompt_activity():
    print("="*70)
    print("ADVANCED PROMPT ENGINEERING : TEMPERARUE PLUS INSTRUCTIONS")
    print("="*70)

    print("\nPART 1:TEMPREATURE EXPLORATION")
    base= input("Enter a creative prompt:")

    for t , label in [(0.1,"LOW(0.1)- Deterministic"),
                      (0.5,"MEDIUM (0.5)- Balanced"),
                      (0.9, "HIGH (0.9)- Craetive")]:
        print(f"\n......{label}......")
        print(generate_response(base,temperature=t, max_tokens=512))
        time.sleep(1)

    print("\nPART 2:INSTRUCTION BASED PROMPT")
    topic=input ("Choose a topic (e.g, climate change , space exploration)")
    prompts=[
        f"Summarize key facts about{topic} in 3-4 sentences",
        f"Explain{topic} as if I'm a 10-year-old child .",
        f"Write a pro/con list about {topic}",
        f"Create a fictional new headline fporm 2050 about{topic}"
    ]
    for i, p in enumerate(prompts, 1):
        print(f"\n----INSTRUCTION {i}----\n{p}")
        print(generate_response(p,temperature=0.7, max_tokens=512))
        time.sleep(1)

    print("\nPARRT3: YOUR OWN INSTRUCTION PROMPT")
    custom= input("Enter yor instruction based prompt:" ).strip()
    try:
        temp=float(input("Set temeparature(0.1 to 1.0):").strip())
        if not (0.1<= temp <= 1.0):raise ValueError
    except ValueError:
        print("Invalid temperature.Uisng 0.7")
        tempt=0.7

    print("\nREFLECTION:")
    print("1) What changed when prompts became more specific?")
    print("2) What improved when context was added?")
    print("3) Which prompt felt most useful and why?")
    print("\nCHALLENGE: Create a prompt chain:")
    print("Generate content → rewrite with constraints → create a sequel (try different temps).")

def pseudo_stream(text, delay=0.013):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def bonus_stream():
    choice = input("\nBONUS: streaming-like output? (y/n): ").lower().strip()
    if choice == "y":
        p = input("Enter a prompt: ").strip()
        out = generate_response(p, temperature=0.7, max_tokens=512)
        print("\nStreaming-like response (not real streaming):")
        pseudo_stream(out)

if __name__ == "__main__":
    temperature_prompt_activity()
    bonus_stream()

