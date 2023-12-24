import openai
import requests
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

prompt = "Tell me a story about four vikings in valheim. Their names are Harrison Fjord, Aslaug, Skagi Skítráðr and Vikingman. make the story about something that has happened today, in another year. Don't introduce the story, just start telling it."

def get_ai_response(prompt):
  try:
      response = openai.Completion.create(
          engine="text-davinci-003",
          prompt=prompt,
          max_tokens=150
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