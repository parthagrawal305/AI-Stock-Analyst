import yfinance as yf
from crewai.tools import tool

@tool("Get Income Statement")
def get_income_statement(ticker: str) -> str:
    """Fetches the latest income statement for a given stock ticker (e.g., AMZN, RELIANCE.NS)."""
    try:
        stock = yf.Ticker(ticker)
        financials = stock.financials
        if financials is None or financials.empty:
            return f"No income statement found for {ticker}."
        return financials.to_string()
    except Exception as e:
        return f"Error fetching income statement for {ticker}: {e}"

@tool("Get Balance Sheet")
def get_balance_sheet(ticker: str) -> str:
    """Fetches the latest balance sheet for a given stock ticker (e.g., AMZN, RELIANCE.NS)."""
    try:
        stock = yf.Ticker(ticker)
        balance_sheet = stock.balance_sheet
        if balance_sheet is None or balance_sheet.empty:
            return f"No balance sheet found for {ticker}."
        return balance_sheet.to_string()
    except Exception as e:
        return f"Error fetching balance sheet for {ticker}: {e}"

@tool("Get Stock News")
def get_stock_news(ticker: str) -> str:
    """Fetches the latest news headlines and articles for a given stock ticker."""
    try:
        stock = yf.Ticker(ticker)
        news = stock.news
        if not news:
            return f"No news found for {ticker}."
        result = []
        for article in news[:5]:
            result.append(f"Title: {article.get('title', 'N/A')}\nPublisher: {article.get('publisher', 'N/A')}\nLink: {article.get('link', 'N/A')}")
        return "\n\n".join(result)
    except Exception as e:
        return f"Error fetching news for {ticker}: {e}"
