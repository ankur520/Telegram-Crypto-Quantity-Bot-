from tkinter import N


entry = 382.20
sl = 396
portfolio = 200 
leverage = 5
rpt = 2

usdtPercent = int(portfolio * rpt / 100)
slDifference = entry - sl
# quantity
calculateQuantity = abs(usdtPercent / (slDifference * leverage))
formatted_calculateQuantity = "{:.5f}".format(calculateQuantity)
# trade amount 
calQuanTradeAmount = abs(int(calculateQuantity * entry))
# sl Percent 
slDifferencePercent =   float(slDifference / entry * 100)
formatted_slDifferencePercent = "{:.2f}".format(slDifferencePercent)


#  loss Dollars 
lossDollars = abs(calculateQuantity * (slDifference * leverage ))
# formatted_lossDollars = "{:.2f}".format(lossDollars)


# total profit % with leverage 
profitPercent = abs(slDifferencePercent * leverage)
formatted_profitPercent = "{:.2f}".format(profitPercent)


messageRPT = "Your RPT is --> " + str(usdtPercent) + " $ "
messageQuantity =  "Quantity --> " + str(formatted_calculateQuantity) 
messageTradeAmount = "Trade Amount --> " + str(calQuanTradeAmount) + "$" 
messageLossDollars = "LossDollars --> "  + str(lossDollars) 
messageProfitPercent = "% Profit on "+ str( leverage) + "X --> " + str(formatted_profitPercent) + " %"
# messageProfitDollar =  "Profit --> " + str(profitDollar) +" $"

reply = messageRPT + "\n" + messageTradeAmount  + "\n" + messageQuantity + "\n" +  messageLossDollars + "\n" +  messageProfitPercent  

print(reply)