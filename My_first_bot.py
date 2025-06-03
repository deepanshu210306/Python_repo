import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv("GROQ_API_KEY")

# Initialize client
client = Groq(api_key=api_key)

def run_chat_agent():
    print("👋 Welcome to your Groq-powered chatbot! Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye! 💫")
            break

        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model="llama3-70b-8192",
        )

        print("Bot:", response.choices[0].message.content)

# Run the chatbot
run_chat_agent()
