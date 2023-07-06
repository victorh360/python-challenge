# python-challenge

This repository contains my work for the Module 3 Challenge, it is composed of two separate exercises, PyBank and Pypoll.
In this readme you will find links to resources I used to complete specific challenges I encountered.

## PyBank
For this challenge we were tasked with using python to analyze the financial records of a company, which were stored in a
.csv file. 
  -For this exercise I chose to store each column of the csv file in an individual list, to then manipulate
    and pull the data from them
  - To find the monthly change in profit I used https://www.geeksforgeeks.org/python-generate-successive-element-difference-list/amp/
    I then stored the results in a new list: 
    *"monthly_change = [profit_loss[i + 1] - profit_loss[i] for i in range (len(profit_loss) - 1)]"*
  - When writing my results to a .txt file, at first everything was printed in one line, to fix this I had to employ the *"\n"*
    method found here: https://mkyong.com/python/how-to-write-a-file-in-python/ to write to a new line.

## PyPoll
In this challenge we were provided with election results in the form of a .csv file, we were then asked to pull the candidate names,
election results and find a winner.
  - For this exercise I chose to store my data in a library. I stored each candidate name and a list with the voter id for each vote
    a candidate received.
  - I was struggling for the right syntax to assign a winning candidate. I worked with a tutor who pointed me in the right direction.
    https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary eventually I worked out that writing a
    for loop *"for name in candidate_list:"* along with *"winner = max(votes, key=votes.get)"* would get me the answer I needed.
  - At first I tried to create a list to calculate and store each candidates total votes as a percentage, eventually I found that it
  was more efficient to calculate the percentage inside my print and write statements by creating a loop through the names in
  candidate_list.
  - I used https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-36.php to learn how to properly
  format my decimal results as a percentage.
  *str("{:.3%}".format(votes[name] / vote_total))*
