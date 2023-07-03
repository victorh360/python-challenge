import csv

#set relative path to csv file
csvpath = 'PyPoll\Resources\election_data.csv'

with open(csvpath) as election_data:
    
    csvreader = csv.reader(election_data, delimiter=',')
    next(csvreader)
    
    vote_total = 0
    
    candidate_list = []

    
    for row in csvreader:
        
        #count each row in csv file to have a total number of votes cast
        vote_total = vote_total + 1

        name = row[2]

        if name not in candidate_list:

            candidate_list.append(name)




    
