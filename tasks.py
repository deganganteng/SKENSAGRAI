from crewai import Agent, Task, Process, Crew
from agents import Agents


class Tasks:
    def __init__(self, event):
        self.information_note = event

    def information_task(self):
        search_task = Task(

            description = """The Information Retrieval Specialist is tasked with sourcing, filtering, and organizing relevant data from {} topics and a wide range of sources to address specific queries or challenges faced by the organization. They must ensure that the data retrieved is accurate, current, and directly applicable to the objectives at hand. The specialist will collaborate with different departments to clarify their information needs and utilize advanced retrieval systems, algorithms, and machine learning techniques to gather precise data.They are responsible for:
                            - Conducting keyword-based and semantic searches across multiple platforms, databases, and the web.
                            - Analyzing and summarizing findings to present in a coherent and structured format.
                            - Continually refining and optimizing search processes to reduce time and improve accuracy.
                            - Validating the credibility of data sources to ensure reliability.
                            - Staying updated with the latest developments in information retrieval technologies.""".format(self.information_note),
            expected_output = """A comprehensive and well-researched report that includes:
                            - Comprehensive Data Reports.
                            - Source Citations and Annotations.
                            - Search Efficiency Metrics.
                            - Recommendations.
                            - Improvement Suggestions.""", 
            agent=Agents().information_agent(), 
        )
        return search_task
