import csv

csvpath = 'PyBank\Resources\pbbudget_data.csv'

with open(csvpath) as budget_data:
    
    csvreader = csv.reader(budget_data, delimiter=',')
    next(csvreader)   

    total_months = 0
    
    net_total = 0
    
    
        
    for row in csvreader:
        
        total_months += 1
        
        net_total = net_total + int(row[1])
        
        
        
        
        
    print("Total Months: " + str(total_months))    
    print("Total: " + str(net_total))
    print("Average Change: " + str(average_change))
    print("Greatest Increase in Profits " + str(increase))
    print("Greatest Decrease in Profits " + str(decrease))
           
    

    
    
    
    
    