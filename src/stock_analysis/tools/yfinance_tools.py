import yfinance as yf
from crewai.tools import tool

@tool("get_income_statement")
def get_income_statement(ticker: str) -> str:
    """Fetches the latest income statement for a given stock ticker (e.g., AMZN, RELIANCE.NS)."""
    try:
        stock = yf.Ticker(ticker)
        financials = stock.financials
        if financials is None or financials.empty:
            return f"No income statement found for {ticker}."
        # Truncate to the 2 most recent periods to save massive LLM token consumption
        return financials.iloc[:, :2].to_string()
    except Exception as e:
        return f"Error fetching income statement for {ticker}: {e}"

@tool("get_balance_sheet")
def get_balance_sheet(ticker: str) -> str:
    """Fetches the latest balance sheet for a given stock ticker (e.g., AMZN, RELIANCE.NS)."""
    try:
        stock = yf.Ticker(ticker)
        balance_sheet = stock.balance_sheet
        if balance_sheet is None or balance_sheet.empty:
            return f"No balance sheet found for {ticker}."
        # Truncate to the 2 most recent periods to save massive LLM token consumption
        return balance_sheet.iloc[:, :2].to_string()
    except Exception as e:
        return f"Error fetching balance sheet for {ticker}: {e}"

@tool("get_stock_news")
def get_stock_news(ticker: str) -> str:
    """Fetches the latest news headlines and articles for a given stock ticker."""
    try:
        stock = yf.Ticker(ticker)
        news = stock.news
        if not news:
            return f"No news found for {ticker}."
        result = []
        # Limit to 3 articles instead of 5 to save context tokens
        for article in news[:3]:
            result.append(f"Title: {article.get('title', 'N/A')}\nPublisher: {article.get('publisher', 'N/A')}\nLink: {article.get('link', 'N/A')}")
        return "\n\n".join(result)
    except Exception as e:
        return f"Error fetching news for {ticker}: {e}"
