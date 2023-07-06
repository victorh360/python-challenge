import csv

#set relative path to csv file
csvpath = 'PyPoll\Resources\election_data.csv'

with open(csvpath) as election_data:
    
    #read csv file and set delimiter
    csvreader = csv.reader(election_data, delimiter=',')
   
    #set header row
    csv_header = next(csvreader)
    
    vote_total = 0
    
    #create library to store candidate name and vote count
    candidate_list = []
    votes = {}
    
    for row in csvreader:
        
        #count each row in csv file to have a total number of votes cast
        vote_total = vote_total + 1

        #set location of candiate name in file
        name = row[2]

        #add candidate name to list, set vote count
        if name not in candidate_list:

            candidate_list.append(name)

            votes[name] = 0
        
        #count each vote per candidate name
        votes[name] += 1
    
    #loop through candidate list to find the winner
    for name in candidate_list:
        
    #Used method outlined in link to pull the max value to name a winner.
    #https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
        winner = max(votes, key=votes.get)

#print data to terminal, formatted like challenge example
print("Election Results")
print("-----------------")
print("Total Votes: " + str(vote_total))
print("-----------------")

#loop through candidate list, print name, calculate percentage of votes and print total votes.
#Use link below to learn how to format as percent
#Used linked method to format as percentage to 3 decimal places
#https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-36.php
for name in candidate_list:
    print(name + ": " + str("{:.3%}".format(votes[name] / vote_total)) + " (" + str(votes[name]) + ")")

print("-----------------")
print("Winner: " + str(winner))   
print("-----------------")       
    
#create file named Analysis to write results to
with open('PyPoll\Analysis\Analysis.txt', "w") as f:
    
    #write results in same format as printed results
    #add \n to break to a new line
    f.write("Election Results" + "\n")
    f.write("-----------------" + "\n")
    f.write("Total Votes: " + str(vote_total) + "\n")
    f.write("-----------------" + "\n")
    
    for name in candidate_list:
        f.write(name + ": " + str("{:.3%}".format(votes[name] / vote_total)) + " (" + str(votes[name]) + ")" + "\n")
    
    f.write("-----------------" + "\n")
    f.write("Winner: " + str(winner) + "\n")   
    f.write("-----------------" + "\n")