from langchain.agents import initialize_agent, AgentType
from langchain_community.llms import GPT4All
from weather_tool import weather_tool

llm = GPT4All(
    model="./models/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    backend="llama",
    verbose=True
)

tools = [weather_tool]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True  # <-- Додано!
)
