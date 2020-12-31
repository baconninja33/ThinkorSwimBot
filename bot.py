#this bot will connect to the alpaca_trade_api as trade api
#this is using paper wallet

#import alpaca_trade_api as tradeapi
import pip._vendor.requestsfrom config import *
BASE_URL = "https://paper-api.alpaca.markets"

r = requests.get(BASE_URL)

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

    