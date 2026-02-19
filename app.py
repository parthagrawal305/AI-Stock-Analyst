import streamlit as st
import sys
import os
from dotenv import load_dotenv

load_dotenv()

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src", "stock_analysis"))
from crew import StockAnalysisCrew

st.set_page_config(page_title="Autonomous Stock Analysis", page_icon="📈", layout="wide")

st.title("📈 Autonomous Stock Analysis (CrewAI)")
st.markdown("""
Welcome to the AI Boardroom. This tool deploys three specialized AI agents to analyze a given stock:
*   **Research Analyst:** Scours recent news and market sentiment.
*   **Financial Analyst:** Analyzes income statements and balance sheets.
*   **Investment Advisor:** Synthesizes qualitative and quantitative data to make a recommendation.
""")

st.info("💡 **Pro Tip**: Works for US Stocks (`AMZN`, `AAPL`) and Indian Stocks (`RELIANCE.NS`, `INFY.NS`).", icon="ℹ️")

ticker = st.text_input("Enter Ticker Symbol", value="RELIANCE.NS")

if st.button("Start Analysis"):
    if ticker:
        if not os.environ.get("GROQ_API_KEY"):
            st.error("Missing GROQ_API_KEY. Please set it in your environment.")
        else:
            with st.status(f"🤖 Agents are analyzing {ticker}...", expanded=True) as status:
                st.write("Initializing agents...")
                inputs = {
                    'query': f'Analyze the financial health and provide an investment recommendation for {ticker}.',
                    'company_stock': ticker,
                }
                
                try:
                    result = StockAnalysisCrew().crew().kickoff(inputs=inputs)
                    status.update(label="Analysis Complete!", state="complete", expanded=False)
                    
                    st.success(f"Final Report for {ticker} Generated Successfully!")
                    st.markdown("---")
                    st.markdown("### 📊 Consolidated Investment Report")
                    
                    # Depending on Crew output, it could be a string or an object with raw property
                    if hasattr(result, "raw"):
                         st.markdown(result.raw)
                    else:
                         st.markdown(result)
                            
                except Exception as e:
                    status.update(label="Analysis Failed", state="error")
                    st.error(f"An error occurred during analysis: {str(e)}")
                    st.exception(e)
    else:
        st.warning("Please enter a valid ticker symbol.")
