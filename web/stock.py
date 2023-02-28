
import yfinance as yf

# shopify = yf.Ticker("SHOP")
# shopify_data = shopify.history(period="min")
# shopify_data.reset_index(inplace=True)
# shopify_data.head()
# print(shopify_data)

Tesla = yf.Ticker("TSLA")
tesla_data = Tesla.history(period = "max")
tesla_data.reset_index(inplace = True)

tesla_data.head()

print(tesla_data.head())

# import yfinance as yf
#
# data = yf.download(tickers="TSLA", period="1y")
# print(data)
#
# import pandas as pd
# df_data = pd.DataFrame(data)
# print(df_data.describe())
#
# import matplotlib.pyplot as plt
# plt.plot(df_data['Close'], label="Close")
# plt.legend()
# plt.show()
