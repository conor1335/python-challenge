import os
import csv
poll_csv = os.path.join("..", "election_data.csv")

candy_list = []
loop_candy = 0
row_count = 0
max_vote = 0

with open(poll_csv, 'r', newline="") as csvfile:
    csv_f = csv.reader(csvfile)
    csv_header = next(csv_f)
    

    for row in csv_f:       
            row_curr = row          
            row_count = row_count + 1
            candidate = row[2]
            candy_list.append(candidate)
    candy_set = set(candy_list)
    candy_list_clean = list(candy_set)
    x = len(candy_list_clean)



output_file = 'poll.txt'
with open(output_file, 'w+', newline="") as pollfile:
    print("Election Results\n-------------------------")
    pollfile.writelines("Election Results\n-------------------------\n")
    print("Total Votes: ", row_count)
    pollfile.writelines(f"Total Votess: {row_count} \n-----------------------------\n")
    print("-----------------------------")
    while loop_candy < x:
        name_candy = candy_list_clean[loop_candy]
        vote_candy = candy_list.count(candy_list_clean[loop_candy])
        percent = round(((int(vote_candy))/int(row_count))*100, 2)     
        print(name_candy + ": " + str(percent) + " %   " + "(" + str(vote_candy) + ")")
        pollfile.writelines(f"{name_candy} : {str(percent)} %   ({str(vote_candy)})\n")
        if(int(vote_candy) > max_vote):
            max_vote = int(vote_candy)
            max_vote_candy = str(name_candy)
        loop_candy = loop_candy + 1
    pollfile.writelines(f"-------------------\nWinner: {max_vote_candy}\n-----------------------")
    print("------------------------")
    print("Winner: ", max_vote_candy)
    print("------------------------")
    
    












    

    










