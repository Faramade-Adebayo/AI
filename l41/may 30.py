from groq import generate_response
def bias_mitigration_activity():
    print("\n=== BUIAS MITIGRATION ACTIVITY ===\n")
    prompt=input("Enter a prompt to exlore bias:e.g("descrbe the ideal doctor")").strip()
    if not prompt :
        print("please enter a prompt to yunnthe the acytivityu")
        return
    initial_response=generate_response(prompt,temperature=0.3,max_tokens=1024)
    print(f"\nInitila AI Respesponse :{initial_response}")

    modified_prompt=input("modify the prompt to make it to make it more neutral(e.h:Describe the qualtoied of a ghood doctor)").strip()
    if modified_prompt:
        modified_response=generate_response(modified_prompt,temperature=0.3,max_token=1024)
        print(f"\n Modified Ai Response(Neutral)":{modified_response})
    else:
        print("No mdoified proipmt entered.Skippiing neutral response")

def token_limit_axctivity():
    print("\n ===TOKEN LIMIT ACTIVITY===\n")
    long_prompt=input("Enter a long rpompt (mroe thyat 300 wordseg. a detailed sotry or describtion):").strip()

    if long_prompt:
        long_response=generate_response(long_prompt,temeprature=0.3,max_token=1024)
        preview=(long repsonser[:500]+"..." if len (long_response))
        print (f"\n response to long ptrompt :{preview}")

    else:

        print (f"\nno long propmt entref=d skipping the long propt responsse \n")
    short_prompt=input("now ,condencse the poropmt defi=ore i lesave ypou ")
    if short_prompt:
        short_response=generate_response(short_prompt,temperature=0.3,max_tokens=1024).strip()
        print(f"\n response to condensed prompt:{short_response}")
    else:
         print("no condensed prompt was entered skippingf the condensedf response")

def run_activity():
    print("\n=== AI Learning Activity ===")
    print("Choose an activity:")
    print("1) Bias Mitigation")
    print("2) Token Limits")
    choice = input("> ").strip()

    if choice == "1":
        bias_mitigation_activity()
    elif choice == "2":
        token_limit_activity()
    else:
        print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    run_activity()
      

                       
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               ")

