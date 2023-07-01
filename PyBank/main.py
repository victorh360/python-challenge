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
    #print("Average Change: " + str(average_change))
    #print("Greatest Increase in Profits " + str(increase))
    #print("Greatest Decrease in Profits " + str(decrease))
        
        
        #used "\n" method from https://mkyong.com/python/how-to-write-a-file-in-python/ to write individual lines 
    with open('PyBank\Analysis\Analysis.txt', "w") as f:
        f.write("Financial Analysis" + "\n")
        f.write("------------------" + "\n")
        f.write("Total Months: " + str(total_months) + "\n")
        f.write("Total: " + str(net_total) + "\n")
        f.write("Average Change: " + "\n")
        f.write("Greatest Increase in Profits: " + "\n")
        f.write("Greatest Decrease in Profits: " + "\n")
                
   
    
   
    
           
    

    
    
    
    
    