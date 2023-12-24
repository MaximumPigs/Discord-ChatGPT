from openai import OpenAI
from discord import SyncWebhook
import os

client = OpenAI(
  api_key = os.environ.get("OPENAI_API_KEY")
)

prompt = "Just say Hi"
#prompt = "Tell me a story in less than 200 words about four vikings in valheim. Their names are Harrison Fjord, Aslaug, Skagi Skítráðr and Vikingman. make the story about something that has happened today, in another year. Don't introduce the story, just start telling it."

def get_ai_response(prompt):
  try:
      response = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[{"role": "user", "content": prompt}]
      )
      print(response.choices[0].message.content)
      return response.choices[0].message.content
  except Exception as e:
      print(f"Error: {e}")

def post_to_discord(message):
  try:
    hook = SyncWebhook.from_url(os.environ.get('DISCORD_WEBHOOK_URL'))
    response = hook.send(message)
    print(response)
  except Exception as e:
    print(f"Error: {e}")

post_to_discord(get_ai_response(prompt))