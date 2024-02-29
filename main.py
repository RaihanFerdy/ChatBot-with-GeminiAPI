import google.generativeai as genai
import os
import dotenv
import platform

def generate_AI(prompt):
    # setting token and model
    dotenv.load_dotenv()
    token = os.getenv("TOKEN")
    genai.configure(api_key=token)
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(contents=[prompt])
    
    # setting OS
    system = platform.system()
    os.system("cls") if system == "Windows" else os.system("clear")
    
    # print response
    print(f"Prompt: {prompt}")
    print(f"\n{response.text}")

prompt = input("Prompt: ")
generate_AI(prompt)
