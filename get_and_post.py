from openai import OpenAI
import requests
import os

client = OpenAI(
  api_key = os.environ["OPENAI_API_KEY"]
)

prompt = "Tell me a story about four vikings in valheim. Their names are Harrison Fjord, Aslaug, Skagi Skítráðr and Vikingman. make the story about something that has happened today, in another year. Don't introduce the story, just start telling it."

def get_ai_response(prompt):
  try:
      response = client.completions.create(
          model="gpt-4",
          prompt=prompt,
      )
      return response.choices[0].text.strip()
  except Exception as e:
      print(f"Error: {e}")

def post_to_discord(message):
  try:
    headers = {
      "Content-Type": "application/json"
    }
    response = requests.post(
      url=os.environ['DISCORD_WEBHOOK_URL'],
      headers=headers,
        json=message
      )
    print(response.text)
  except Exception as e:
    print(f"Error: {e}")

post_to_discord(get_ai_response(prompt))