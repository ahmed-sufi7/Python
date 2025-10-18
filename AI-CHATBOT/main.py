import os
from openai import OpenAI

key= "api key"

messages = []


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=key,
)


def completion(message):
    global messages
    
    messages.append(
        {
        "role": "user",
        "content": message
        }
    )
    
    
    
    chat_completion = client.chat.completions.create(messages=messages, model= "openai/gpt-4o")

    # print(chat_completion)
    message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }
    messages.append(message)
    print(f"Jarvis: {message['content']}")


if __name__ == "__main__":
    user_question = input(f"JArvis: HI, im jarvis, How may i help you?\n")
    completion(user_question)
