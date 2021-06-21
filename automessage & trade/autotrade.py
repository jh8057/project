import time
import pyupbit
import datetime
import requests

access = ""
secret = ""
myToken = ""

def post_message(token, channel, text):
    """슬랙 메시지 전송"""
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_ma15(ticker):
    """15일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
    ma15 = df['close'].rolling(15).mean().iloc[-1]
    return ma15

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")
# 시작 메세지 슬랙 전송
post_message(myToken,"#message", "autotrade start")

while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)

        # BTC
        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-BTC", 0.5)
            ma15 = get_ma15("KRW-BTC")
            current_price = get_current_price("KRW-BTC")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-BTC", krw*0.0995)
                    post_message(myToken,"#message", "BTC buy : " +str(buy_result))
        else:
            btc = get_balance("BTC")
            krw = get_balance("KRW")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-BTC", btc*0.0995)
                post_message(myToken,"#message", "BTC sell : " +str(sell_result))
            post_message(myToken,"#message", "Today KRW : " +str(krw))
        time.sleep(0.1)

        # DOGE
        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-DOGE", 0.1)
            ma15 = get_ma15("KRW-DOGE")
            current_price = get_current_price("KRW-DOGE")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-DOGE", krw*0.0995)
                    post_message(myToken,"#message", "DOGE buy : " +str(buy_result))
        else:
            doge = get_balance("DOGE")
            if doge > 0.00008:
                sell_result = upbit.sell_market_order("KRW-DOGE", doge*0.0995)
                post_message(myToken,"#message", "DOGE sell : " +str(sell_result))
        time.sleep(0.1)


        # LINK 
        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-LINK", 0.3)
            ma15 = get_ma15("KRW-LINK")
            current_price = get_current_price("KRW-LINK")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-LINK", krw*0.0995)
                    post_message(myToken,"#message", "LINK buy : " +str(buy_result))
        else:
            link = get_balance("LINK")
            if link > 0.00008:
                sell_result = upbit.sell_market_order("KRW-LINK", link*0.0995)
                post_message(myToken,"#message", "LINK sell : " +str(sell_result))
        time.sleep(0.1)

        # BCH 
        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-BCH", 0.7)
            ma15 = get_ma15("KRW-BCH")
            current_price = get_current_price("KRW-BCH")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-BCH", krw*0.0995)
                    post_message(myToken,"#message", "BCH buy : " +str(buy_result))
        else:
            bch = get_balance("BCH")
            if bch > 0.00008:
                sell_result = upbit.sell_market_order("KRW-BCH", bch*0.0995)
                post_message(myToken,"#message", "BCH sell : " +str(sell_result))
        time.sleep(0.1)
        
        #ETH
        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-ETH", 0.6)
            ma15 = get_ma15("KRW-ETH")
            current_price = get_current_price("KRW-ETH")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-ETH", krw*0.0995)
                    post_message(myToken,"#message", "ETH buy : " +str(buy_result))
        else:
            eth = get_balance("ETH")
            if eth > 0.00008:
                sell_result = upbit.sell_market_order("KRW-ETH", eth*0.0995)
                post_message(myToken,"#message", "ETH sell : " +str(sell_result))
        time.sleep(0.1)

        # ADA
        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-ADA", 0.5)
            ma15 = get_ma15("KRW-ADA")
            current_price = get_current_price("KRW-ADA")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-ADA", krw*0.0995)
                    post_message(myToken,"#message", "ADA buy : " +str(buy_result))
        else:
            ada = get_balance("ADA")
            if ada > 0.00008:
                sell_result = upbit.sell_market_order("KRW-ADA", ada*0.0995)
                post_message(myToken,"#message", "ADA sell : " +str(sell_result))
        time.sleep(0.1)

        #ETC
        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-ETC", 0.5)
            ma15 = get_ma15("KRW-ETC")
            current_price = get_current_price("KRW-ETC")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-ETC", krw*0.0995)
                    post_message(myToken,"#message", "ETC buy : " +str(buy_result))
        else:
            etc = get_balance("ETC")
            if etc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-ETC", etc*0.0995)
                post_message(myToken,"#message", "ETC sell : " +str(sell_result))
        time.sleep(0.1)

        #EOS
        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-EOS", 0.6)
            ma15 = get_ma15("KRW-EOS")
            current_price = get_current_price("KRW-EOS")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-EOS", krw*0.0995)
                    post_message(myToken,"#message", "EOS buy : " +str(buy_result))
        else:
            eos = get_balance("EOS")
            if eos > 0.00008:
                sell_result = upbit.sell_market_order("KRW-EOS", eos*0.0995)
                post_message(myToken,"#message", "EOS sell : " +str(sell_result))
        time.sleep(0.1)

        #MANA
        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-MANA", 0.2)
            ma15 = get_ma15("KRW-MANA")
            current_price = get_current_price("KRW-MANA")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-MANA", krw*0.0995)
                    post_message(myToken,"#message", "MANA buy : " +str(buy_result))
        else:
            mana = get_balance("MANA")
            if mana > 0.00008:
                sell_result = upbit.sell_market_order("KRW-MANA", mana*0.0995)
                post_message(myToken,"#message", "MANA sell : " +str(sell_result))
        time.sleep(0.1)

        #XLM
        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-XLM", 0.6)
            ma15 = get_ma15("KRW-XLM")
            current_price = get_current_price("KRW-XLM")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-XLM", krw*0.0995)
                    post_message(myToken,"#message", "XLM buy : " +str(buy_result))
        else:
            xlm = get_balance("XLM")
            if xlm > 0.00008:
                sell_result = upbit.sell_market_order("KRW-XLM", xlm*0.0995)
                post_message(myToken,"#message", "XLM sell : " +str(sell_result))
        time.sleep(0.1)

        #XRP
        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-XRP", 0.5)
            ma15 = get_ma15("KRW-XRP")
            current_price = get_current_price("KRW-XRP")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-XRP", krw*0.0995)
                    post_message(myToken,"#message", "XRP buy : " +str(buy_result))
        else:
            xrp = get_balance("XRP")
            if xrp > 0.00008:
                sell_result = upbit.sell_market_order("KRW-XRP", xrp*0.0995)
                post_message(myToken,"#message", "XRP sell : " +str(sell_result))
        time.sleep(1)

    except Exception as e:
        print(e)
        post_message(myToken,"#message", e)
        time.sleep(1)