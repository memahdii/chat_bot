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

messages = []


def bot(message):
    messages.append({'role': 'user', 'content': message})
    response = llm.chat.completions.create(model='openai/gpt-oss-120b',
                                           messages=messages)

    response_message = response.choices[0].message.content
    messages.append({'role': 'assistant', 'content': response_message})
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


if __name__ == "__main__":
    main()
