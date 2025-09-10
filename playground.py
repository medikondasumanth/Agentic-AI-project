import os
import phi
from dotenv import load_dotenv 
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import Playground, serve_playground_app #here fastapi is used

load_dotenv()
phi.api = os.getenv("PHI_API_KEY")


web_search_agent = Agent(
    name="Web Search Agent",
    role="A web search agent that can search the web for information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include the source of the information in your response"],
    show_tools_calls=True,
    markdown=True,
)

financial_agent = Agent(
    name="Financial Agent",
    role="A financial agent that can answer questions about financial data",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True,
        company_news=True
    )],
    instructions=[
        "Always use stock ticker symbols (like NVDA for NVIDIA, AAPL for Apple) when calling YFinanceTools.",
        "Use tables to display the data."
    ],
    show_tools_calls=True,
    markdown=True,
)


app = Playground(agents=[financial_agent, web_search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app",reload=True)