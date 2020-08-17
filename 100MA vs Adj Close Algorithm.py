


#Ademola Adam Asimolowo
#Adj Close vs 100 MA Technical Anaylsis Algorithm
#UTILIZING YAHOO API

import datetime as date
import matplotlib.pyplot as plotter 
from matplotlib import style 
import pandas as pd 
import pandas_datareader.data as datareader #reads data from api
import matplotlib.ticker as ticker

print(date)
print(pd)
print(plotter)
print(datareader)
print(ticker)


def get_data(ticker, api):

    start_date = date.datetime(2020, 5, 9) #starting date for our stock analysis. where we start our analysis
    end_date = date.datetime(2020, 8, 14) #end date for our stock anaylsis. where we end our analysis
    df = datareader.DataReader(ticker, api, start_date, end_date)
    
    return df

def adj_close_100ma_algo(ticker):
    datafrme = get_data('AMD', 'yahoo')
    datafrme['100MA'] = datafrme["Adj Close"].rolling(window = 100, min_periods = 0).mean() 
    print(datafrme.tail(100))
    
    #setting up graph
    ax1 = plotter.subplot2grid((6, 1), (0, 0), rowspan = 5, colspan = 1) #6 by 1 so 6 rows 1 column, starting point (0,0)

    ax1.set_title(ticker + " - Adj Close vs 100MA")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Price")
    ax1.plot(datafrme.index, datafrme['Adj Close'])#ax1.plot(x, y) so ax1.plot(df.index(the date), df['Adj Close']#the price or y axis)
    ax1.plot(datafrme.index, datafrme['100MA'])
    plotter.xticks(rotation=35)
    
    #KEY FOR GRAPH
    #BLUE = 100MA RED = ADJ CLOSE
    
    print(df.head())

    bullish_days = 0
    bearish_days = 0
    no_signal = 0

    for i in datafrme.index:
        #print("Adj Close: " + str(df.iloc[:, 5][i]))#prints out the volume for each date
        #print("100 MA: " + str(df.iloc[:, 6][i]))

        if datafrme.iloc[:, 5][i] > datafrme.iloc[:, 6][i]:
            bullish_days += 1
            #print("Bullish signature")
        elif datafrme.iloc[:, 5][i] == datafrme.iloc[:,6][i]:
            no_signal += 1
            #print(str(i) + "100 MA and Adj Close equal to each other, no signal")
        else:
            bearish_days += 1
            #print("Bearish signature")

    print(""), print("           -----PRICE VS 100 MA ANALYSIS-----")
    print("Bullish Days: " + str(bullish_days) + "\nBearish Days: " + str(bearish_days) + "\nNo Signal Days: " + str(no_signal)+ "\n\n")
    if bullish_days > bearish_days:
        print("Technical Mid-Term Signal: Bullish on " + ticker + " from a Technical standpoint")
    else:
        print("Technical Mid-Term Signal: Bearish on " + ticker+ " from a Technical standpoint")


    
adj_close_100ma_algo('AMD')
    
    

