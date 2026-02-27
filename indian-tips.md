


Cloning a popular AI project and localizing it or pivoting it to a different market is an excellent way to build your resume. It shows recruiters that you didn't just copy-paste a tutorial, but actually understand the architecture well enough to swap out data sources and tools. 

The original `stock-analysis-crew` relies on SEC filings (10-K, 10-Q), which are strictly for US companies. If you want to adapt this for the **Indian Stock Market** or **Global Markets (Forex/Crypto)** using **free** APIs, here are the best ways to do it:

---

### Option 1: Adapt for the Indian Stock Market (Highly Recommended)
Instead of SEC filings, Indian companies release Annual Reports, Quarterly Results, and Corporate Announcements to the NSE/BSE. 

**Free APIs & Data Sources you can use:**
1. **`yfinance` (Yahoo Finance Python Library):** 
   * **Why use it:** It has excellent coverage of the Indian market. You just add `.NS` for NSE or `.BO` for BSE (e.g., `RELIANCE.NS`, `TCS.NS`).
   * **Replacement for SEC:** `yfinance` provides full Income Statements, Balance Sheets, and Cash Flow statements. Instead of having your AI agent read an SEC 10-K text file, you can pass the parsed financial statement data directly to the agent.
2. **`jugaad-data` (Python Library):**
   * **Why use it:** It is a reliable, free library to scrape historical stock data and corporate announcements directly from the NSE website without getting blocked.
3. **Moneycontrol / Economic Times (News & Sentiment):**
   * **Why use it:** SEC filings often include "Management Discussion". You can replace this by hooking your agent up to a free RSS feed from Moneycontrol or using the `GoogleNews` python library filtered for Indian companies to analyze market sentiment.

### Option 2: Adapt for Forex (Global Market)
Forex doesn't have "company filings." Instead, currency prices are driven by **Macroeconomics** and **Central Bank Announcements**.

**Free APIs & Data Sources:**
1. **Alpha Vantage (Free Tier):** Excellent free API for live and historical Forex (and crypto) data.
2. **Forex Factory Economic Calendar:**
   * **Replacement for SEC:** Instead of analyzing a company, your AI agents will analyze the **Economic Calendar**. You can scrape the Forex Factory calendar (or use free APIs like *TradingEconomics* free tiers) to feed your agents data about upcoming Interest Rate Decisions, GDP reports, and Inflation (CPI) data.
3. **Federal Reserve (FRED API):** Completely free API from the US government that provides massive amounts of global economic data.

### Option 3: Adapt for Crypto (Easiest API Access)
Crypto is a favorite for developer portfolios because the APIs are modern, free, and run 24/7.

**Free APIs & Data Sources:**
1. **CoinGecko API (Free Tier) / Binance API:** Free, limitless access to price data, order books, and historical trends.
2. **Replacement for SEC Filings (Whitepapers & Commits):** 
   * Have your AI agents analyze a crypto project's **Whitepaper** (PDF parsing).
   * Hook an agent up to the **GitHub API** to analyze how active the developers are on a specific crypto project (e.g., analyzing commits for Ethereum or Solana). 

---

### How to Modify the Code (Step-by-Step)
Assuming the repo uses **CrewAI** (based on the name "crew"), you will need to swap out the tools.

**1. Remove the SEC Tool:**
In the original code, there is likely a tool fetching data from `sec-api` or `edgar`. Delete that tool.

**2. Create a `yfinance` Financial Tool (If doing Indian Stocks):**
Create a custom CrewAI tool that fetches the balance sheet and gives it to the agent:
```python
from crewai.tools import tool
import yfinance as yf

@tool("Get Company Financials")
def get_company_financials(ticker: str) -> str:
    """Fetches the latest income statement for a given Indian stock ticker (e.g., INFY.NS)."""
    stock = yf.Ticker(ticker)
    financials = stock.financials
    return financials.to_string() # Returns the data as text for the AI to read
```

**3. Change the Prompts / Roles:**
In the `agents.py` and `tasks.py` files, change the prompts.
* **Old:** *"You are an expert SEC filing analyst. Read the 10-K and find risks."*
* **New:** *"You are a Dalal Street quantitative analyst. Analyze the Income Statement and the latest Moneycontrol news for {company_name} and summarize the financial health."*

### Final Resume Tip
If you do this, rename the repo to something like **`Dalal-Street-AI-Analyst`** or **`Forex-Macro-Agent-Crew`**. 
In your resume, write: *"Cloned an AI agent architecture and completely re-engineered the data pipelines to analyze the Indian equities market using Yahoo Finance and News APIs, bypassing the need for paid SEC data."* This sounds extremely impressive to recruiters!