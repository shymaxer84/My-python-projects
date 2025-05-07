from openai import OpenAI
from dotenv import load_dotenv
import os


class Agent:

    def __int__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.system_msg = "You are a helpful assistant"
        self.messages = []
        self.messages.append({"role": "system", "content": self.system_msg})

    def send_message(self,message):
        self.messages.append({"role": "user", "content": message})
        response = self.client.chat.completions.create(model="gpt-4.1", messages=self.messages)

        return response.choices[0].message.content


if __name__ == "__main__":
    agent = Agent()
    message = "Write a 50 words explanation af AI agents."
    response = agent.send_message(message)
    print(response)
