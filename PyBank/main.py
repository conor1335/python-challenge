import os
import csv
budget_csv = os.path.join("..", "budget_data.csv")
with open(budget_csv, newline="") as csvfile:
    csv_f = csv.reader(csvfile)

    csv_header = next(csvfile)

    month_count = 0
    pl_total = 0
    prev_pl = 0

    prev_bigg_loss = 0

    prev_bigg_prof = 0

    curr_diff = 0



    for row in csvfile:
        

        row_curr = row
        
        date,pl = row_curr.split(",")

        if(int(month_count) == 0):
            pl_ini = pl
            prev_bigg_prof
        
        curr_pl = pl

        month_count = month_count + 1   
        
        pl_total = int(pl) + pl_total

        curr_diff = int(curr_pl) - int(prev_pl)
        
        if curr_diff > 0:
            if(curr_diff > prev_bigg_prof):
                prev_bigg_prof = curr_diff
                prof_date = date
        
        if curr_diff < 0:
            if(curr_diff < prev_bigg_loss):
                prev_bigg_loss = curr_diff
                loss_date = date


        prev_pl = curr_pl
        
    diff = int(curr_pl) - int(pl_ini)
    avg_change = diff/(int(month_count)-1)
    

print("Financial Analysis\n----------------------")
print("Total Months: ",int(month_count))
print("Total: $", int(pl_total))
print("Average Change: $", round(avg_change,2))
print("Greatest Increase in Profits: ", prof_date, "($", int(prev_bigg_prof), ")")
print("Greatest Decrease in Profits: ", loss_date, "($", int(prev_bigg_loss),")")

output_file = 'bank.txt'
with open(output_file, "w", newline="") as datafile:
    csvwriter = csv.writer(datafile)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["---------------------"])
    csvwriter.writerow([f"Total Months:  {month_count}"])
    csvwriter.writerow([f"Average Change: $ {round(avg_change,2)} " ])
    csvwriter.writerow([f"Greatest Increase in Profits:  {prof_date} ($ {int(prev_bigg_prof)} )"])
    csvwriter.writerow([f"Greatest Decrease in Profits:  {loss_date} ($ {int(prev_bigg_loss)} )"])
    
