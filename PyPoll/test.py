import os
import csv
import unicodecsv
cereal_csv = os.path.join("..", "budget_data")

# Open and read csv
with open(cereal_csv, newline="") as csvfile:
    csvreader = unicodecsv.reader(csvfile, delimiter=",",encoding='utf-8-sig')

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csvreader:

        # Convert row to float and compare to grams of fiber
        if float(row[7]) >= 5:
            print(row)
