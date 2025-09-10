import os
from dotenv import load_dotenv 
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

# --- Sub-agents ---
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

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

# --- Multi-agent (wrap sub-agents as tools) ---
multi_ai_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    team=[web_search_agent, financial_agent],
    instructions=[
        "If the user gives a company name (like NVIDIA), first use the Web Search Agent to find its stock ticker symbol.",
        "Then use the Financial Agent with that ticker to get stock data, analyst recommendations, and company news.",
        "For general non-financial information, use the Web Search Agent directly.",
        "Always include the source of the information in your response.",
        "Use tables to display the data where relevant."
    ],
    show_tools_calls=True,
    markdown=True,
)

multi_ai_agent.print_response(
    "Summarize the analyst recommendations and the latest news for Tesla",
    stream=True
)
