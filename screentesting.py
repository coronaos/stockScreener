import json
import yfinance as yf
from datetime import datetime, timedelta



# Función para obtener datos históricos de una acción desde Alpha Vantage
def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    #hist = stock.history(period="5d")  # Fetch the last week's data
    end_date = datetime.today()
    start_date = end_date - timedelta(days=end_date.weekday() + 7)  # Start from the Monday of last week
    finalle_date = end_date - timedelta(days=end_date.weekday() + 2)
    start_date_str = start_date.strftime('%Y-%m-%d')
    #print(start_date_str)
    end_date_str = finalle_date.strftime('%Y-%m-%d')
    #print(end_date_str)
    hist = stock.history(start=start_date_str, end=end_date_str)
    #print(hist["Close"])
    # Extract the specific column data
    if "Close" in hist.columns:
        close_prices = hist["Close"]

        # Get the last close price
        last_close_date = close_prices.index[-1]
        last_close_price = close_prices.iloc[-1]

        # Format the result as a JSON string
        result = {str(last_close_date): last_close_price}
        closingPriceWeek = json.dumps(result, indent=2)

    if "Open" in hist.columns:
        open_prices = hist["Open"]

        # Get the first open price
        # last_close_date = close_prices.index[-1]
        first_open_date = open_prices.index[0]
        first_open_price = open_prices.iloc[0]

        # Format the result as a JSON string
        result = {str(first_open_date): first_open_price}
        openingPriceWeek = json.dumps(result, indent=2)

    #openingPriceWeekS = str(openingPriceWeek)
    #closingPr(iceWeekS = str(closingPriceWeek)
    #print(last_close_price)
    #print(first_open_price)
    percent = ((last_close_price*100)/first_open_price)-100
    #print(percent)
    #print("DATOS OBTENIDOS")
    if(percent <= -5):
        print(symbol, percent) #COMPRAR 5 DOLARES DE CADA ACCION

    return 0


# Filtrar las acciones según los criterios y mostrar los resultados
#filtered_stocks = filter_stocks(sp500_tickers, api_key)
tickers = ["MMM", "ABT", "ABBV", "ACN", "ADBE", "AMD", "AAP", "AES",
    "AFL", "A", "APD", "AKAM", "ALK", "ALB", "ARE", "ALGN", "ALLE",
    "LNT", "ALL", "GOOGL", "GOOG", "MO", "AMZN", "AMCR", "AEE", "AAL", "AEP",
    "AXP", "AIG", "AMT", "AWK", "AMP", "AME", "AMGN", "APH", "ADI", "ANSS",
    "AON", "AOS", "APA", "AAPL", "AMAT", "APTV", "ADM", "ANET", "AJG",
    "AIZ", "T", "ATO", "ADSK", "ADP", "AZO", "AVB", "AVY", "BKR", "BAC",
    "BK", "BAX", "BDX", "BBY", "BIO", "BIIB", "BLK", "BA", "BKNG", "BWA",
    "BXP", "BSX", "BMY", "AVGO", "BR", "CHRW", "CDNS", "CZR", "CPB",
    "COF", "CAH", "KMX", "CCL", "CARR", "CTLT", "CAT", "CBOE", "CBRE", "CDW", "CE",
    "CNC", "CNP", "CF", "SCHW", "CHTR", "CVX", "CMG", "CB", "CHD", "CI",
    "CINF", "CTAS", "CSCO", "C", "CFG", "CLX", "CME", "CMS", "KO", "CTSH",
    "CL", "CMCSA", "CMA", "CAG", "COP", "ED", "STZ", "COO", "CPRT", "GLW",
    "CTVA", "COST", "CCI", "CSX", "CMI", "CVS", "DHI", "DHR", "DRI", "DVA", "DE",
    "DAL", "XRAY", "DVN", "DXCM", "FANG", "DLR", "DFS",
    "DG", "DLTR", "D", "DPZ", "DOV", "DOW", "DTE", "DUK", "DD", "DXC", "EMN",
    "ETN", "EBAY", "ECL", "EIX", "EW", "EA", "EMR", "ENPH", "ETR", "EOG", "EFX",
    "EQIX", "EQR", "ESS", "EL", "ETSY", "EVRG", "ES", "EXC", "EXPE", "EXPD",
    "EXR", "XOM", "FFIV", "FAST", "FRT", "FDX", "FIS", "FITB", "FE",
    "EXR", "XOM", "FFIV", "FAST", "FRT", "FDX", "FIS", "FITB", "FE",
    "FISV", "FLS", "FMC", "F", "FTNT", "FTV", "FOXA", "FOX",
    "BEN", "FCX", "GPS", "GRMN", "IT", "GD", "GE", "GIS", "GM", "GPC", "GILD",
    "GL", "GPN", "GS", "GWW", "HAL", "HBI", "HIG", "HAS", "HCA", "HSIC",
    "HSY", "HES", "HPE", "HLT", "HOLX", "HD", "HON", "HRL", "HST", "HWM",
    "HPQ", "HUM", "HBAN", "HII", "IEX", "IDXX", "ITW", "ILMN", "INCY",
    "IR", "INTC", "ICE", "IBM", "IP", "IPG", "IFF", "INTU", "ISRG", "IVZ", "IPGP",
    "IQV", "IRM", "JKHY", "J", "JBHT", "SJM", "JNJ", "JCI", "JPM", "JNPR",
    "K", "KEY", "KEYS", "KMB", "KIM", "KMI", "KLAC", "KHC", "KR", "LB", "LHX",
    "LH", "LRCX", "LW", "LVS", "LEG", "LDOS", "LEN", "LLY", "LNC", "LIN", "LYV",
    "LKQ", "LMT", "L", "LOW", "LUMN", "LYB", "MTB", "MRO", "MPC", "MKTX", "MAR",
    "MMC", "MLM", "MAS", "MA", "MKC", "MCD", "MCK", "MDT", "MRK", "MET",
    "MTD", "MGM", "MCHP", "MU", "MSFT", "MAA", "MHK", "TAP", "MDLZ", "MPWR",
    "MNST", "MCO", "MS", "MOS", "MSI", "MSCI", "NDAQ", "NTAP", "NFLX", "NWL",
    "NEM", "NWSA", "NWS", "NEE", "NKE", "NI", "NSC", "NTRS", "NOC",
    "NCLH", "NOV", "NRG", "NUE", "NVDA", "NVR", "ORLY", "OXY", "ODFL",
    "OMC", "OKE", "ORCL", "OTIS", "PCAR", "PKG", "PH", "PAYX", "PAYC", "PYPL",
    "PENN", "PNR", "PEP", "PRGO", "PFE", "PM", "PSX", "PNW",
    "PNC", "POOL", "PPG", "PPL", "PFG", "PG", "PGR", "PLD", "PRU", "PTC", "PEG",
    "PSA", "PHM", "PVH", "QRVO", "PWR", "QCOM", "DGX", "RL", "RJF", "RTX", "O",
    "REG", "REGN", "RF", "RSG", "RMD", "RHI", "ROK", "ROL", "ROP", "ROST", "RCL",
    "SPGI", "CRM", "SBAC", "SLB", "STX", "SEE", "SRE", "NOW", "SHW", "SPG",
    "SWKS", "SNA", "SO", "LUV", "SWK", "SBUX", "STT", "STE", "SYK", "SYF",
    "SNPS", "SYY", "TMUS", "TROW", "TTWO", "TPR", "TGT", "TEL", "TDY", "TFX",
    "TER", "TSLA", "TXN", "TXT", "TMO", "TJX", "TSCO", "TT", "TDG", "TRV", "TRMB",
    "TFC", "TYL", "TSN", "UDR", "ULTA", "USB", "UAA", "UA", "UNP", "UAL",
    "UNH", "UPS", "URI", "UHS", "UNM", "VFC", "VLO", "VTR", "VRSN",
    "VRSK", "VZ", "VRTX", "V", "VNT", "VNO", "VMC", "WRB", "WAB", "WMT",
    "WBA", "DIS", "WM", "WAT", "WEC", "WFC", "WELL", "WST", "WDC", "WU",
    "WY", "WHR", "WMB", "WYNN", "XEL", "XRX", "XYL", "YUM",
    "ZBRA", "ZBH", "ZION", "ZTS"]
print("DATOS PRINTEADOS:")
for name in tickers:
    get_stock_data(name)
