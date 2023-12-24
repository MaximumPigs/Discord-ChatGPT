from openai import OpenAI
from discord import Webhook
import requests
import os

client = OpenAI(
  api_key = os.environ.get("OPENAI_API_KEY")
)

prompt = "Tell me a story about four vikings in valheim. Their names are Harrison Fjord, Aslaug, Skagi Skítráðr and Vikingman. make the story about something that has happened today, in another year. Don't introduce the story, just start telling it."

def get_ai_response(prompt):
  try:
      response = client.chat.completions.create(
          model="gpt-4",
          messages=[{"role": "user", "content": prompt}]
      )
      print(response.choices[0].message)
      return response.choices[0].message
  except Exception as e:
      print(f"Error: {e}")

def post_to_discord(message):
  try:
    hook = Webhook.from_url(os.environ.get('DISCORD_WEBHOOK_URL'))
    response = hook.send(message)
    print(response)
  except Exception as e:
    print(f"Error: {e}")

post_to_discord(get_ai_response(prompt))