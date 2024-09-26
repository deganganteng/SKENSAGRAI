import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from crewai import Agent


load_dotenv()

class Agents:
    def __init__(self):
        self.openaigpt4 = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.2,
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def information_agent(self):
        information = Agent(role="Information Retrieval Specialist",
                        goal="""Tujuan utama dari Information Retrieval Specialist...""",
                        backstory="""Information Retrieval Specialist selalu tertarik dengan...""",
                        verbose=True,
                        llm=self.openaigpt4
                    )
        return information
    
    