import sys
import os
import yfinance as yf
sys.path.append(os.path.join(os.getcwd(), 'src', 'stock_analysis'))
from crew import StockAnalysisCrew

inputs = {
    'query': 'Analyze AMZN',
    'company_stock': 'AMZN',
}
print("Starting Kickoff...")
crew = StockAnalysisCrew().crew()
result = crew.kickoff(inputs=inputs)
print("SUCCESS!")
print(result)
