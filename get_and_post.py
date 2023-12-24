from openai import OpenAI
import requests
import os

client = OpenAI(
  api_key = os.environ.get("OPENAI_API_KEY")
)

role = "You are an author of childrens stories"
prompt = "Tell me a story about four vikings in valheim. Their names are Harrison Fjord, Aslaug, Skagi Skítráðr and Vikingman. make the story about something that has happened today, in another year. Don't introduce the story, just start telling it."

def get_ai_response(role, prompt):
  try:
      response = client.completions.create(
          model="curie",
          messages=[
             {"role": "system", "content": role},
             {"role": "user", "content": prompt}
          ]
      )
      return response.choices[0].message.strip()
  except Exception as e:
      print(f"Error: {e}")

def post_to_discord(message):
  try:
    headers = {
      "Content-Type": "application/json"
    }
    response = requests.post(
      url=os.environ.get('DISCORD_WEBHOOK_URL'),
      headers=headers,
        json=message
      )
    print(response.text)
  except Exception as e:
    print(f"Error: {e}")

post_to_discord(get_ai_response(role,prompt))