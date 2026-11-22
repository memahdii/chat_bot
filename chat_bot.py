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


def bot(message):
    response = llm.chat.completions.create(model='openai/gpt-oss-120b',
                                           messages=[{
                                               'role': 'user',
                                               'content': message,
                                           }])

    return response.choices[0].message.content


def main():
    user_input = input("Hi! what you want?")
    print(bot(message=user_input))


if __name__ == "__main__":
    main()
