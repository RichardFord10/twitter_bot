
import keys
import openai

openai.api_key = keys.openai

class ChatGpt: 

  def __init__(self):
    pass


  def prompt(self, chat_prompt):
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=chat_prompt,
    temperature=0.5,
    max_tokens=256,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0)
    
    return(response['choices'][0]['text'])






