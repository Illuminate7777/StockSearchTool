import finnhub
import yfinance as yf
import time

# Initialize the Finnhub client with your API key
finnhub_client = finnhub.Client(api_key='ct4hebhr01qo7vqamo40ct4hebhr01qo7vqamo4g')  # Replace with your actual API key

def get_finnhub_data(symbol):
    data = {}
    
    # Fetch Company Profile
    try:
        profile = finnhub_client.company_profile2(symbol=symbol)
        data['Company Profile'] = profile
    except finnhub.exceptions.FinnhubAPIException as e:
        data['Company Profile'] = f"Error fetching company profile: {e}"
    time.sleep(1)
    
    # Fetch Financials Reported
    try:
        financials_reported = finnhub_client.financials_reported(symbol=symbol, freq='annual')
        data['Financials Reported'] = financials_reported
    except finnhub.exceptions.FinnhubAPIException as e:
        data['Financials Reported'] = f"Error fetching financials reported: {e}"
    time.sleep(1)
    
    # Fetch Filings
    try:
        filings = finnhub_client.filings(symbol=symbol, _from="2013-01-01", to="2023-12-31")
        data['Filings'] = filings
    except finnhub.exceptions.FinnhubAPIException as e:
        data['Filings'] = f"Error fetching filings: {e}"
    time.sleep(1)
    
    # Fetch Company Peers
    try:
        peers = finnhub_client.company_peers(symbol)
        data['Company Peers'] = peers
    except finnhub.exceptions.FinnhubAPIException as e:
        data['Company Peers'] = f"Error fetching company peers: {e}"
    time.sleep(1)
    
    # Fetch Basic Financials
    try:
        basic_financials = finnhub_client.company_basic_financials(symbol, 'all')
        data['Basic Financials'] = basic_financials
    except finnhub.exceptions.FinnhubAPIException as e:
        data['Basic Financials'] = f"Error fetching basic financials: {e}"
    time.sleep(1)
    
    # Fetch Company News
    try:
        company_news = finnhub_client.company_news(symbol, _from="2022-12-31", to="2023-12-31")
        data['Company News'] = company_news
    except finnhub.exceptions.FinnhubAPIException as e:
        data['Company News'] = f"Error fetching company news: {e}"
    time.sleep(1)
    
    # Fetch Recommendation Trends
    try:
        recommendation_trends = finnhub_client.recommendation_trends(symbol)
        data['Recommendation Trends'] = recommendation_trends
    except finnhub.exceptions.FinnhubAPIException as e:
        data['Recommendation Trends'] = f"Error fetching recommendation trends: {e}"
    time.sleep(1)
    
    # Fetch Quote
    try:
        quote = finnhub_client.quote(symbol)
        data['Quote'] = quote
    except finnhub.exceptions.FinnhubAPIException as e:
        data['Quote'] = f"Error fetching quote: {e}"
    time.sleep(1)
    
    return data

def get_yfinance_data(ticker):
    data = {}
    try:
        # Download the stock data
        stock = yf.Ticker(ticker)
        
        # Fetch basic stock information
        info = stock.info
        data['Company Name'] = info.get('longName', 'N/A')
        data['Sector'] = info.get('sector', 'N/A')
        data['Industry'] = info.get('industry', 'N/A')
        data['Market Cap'] = info.get('marketCap', 'N/A')
        data['Trailing PE'] = info.get('trailingPE', 'N/A')
        data['Forward PE'] = info.get('forwardPE', 'N/A')
        data['Price to Book'] = info.get('priceToBook', 'N/A')
        data['Profit Margins'] = info.get('profitMargins', 'N/A')
        data['Gross Margins'] = info.get('grossMargins', 'N/A')
        data['Operating Margins'] = info.get('operatingMargins', 'N/A')
        data['Return on Assets'] = info.get('returnOnAssets', 'N/A')
        data['Return on Equity'] = info.get('returnOnEquity', 'N/A')
        data['Beta'] = info.get('beta', 'N/A')
        data['Enterprise to Ebitda'] = info.get('enterpriseToEbitda', 'N/A')
        data['Total Revenue'] = info.get('totalRevenue', 'N/A')
        data['Revenue Growth'] = info.get('revenueGrowth', 'N/A')
        data['Earnings Growth'] = info.get('earningsGrowth', 'N/A')
        data['Total Debt'] = info.get('totalDebt', 'N/A')
        data['Debt to Equity'] = info.get('debtToEquity', 'N/A')
        data['Operating Cashflow'] = info.get('operatingCashflow', 'N/A')
        data['Free Cashflow'] = info.get('freeCashflow', 'N/A')
        data['Dividend Yield'] = info.get('dividendYield', 'N/A')
        data['Payout Ratio'] = info.get('payoutRatio', 'N/A')
        
        # Fetch historical data from 2013-01-01 to the latest date, with monthly intervals
        start_date = '2013-01-01'
        end_date = None  # Let yfinance use the most recent data
        historical_data = stock.history(start=start_date, end=end_date, interval='1mo')
        
        # Keep only the 'Close' price
        historical_close = historical_data['Close'].dropna()
        
        # Add historical close prices to the result
        data['Historical Close Prices'] = historical_close.to_dict()
        
    except Exception as e:
        data['Error'] = f"An error occurred with yfinance: {e}"
        
    return data

if __name__ == '__main__':
    # Replace 'AAPL' with your desired stock symbol
    symbol = 'AAPL'  # For Finnhub
    ticker = 'AAPL'  # For yfinance
    
    # Get data from Finnhub
    finnhub_data = get_finnhub_data(symbol)
    
    # Get data from yfinance
    yfinance_data_result = get_yfinance_data(ticker)
    
    # Combine data into a single output
    output = {
        'Finnhub Data': finnhub_data,
        'Yahoo Finance Data': yfinance_data_result
    }
    
    # Print the output
    print(output)
