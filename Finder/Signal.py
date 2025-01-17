from email.policy import default
import Enum.CommonEnum as enum
import Finder.Pattern as pattern
import Finder.CandleStick as candle
import Finder.SupportResistence as sr

#https://medium.com/geekculture/candlestick-trading-a-full-guide-on-patterns-and-strategies-b1efcb98675c

def basedOn_Piercing_Dark_CloudSystem(prev_openPrice, prev_closePrice, openPrice, closePrice):
    signal = enum.Signal.NONE
    if pattern.isPiercingCloudCoverPattern(prev_openPrice, prev_closePrice, openPrice, closePrice):
        signal = enum.Signal.BUY    
    if signal == enum.Signal.NONE and pattern.isDarkCloudCoverPattern(prev_openPrice, prev_closePrice, openPrice, closePrice):
        signal = enum.Signal.SELL
    return signal

def basedOn_HammerCandleSys(openPrice, highPrice, lowPrice, closePrice):
    match candle.find_Hammer_Sys(openPrice, highPrice, lowPrice, closePrice):
        case enum.HammerCandleSys.Hammer | enum.HammerCandleSys.InvertedHammer:
            return enum.Signal.BUY
        case enum.HammerCandleSys.HangingMan:
            return enum.Signal.SELL
        #case _:
        case default:
            return enum.Signal.NONE

def basedOn_ThreeCandles(highPrice, prev1_highPrice, prev2_highPrice, prev3_highPrice):
    signal = enum.Signal.NONE
    if pattern.find_ThreeWhiteKnights(highPrice, prev1_highPrice, prev2_highPrice, prev3_highPrice):
        signal = enum.Signal.BUY
    elif pattern.find_ThreeBlackCrows(highPrice, prev1_highPrice, prev2_highPrice, prev3_highPrice):
        signal = enum.Signal.SELL
    return signal

def basedOn_StarCandleSys(openPrice, highPrice, closePrice, prev1_openPrice, prev1_highPrice, prev1_lowPrice, prev1_closePrice, prev2_openPrice, prev2_closePrice):
    signal = enum.Signal.NONE
    match candle.find_Star_Sys(openPrice, highPrice, closePrice, prev1_openPrice, prev1_highPrice, prev1_lowPrice, prev1_closePrice, prev2_openPrice, prev2_closePrice):
        case enum.StarCandleSys.MORNING:
            return enum.Signal.BUY
        case enum.StarCandleSys.EVENING:
            return enum.Signal.SELL
        #case _:
        case default:
            return enum.Signal.NONE

def basedOn_DojiCandleSys(openPrice, closePrice, prev_openPrice, prev_closePrice):
    signal = enum.Signal.NONE
    match candle.find_Doji_Sys(openPrice, closePrice, prev_openPrice, prev_closePrice):
        case enum.DojiCandleSys.BULL:
            return enum.Signal.BUY
        case enum.DojiCandleSys.BEAR:
            return enum.Signal.SELL
        #case _:
        case default:
            return enum.Signal.NONE 

def basedOn_MarubozuCandleSys(openPrice, highPrice, lowPrice, closePrice):
    signal = enum.Signal.NONE
    match candle.find_Marubozu_Sys(openPrice, highPrice, lowPrice, closePrice):
        case enum.MarubozuCandleSys.BULL:
            return enum.Signal.BUY
        case enum.MarubozuCandleSys.BEAR:
            return enum.Signal.SELL
        #case _:
        case default:
            return enum.Signal.NONE 

def basedOn_Harami_Pattern(openPrice, highPrice, lowPrice, closePrice, prev_openPrice, prev_closePrice):
    signal = enum.Signal.NONE
    match pattern.find_Harami_Pattern(openPrice, highPrice, lowPrice, closePrice, prev_openPrice, prev_closePrice):
        case enum.HaramiCandleSys.BULL:
            return enum.Signal.BUY
        case enum.HaramiCandleSys.BEAR:
            return enum.Signal.SELL
        #case _:
        case default:
            return enum.Signal.NONE 

def basedOn_ThreeSystem_Method(openPrice, closePrice, prev1_closePrice, prev1_openPrice, prev2_openPrice, prev2_closePrice, prev3_openPrice, prev3_closePrice, prev4_openPrice, prev4_closePrice):
    signal = enum.Signal.NONE
    match pattern.ThreeSystem_Method(openPrice, closePrice, prev1_closePrice, prev1_openPrice, prev2_openPrice, prev2_closePrice, prev3_openPrice, prev3_closePrice, prev4_openPrice, prev4_closePrice):
        case enum.ThreeSystem_Method.BULL:
            return enum.Signal.BUY
        case enum.ThreeSystem_Method.BEAR:
            return enum.Signal.SELL
        #case _:
        case default:
            return enum.Signal.NONE 

def basedOn_First_SupportResistence(supportresistence: sr, candle, trend, live_open_price, live_close_price):
    signal = enum.Signal.NONE
    if supportresistence.ready_at_enter == enum.SR_First_Method.BUY_AT_RESISTENCE or \
    supportresistence.ready_at_enter == enum.SR_First_Method.BUY_AT_SUPPORT:
        signal = enum.Signal.BUY
    elif supportresistence.ready_at_enter == enum.SR_First_Method.SELL:
        signal = enum.Signal.SELL
    return signal

def basedOnCandle(openPrice, closePrice): 
    signal = enum.Signal.NONE
    candl = candle.getCandleColor(openPrice, closePrice)
    if candl == enum.Candle.GREEN:
        signal = enum.Signal.BUY
    elif candl == enum.Candle.RED:
        signal = enum.Signal.SELL

    return signal

