import os
from dotenv import load_dotenv
import streamlit as st
from streamlit.components.v1 import html
from langchain_openai import ChatOpenAI
from crewai import Process, Crew
from agents import Agents
from tasks import Tasks
from tools import file_writer_tool

load_dotenv()

def main():

    st.set_page_config(
        page_title="BIOTROP AI",
        page_icon="🌾",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("Biotrop AI 🌾")


    question = st.text_area("Hello Can I help you?:", "Write your question here")
    st.write(f"**Your Question:** {question}")

    st.markdown("### Processing...")

    openaigpt4 = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL_NAME"),
        temperature=0.2,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    information_crew = Crew(
        agents=[Agents().information_agent()],
        tasks=[Tasks(question).information_task()],
        process=Process.sequential,
        manager_llm=openaigpt4
    )
        
    results = information_crew.kickoff()
    
    st.markdown("## Results obtained:")
    st.write(f"""
        **Answer:**
        {results}
    """)

    results_str = str(results)
    runner = file_writer_tool._run(filename='example.txt', content=results_str, directory='./note', overwrite=True)
    print(runner)

    st.success("Results saved successfully!")
    st.balloons()

if __name__ == "__main__":
    main()