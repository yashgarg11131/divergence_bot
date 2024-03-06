# from tvDatafeed import Interval
# symbols_dict = {
#     'BTCUSDT.P': ("BINANCE", "BTCUSDT.P"),
#     'ETHUSDT.P': ("BINANCE", "ETHUSDT.P"),
#     'XRPUSDT.P': ("BINANCE", "XRPUSDT.P"),
#     'BNBUSDT.P': ("BINANCE", "BNBUSDT.P"),
#     'LTCUSDT.P': ("BINANCE", "LTCUSDT.P"),
#     'LINKUSDT.P': ("BINANCE", "LINKUSDT.P"),
#     'KSMUSDT.P': ("BINANCE", "KSMUSDT.P"),
#     'SOLUSDT.P': ("BINANCE", "SOLUSDT.P"),
#     'BCHUSDT.P': ("BINANCE", "BCHUSDT.P"),
#     'DOGEUSDT.P': ("BINANCE", "DOGEUSDT.P"),
#     'MATICUSDT.P': ("BINANCE", "MATICUSDT.P"),
#     'ADAUSDT.P': ("BINANCE", "ADAUSDT.P"),
#     'AVAXUSDT.P': ("BINANCE", "AVAXUSDT.P"),
#     'DOTUSDT.P': ("BINANCE", "DOTUSDT.P"),
#     'ETCUSDT.P': ("BINANCE.P", "ETCUSDT.P"),
#     'AAVEUSDT.P': ("BINANCE", "AAVEUSDT.P"),
#     'COMPUSDT.P': ("BINANCE", "COMPUSDT.P"),
#     'ATOMUSDT.P': ("BINANCE", "ATOMUSDT.P"),
#     'RUNEUSDT.P': ("BINANCE", "RUNEUSDT.P"),
#     'UNIUSDT.P': ("BINANCE", "UNIUSDT.P"),
#     'MKRUSDT.P': ("BINANCE", "MKRUSDT.P"),
#     'XLMUSDT.P': ("BINANCE", "XLMUSDT.P"),
#     'NEARUSDT.P': ("BINANCE", "NEARUSDT.P"),
#     'XMRUSDT.P': ("BINANCE", "XMRUSDT.P"),
#     'CRVUSDT.P': ("BINANCE", "CRVUSDT.P"),
#     'ZECUSDT.P': ("BINANCE", "ZECUSDT.P"),
#     'INJUSDT.P': ("BINANCE", "INJUSDT.P"),
#     'DYDXUSDT.P': ("BINANCE", "DYDXUSDT.P"),
#     'RNDRUSDT.P': ("BINANCE", "RNDRUSDT.P"),
#     'SNXUSDT.P': ("BINANCE", "SNXUSDT.P"),
#     'MANAUSDT.P': ("BINANCE", "MANAUSDT.P"),
#     'SANDUSDT.P': ("BINANCE", "SANDUSDT.P"),
#     'AXSUSDT.P': ("BINANCE", "AXSUSDT.P"),
#     'HBARUSDT.P': ("BINANCE", "HBARUSDT.P"),
#     'ALGOUSDT.P': ("BINANCE", "ALGOUSDT.P"),
#     'CHRUSDT.P': ("BINANCE", "CHRUSDT.P"),
#     'QNTUSDT.P': ("BINANCE", "QNTUSDT.P"),
#     'WOOUSDT.P': ("BINANCE", "WOOUSDT.P"),
#     'ZILUSDT.P': ("BINANCE", "ZILUSDT.P"),
#     'BATUSDT.P': ("BINANCE", "BATUSDT.P"),
#     'ENJUSDT.P': ("BINANCE", "ENJUSDT.P"),
#     'LPTUSDT.P': ("BINANCE", "LPTUSDT.P"),
#     'QTUMUSDT.P': ("BINANCE", "QTUMUSDT.P"),
#     'WAVESUSDT.P': ("BINANCE", "WAVESUSDT.P"),
#     'FETUSDT.P': ("BINANCE", "FETUSDT.P"),
#     'YFIUSDT.P': ("BINANCE", "YFIUSDT.P"),
#     'OCEANUSDT.P': ("BINANCE", "OCEANUSDT.P"),
#     'TOMOUSDT.P': ("BINANCE", "TOMOUSDT.P"),
#     'ZRXUSDT.P': ("BINANCE", "ZRXUSDT.P"),
#     'LRCUSDT.P': ("BINANCE", "LRCUSDT.P"),
#     'ONTUSDT.P': ("BINANCE", "ONTUSDT.P"),
#     'KASUSDT.P': ("BYBIT", "KASUSDT.P"),
#     'BANDUSDT.P': ("BINANCE", "BANDUSDT.P"),
#     'TRBUSDT.P': ("BINANCE", "TRBUSDT.P"),
#     'API3USDT.P': ("BINANCE", "API3USDT.P"),
#     'ONEUSDT.P': ("BINANCE", "ONEUSDT.P"),
#     'BALUSDT.P': ("BINANCE", "BALUSDT.P"),
#     'RSRUSDT.P': ("BINANCE", "RSRUSDT.P"),
#     'ICXUSDT.P': ("BINANCE", "ICXUSDT.P"),
#     'GMXUSDT.P': ("BINANCE", "GMXUSDT.P"),
#     'DASHUSDT.P': ("BINANCE", "DASHUSDT.P"),
#     'EGLDUSDT.P': ("BINANCE", "EGLDUSDT.P"),
#     'ARUSDT.P': ("BINANCE", "ARUSDT.P"),
#     'NEOBUSD.P': ("BINANCE", "NEOBUSD.P"),
#     'APTUSDT.P': ("BINANCE", "APTUSDT.P"),
#     'FILUSDT.P': ("BINANCE", "FILUSDT.P"),
#     'KAVAUSDT.P': ("BINANCE", "KAVAUSDT.P"),
#     'OPUSDT.P': ("BINANCE", "OPUSDT.P"),
#     'XTZUSDT.P': ("BINANCE", "XTZUSDT.P"),
#     'THETAUSDT.P': ("BINANCE", "THETAUSDT.P"),
#     'EOSUSDT.P': ("BINANCE", "EOSUSDT.P"),
#     'STXUSDT.P': ("BINANCE", "STXUSDT.P"),
#     'FTMUSDT.P': ("BINANCE", "FTMUSDT.P"),
#     'CHZUSDT.P': ("BINANCE", "CHZUSDT.P"),
#     'GRTUSDT.P': ("BINANCE", "GRTUSDT.P"),
#     'GALAUSDT.P': ("BINANCE", "GALAUSDT.P"),
#     'VETUSDT.P': ("BINANCE", "VETUSDT.P"),
#     'UNFIUSDT.P': ("BINANCE", "UNFIUSDT.P"),
#     'BLZUSDT.P': ("BINANCE", "BLZUSDT.P"),
#     'ROSEUSDT.P': ("BINANCE", "ROSEUSDT.P"),
#     'SUSHIUSDT.P': ("BINANCE", "SUSHIUSDT.P"),
#     'BNTUSDT.P': ("BINANCE", "BNTUSDT.P"),
#     'DEFIUSDT.P': ("BINANCE", "DEFIUSDT.P"),
#     'BTCDOMUSDT.P': ("BINANCE", "BTCDOMUSDT.P"),
#     'ZENUSDT.P': ("BINANCE", "ZENUSDT.P"),
#     'STORJUSDT.P': ("BINANCE", "STORJUSDT.P"),
#     'RLCUSDT.P': ("BINANCE", "RLCUSDT.P"),
#     '1000SHIBUSDT.P': ("BINANCE", "1000SHIBUSDT.P"),
#     'WLDUSDT.P': ("BINANCE", "WLDUSDT.P"),
#     'GALUSDT.P': ("BINANCE", "GALUSDT.P"),
#     'MTLUSDT.P': ("BINANCE", "MTLUSDT.P"),
#     'SFPUSDT.P': ("BINANCE", "SFPUSDT.p"),
#     'ALICEUSDT.P': ("BINANCE", "ALICEUSDT.P"),
#     'MAGICUSDT.P': ("BINANCE", "MAGICUSDT.P"),
#     'PERPUSDT.P': ("BINANCE", "PERPUSDT.P"),
#     'BAKEUSDT.P': ("BINANCE", "BAKEUSDT.P"),
#     'KNCUSDT.P': ("BINANCE", "KNCUSDT.P"),
#     'BELUSDT.P': ("BINANCE", "BELUSDT.P"),
#     'OMGUSDT.P': ("BINANCE", "OMGUSDT.P"),
#     'IMXUSDT.P': ("BINANCE", "IMXUSDT.P"),
#     'SXPUSDT.P': ("BINANCE", "SXPUSDT.P"),
#     'LITUSDT.P': ("BINANCE", "LITUSDT.P"),
#     'MASKUSDT.P': ("BINANCE", "MASKUSDT.P"),
# }
# columns_to_check = [
#     'Bullish Divergence',
#     'Bearish Divergence',
#     'Bullish Hidden Divergence',
#     'Bearish Hidden Divergence',
#     'Overbought',
#     'Oversold'
# ]

# interval_dict = {
#     '15 MINUTE': Interval.in_15_minute,
#     '1 HOUR': Interval.in_1_hour,
#     '4 HOUR': Interval.in_4_hour,
#     'DAILY': Interval.in_daily,
#     'WEEKLY': Interval.in_weekly,
# }

from tvDatafeed import Interval
import time
import threading
import mysql.connector
# MySQL database local  configuration
config = {
    'user': 'breakout_user',
    'password': 'Mobilo/tte56',
    'host': '3.234.60.184',
    'database': 'breakoutDB_live',
    'port': '3306', 
}
old_data = "Testing"

def fetch():
    # Establishing a connection to MySQL
    conn = mysql.connector.connect(**config)
    # Creating a cursor object to interact with the database
    cursor = conn.cursor()
    # Example query (replace 'App_cryptopair' with your table name)
    query = "SELECT * FROM App_cryptototalmarket"

    if not conn.autocommit:
        conn.autocommit = True  # This is incorrect
    # Correct way to enable autocommit:
    conn.autocommit = True
    # Executing the query
    cursor.execute(query)
    # Fetching results
    global data
    data = cursor.fetchall()
    # print("data", data)

    # Closing the cursor and connection
    cursor.close()
    conn.close()

    formatted_data = {symbol: (exchange, symbol) for _, symbol, exchange in data}
    return formatted_data
#     global symbols_dict
#     symbols_dict = formatted_data
#     global old_data
#     if old_data != formatted_data:
#         old_data = formatted_data
#         # print(formatted_data)

# fetch()

# # reterving the data in every 2 second

# def hello():
#     while True:
#         fetch()
#         time.sleep(2)

# data_refresh_thread = threading.Thread(target=hello)
# data_refresh_thread.daemon = True
# data_refresh_thread.start() 

columns_to_check = [
    'Bullish Divergence',
    'Bearish Divergence',
    'Bullish Hidden Divergence',
    'Bearish Hidden Divergence',
    'Overbought',
    'Oversold'
]
interval_dict = {
    '15 MINUTE': Interval.in_15_minute,
    '1 HOUR': Interval.in_1_hour,
    '4 HOUR': Interval.in_4_hour,
    'DAILY': Interval.in_daily,
    'WEEKLY': Interval.in_weekly,
}




