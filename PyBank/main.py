import csv

#set relative path to csv file
csvpath = 'PyBank\Resources\pbbudget_data.csv'

with open(csvpath) as budget_data:
    
    #read csv file
    csvreader = csv.reader(budget_data, delimiter=',')
    next(csvreader)   

    #make blank list for months
    months = []
    
    #make blank list for monthly profit or loss data
    profit_loss = []

    #iterate through csv file and store month and profit/loss values to lists
    for row in csvreader:
               
        months.append(row[0])
                
        profit_loss.append(int(row[1]))
    
    #calculate number of months in file
    total_months = len(months)

    #calculate total monthly values by using sum function on list
    net_total = sum(profit_loss)

    #Use formula for comparing values in a list from: https://www.geeksforgeeks.org/python-generate-successive-element-difference-list/amp/
    #Store values in a new list
    monthly_change = [profit_loss[i + 1] - profit_loss[i] for i in range (len(profit_loss) - 1)]

    #calculate average monthly change, round to 2 decimal places
    avg_change = round(sum(monthly_change) / len(monthly_change), 2)    

    #calculate min and max monthly change values, use value optained to reference the index for value in the month list 
    increase = max(monthly_change)    
    imonth = months[monthly_change.index(increase) + 1]
    decrease = min(monthly_change)
    dmonth = months[monthly_change.index(decrease) + 1]

    #write print statement for values obtained to return values to terminal, format properly
    print("Total Months: " + str(total_months))    
    print("Total: " + "$" + str(net_total))
    print("Average Change: " + "$" + str(avg_change))
    print("Greatest Increase in Profits " + str(imonth) + " ($" + str(increase) + ")")
    print("Greatest Decrease in Profits " + str(dmonth) + " ($" +str(decrease) + ")")

    #create a text file in analysis folder, writye values to folder, convert to string        
    #used "\n" method from https://mkyong.com/python/how-to-write-a-file-in-python/ to write individual lines 
    with open('PyBank\Analysis\Analysis.txt', "w") as f:
        f.write("Financial Analysis" + "\n")
        f.write("-------------------------" + "\n")
        f.write("Total Months: " + str(total_months) + "\n")
        f.write("Total: " + str(net_total) + "\n")
        f.write("Average Change: " + "$" + str(avg_change) + "\n")
        f.write("Greatest Increase in Profits: " + str(imonth) + "($" + str(increase) + ")" + "\n")
        f.write("Greatest Decrease in Profits: " + str(dmonth) + "($" +str(decrease) + ")" + "\n")
                
   
    
   
    
           
    

    
    
    
    
    