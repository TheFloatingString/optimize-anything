import os

from colorama import Back, Fore, Style
from dotenv import load_dotenv
from openai import OpenAI
from swarm import Agent, Swarm

load_dotenv()

client = Swarm(OpenAI(api_key=os.getenv("OPENAI_API_KEY")))


def solve_latex_code():
    print(Style.DIM + "solving latex code!")
    print(Style.RESET_ALL)

    return agent_b


def rewrite_text_as_optimization_statement():
    print(Style.DIM + "rewrite_text_as_optimization_statement")
    print(Style.RESET_ALL)

    return agent_c


def rewrite_optimization_statement_as_latex():
    print(Style.DIM + "rewrite_optimization_statement_as_latex")
    print(Style.RESET_ALL)

    return agent_d


def rewrite_latex_code_and_substitute_missing_data():
    print(Style.DIM + "rewrite_latex_code_and_substitute_missing_data")
    print(Style.RESET_ALL)

    return agent_e


user_resp = input("Hot take, rant or comment: ")

agent_a = Agent(
    name="Agent A",
    instructions="You are a helpful agent",
    functions=[
        solve_latex_code,
        rewrite_text_as_optimization_statement,
        rewrite_optimization_statement_as_latex,
        rewrite_latex_code_and_substitute_missing_data,
    ],
)

agent_b = Agent(
    name="Agent B",
    instructions="Solve latex and state the answer as a decimal",
)

agent_c = Agent(
    name="Agent C",
    instructions="Rewrite prompt as an optimization statement",
)

agent_d = Agent(
    name="Agent D",
    instructions="Rewrite optimization statement as system of equations in latex with minimization statement and make sure all variables have a numerical value. Do not return explanations, just latex equations.",
)

agent_e = Agent(
    name="Agent E",
    instructions="Rewrite the optimization statement and replace all unknown variables with estimates for numerical values",
)


response = client.run(
    agent=agent_a,
    messages=[
        {
            "role": "user",
            "content": f"Rewrite as an optimizaiton statement: {user_resp}",
        }
    ],
)

print("---")
print(Fore.YELLOW + response.messages[-1]["content"])
print(Style.RESET_ALL)


for i in range(100):
    response = client.run(
        agent=agent_a,
        messages=[
            {
                "role": "user",
                "content": response.messages[-1]["content"],
            }
        ],
    )

    print(Fore.YELLOW + response.messages[-1]["content"])
    print(Style.RESET_ALL)
