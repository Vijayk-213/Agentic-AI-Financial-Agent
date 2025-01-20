from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.model.google import Gemini

web_search_agent = Agent(
    name="web search agent",
    roles=["search the web for the information"],
    tools=[DuckDuckGo()],model=Gemini(id="gemini-1.5-flash"),
    show_tool_calls=True
    )


financial_agent = Agent(
    name="financial ai agent",
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    model=Gemini(id="gemini-1.5-flash"),
    show_tool_calls=True,
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."],
)
multi_ai_agent = Agent(
    team=[web_search_agent, financial_agent],
    model=Gemini(id="gemini-1.5-flash"),
    instructions=["use the web search agent to find information","the financial ai agent to analyze the data"],
    show_tool_calls=True,
    markdown=True
)


multi_ai_agent.print_response("Summarize analyst recommendations and share the latest new for NVDIA", stream = True)
