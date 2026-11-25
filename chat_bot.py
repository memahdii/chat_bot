import dotenv
import os
from openai import OpenAI

#  load env variables
dotenv.load_dotenv()


class ChatBot:
    def __init__(self):
        # Client object
        self.llm = OpenAI(
            # access the env variable
            api_key=os.getenv("GROQ_API_KEY"),
            base_url='https://api.groq.com/openai/v1'
        )

        self.messages = [{'role': 'system', 'content': "You are a helpful assistant. Answer the questions as best as you can. short and concise. your name is Neon bot, introduce yourself as Neon bot. introduce yourself as Neon bot in the first response."}]

        self.total_tokens = 0

    def bot(self, message):
        self.messages.append({'role': 'user', 'content': message})
        response = self.llm.chat.completions.create(model='openai/gpt-oss-120b',
                                                    messages=self.messages)

        response_message = response.choices[0].message.content
        self.messages.append(
            {'role': 'assistant', 'content': response_message})
        self.total_tokens += response.usage.total_tokens
        return response_message

    def chat_with_bot(self):
        print("Hi! I am a bot. Ask me anything.")
        while True:
            user_input = input("You: ").strip().lower()
            if user_input == 'q':
                print("Bye!")
                break
            response = self.bot(message=user_input)
            print(f"Bot: {response}")

    # Observability
    def report(self):
        for message in self.messages:
            print(message)
        print(f"Total tokens used: {self.total_tokens}")


def main():
    bot = ChatBot()
    bot.chat_with_bot()
    bot.report()


if __name__ == "__main__":
    main()
