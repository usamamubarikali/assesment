import openai
import os
import json


class GPTPrompt:
    def __init__(self, country: str, season: str) -> None:
        self.country: str = country
        self.season: str = season
        self.__gpt_message: list = []

    def __set_initial_prompt(self) -> None:
        self.__gpt_message.extend([
            {
                "role": "user",
                "content": f"Tell me three things I can do in {self.country} at {self.season} season."
            },
        ])

    def __set_response_prompts(self) -> None:
        self.__gpt_message.extend([
            {
                "role": "user",
                "content": """Your final output should be formatted as below. Double check to ensure that there is nothing added before or after the main json object.
                    {
                        recommendations: []
                    }
                """
            },
        ])

    def get_gpt_prompts(self) -> list:
        self.__set_initial_prompt()
        self.__set_response_prompts()
        return self.__gpt_message


def get_recommendations(country: str, season: str):
    prompts = GPTPrompt(country=country, season=season).get_gpt_prompts()
    
    openai.api_key = os.getenv('OPENAI_API_KEY')
    completion =openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=prompts,
        temperature=0.2
    )
    response = json.loads(completion.choices[0].message.content)
    return response["recommendations"]

