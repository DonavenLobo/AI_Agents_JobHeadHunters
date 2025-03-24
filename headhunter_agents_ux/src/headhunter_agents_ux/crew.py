from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
from crewai_tools import (
    FileReadTool,
    ScrapeWebsiteTool,
    SerperDevTool,
    PDFSearchTool
)

# Initialize tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
excel_tool = FileReadTool(file_path='C:\\Users\\donav\\OneDrive\\Desktop\\Agents\\files')
read_resume = PDFSearchTool(file_path='C:\\Users\\donav\\OneDrive\\Desktop\\Agents\\files\\resume.pdf')

# Create a PDF knowledge source
pdf_source = PDFKnowledgeSource(
    file_paths=["knowledge/resume.pdf", "knowledge/aboutme.pdf"]
)

@CrewBase
class HeadhunterAgentsUx():
    """HeadhunterAgentsUx crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'


    @agent
    def manager(self) -> Agent:
        return Agent(
            config=self.agents_config['manager'],
            verbose=True,
            allow_delegation=True,
            tools=[excel_tool, read_resume],
            knowledge_sources=[pdf_source]
            # Optionally, you could add additional tools or LLM configuration here
        )
    
    @agent
    def job_scout(self) -> Agent:
        return Agent(
            config=self.agents_config['job_scout'],
            verbose=True,
            knowledge_sources=[pdf_source],
            tools=[search_tool, scrape_tool, excel_tool]
        )

    @agent
    def job_verifier(self) -> Agent:
        return Agent(
            config=self.agents_config['job_verifier'],
            knowledge_sources=[pdf_source],
            verbose=True
        )

    @agent
    def resume_tailor(self) -> Agent:
        return Agent(
            config=self.agents_config['resume_tailor'],
            verbose=True,
            knowledge_sources=[pdf_source],
            tools=[read_resume]
        )

    @agent
    def cover_letter_artisan(self) -> Agent:
        return Agent(
            config=self.agents_config['cover_letter_artisan'],
            knowledge_sources=[pdf_source],
            verbose=True
        )

    @task
    def job_listing_discovery_task(self) -> Task:
        return Task(
            config=self.tasks_config['job_listing_discovery_task'],
            output_file=r'C:\Users\donav\OneDrive\Desktop\Agents\files\jobs.csv'  # Append new job listings to the existing CSV, ensuring no duplicates
        )

    @task
    def job_analysis_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['job_analysis_strategy_task']
        )

    @task
    def resume_optimization_task(self) -> Task:
        return Task(
            config=self.tasks_config['resume_optimization_task'],
            # Output file name will dynamically incorporate details from the job listing (e.g., job title)
            output_file='./output/resume_{job_title}.md'
        )

    @task
    def cover_letter_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['cover_letter_generation_task'],
            # Output file name will be dynamically generated based on the job listing details
            output_file='./output/cover_letter_{job_title}.md'
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the HeadhunterAgentsUx crew"""
        return Crew(
            agents=self.agents,  # Automatically collected by the @agent decorator
            tasks=self.tasks,    # Automatically collected by the @task decorator
            # process=Process.sequential,
            manager_agent=self.manager,
            memory=True,
            planning=True,
            knowledge_sources=[pdf_source],
            # planning_llm="gpt-4o",
            verbose=True,
            # For hierarchical processing, uncomment the following line:
            process=Process.hierarchical,
        )

