"""
A POC file to prove the validity of the OPENAI_API_KEY.
This is a direct request from OpenAI and has nothing to do with CrewAI.
"""
import openai
import os
from dotenv import load_dotenv, find_dotenv

def load_env():
    _ = load_dotenv(find_dotenv())

def get_openai_api_key():
    # load .env file
    load_env()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return openai_api_key

client = openai.OpenAI(api_key=get_openai_api_key())

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"user","content":"What is the difference between an Apple and an Orange?"}
    ]
)

print(response.choices[0].message.content)
