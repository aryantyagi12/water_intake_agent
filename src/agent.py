import os
from dotenv import load_dotenv


from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

class waterintake:
    def __init__(self):
        self.history=[]
    def analyse_intake(self,intake):
        prompt=f"""
        You are a water intake analysis agent. The user consumes {intake} ml of water today
        provide hydration status and suggestions for the user to improve their water intake.
        """
        response=llm.invoke([SystemMessage(content="You are a helpful assistant.") ,HumanMessage(content=prompt)])
        return response.content

if __name__=="__main__":
    water_agent=waterintake()
    intake=1500
    feedback=water_agent.analyse_intake(intake)
    print(f"hydration analyse: {feedback}")




