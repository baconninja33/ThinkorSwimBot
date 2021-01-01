#this bot will connect to the alpaca_trade_api as trade api
#this is using paper wallet

#import alpaca_trade_api as tradeapi
import requests
from config import *
BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)

r = requests.get(account_url, headers={'APCA-API-KEY-ID':API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY})

print(r.content)

#class Martingale(object):
   #def __init__(self):
        #self.key = ''
        #self.secret = ''
       # self.alpaca_endpoint ='https://paper-api.alpaca.markets'
       # self.symbol = 'IVV'
        #self.current_order = None
        #self.last_price = 1

    #try:
       # self.position = int(self.api.get_position(self.symbol).qty)
   # except:
      #  self.position = 0

#def submit_order(self, target):
    #if self.current_order is not None:
        #self.api.cancel_order(self.current_order.id)

    