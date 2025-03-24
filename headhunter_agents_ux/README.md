# HeadhunterAgents UX

Welcome to the HeadhunterAgents UX project, powered by [crewAI](https://crewai.com). This project creates an AI-powered system to assist headhunters and recruiters in their daily tasks, leveraging multiple collaborative AI agents.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling.

1. Install UV:
```bash
pip install uv
```

2. Clone this repository and navigate to the project directory

3. Install dependencies:
```bash
uv venv
uv pip install -r requirements.txt
```

Alternatively, use the CLI command:
```bash
crewai install
```

### Configuration

1. Create a `.env` file in the root directory
2. Add your `OPENAI_API_KEY` to the `.env` file:

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/headhunter_agents_ux/config/agents.yaml` to define your agents
- Modify `src/headhunter_agents_ux/config/tasks.yaml` to define your tasks
- Modify `src/headhunter_agents_ux/crew.py` to add your own logic, tools and specific args
- Modify `src/headhunter_agents_ux/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the headhunter_agents_UX Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The headhunter_agents_UX Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the HeadhunterAgentsUx Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
