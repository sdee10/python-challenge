import os
import csv
print("Financial Analysis")
print("-----------------------------")
budget_data_path = os.path.join('Resources', 'budget_data.csv')

with open(budget_data_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    data = list(csvreader)
    date, profit_loss =  zip(*data)
    #print('date =', date)
    #print('profit and loss =', profit_loss)
    xtol  = [int(x) for x in profit_loss if x]
    #print(xval)
    total_date = len(date)
    print("Total Month: " + str(total_date))
    total_profit_loss = sum(xtol)
    print("Total Profit and Loss: " + str(total_profit_loss))
    revenue_change = []
    for i in range(1, len(xtol)):
        revenue_change.append((int(xtol[i]) - int(xtol[i-1])))
    # calculate average revenue change
    revenue_average = sum(revenue_change) / len(revenue_change)
    print("Average change is: " + str(revenue_average))
    maxtotal = max(xtol)
    print("The greatest increase is: " + str(date[revenue_change.index(max(revenue_change))+1]) + " " + str(maxtotal))
    mintotal = min(xtol)
    print("The greatest decrease is: " + str(date[revenue_change.index(min(revenue_change))+1]) + " " + str(mintotal))

    
    file = open("output.txt","w")
    file.write("Financial Analysis" + "\n")
    file.write("...................................................................................." + "\n")
    file.write("Total Month: " + str(total_date) + "\n")
    file.write("Total Profit and Loss: " + str(total_profit_loss) + "\n")
    file.write("Average change is: " + str(revenue_average) + "\n")
    file.write("The greatest increase is: " + str(date[revenue_change.index(max(revenue_change))+1]) + " " + str(maxtotal) + "\n")
    file.write("The greatest decrease is: " + str(date[revenue_change.index(min(revenue_change))+1]) + " " + str(mintotal) + "\n")
    file.close()
        
        