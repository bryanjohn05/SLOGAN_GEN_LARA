from openai import AzureOpenAI
import os
from prompt_library import (
    general_slogan_prompt,
    creative_slogan_prompt,
    bold_slogan_prompt
)
from dotenv import load_dotenv
load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

def generate_slogans(prompt):
    response = client.chat.completions.create(
        model="AZURE_MODEL",
        messages=[
            {"role": "system", "content": "You are a professional marketing slogan generator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=200
    )

    return response.choices[0].message.content


product_name = input("Enter product name: ")
target_audience = input("Enter target audience: ")

valid_tones = ["professional", "friendly", "bold"]
while True:
    tone = input("Enter tone (professional / friendly / bold): ").strip().lower()
    if tone in valid_tones:
        break
    print("Invalid input. Try again.")

print("\nChoose Slogan Style:")
print("1. General")
print("2. Creative")
print("3. Inovative")


choice = input("Enter choice (1/2/3): ")

if choice == "1":
    prompt = general_slogan_prompt(product_name, target_audience, tone)
elif choice == "2":
    prompt = creative_slogan_prompt(product_name, target_audience)
elif choice == "3":
    prompt = bold_slogan_prompt(product_name, target_audience)
else:
    print("Invalid choice")
    exit()

output = generate_slogans(prompt)

print("\nGenerated Marketing Slogans:\n")
print(output)
