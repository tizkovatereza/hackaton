#
import os
import openai
from dotenv import load_dotenv

# openai.organization = "YOUR_ORG_ID"

loaded_envs = load_dotenv()  # take environment variables from .env.
openai.api_key = os.getenv("OPENAI_API_KEY")
openai_model_list = openai.Model.list()



# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.

# print(loaded_envs)
# print(openai.api_key)
# print(openai_model_list)

prompt = "Once upon a time"
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":prompt}],
    max_tokens=50,
    )


print(response["choices"][0]["message"]["content"])



