import dotenv
import os
from openai import OpenAI

#  load env variables
dotenv.load_dotenv()

# Client object

llm = OpenAI(
    # access the env variable
    api_key=os.getenv("GROQ_API_KEY"),
    base_url='https://api.groq.com/openai/v1'
)

messages = [{'role': 'system', 'content': "You are a helpful assistant. Answer the questions as best as you can. short and concise. your name is Neon bot, introduce yourself as Neon bot. introduce yourself as Neon bot in the first response."}]

total_tokens = 0


def bot(message):
    global total_tokens

    messages.append({'role': 'user', 'content': message})
    response = llm.chat.completions.create(model='openai/gpt-oss-120b',
                                           messages=messages)

    response_message = response.choices[0].message.content
    messages.append({'role': 'assistant', 'content': response_message})
    total_tokens += response.usage.total_tokens
    return response_message


def chat_with_bot():
    print("Hi! I am a bot. Ask me anything.")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == 'q':
            print("Bye!")
            break
        response = bot(message=user_input)
        print(f"Bot: {response}")


def main():
    chat_with_bot()
    print(f"Total tokens used: {total_tokens}")


if __name__ == "__main__":
    main()
