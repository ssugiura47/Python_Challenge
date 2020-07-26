import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

print("Financial Analysis:")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    for row in csvreader:
        row_count = sum(1 for row in csvreader)
    print("Total number of months: " + str(row_count))

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader) 
    row_profit = 0
    for row in csvreader:
        row_profit = row_profit + int(row[1])
    print("Total profit: $" + str(row_profit))

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    totalchange = []
    previousrow = 0
    for row in csvreader:
        change = (int(row[1]) - int(previousrow))
        totalchange.append(change)
        previousrow = row[1]
    
    totalchange.pop(0)
    
    total = 0
    for changes in range(0, len(totalchange)):
        total = total + totalchange[changes]

    for row in totalchange:
        totalchangerow_count = sum(1 for row in totalchange)
    
    average = (int(total)/int(totalchangerow_count))   
    print("Total average change: $" + str(average))

    maxNumber = 0
    for number in totalchange:
        if maxNumber < number:
            maxNumber = number
    print("The greatest increase in profits: $" + str(maxNumber))

    minNumber = 0
    for number in totalchange:
        if minNumber > number:
            minNumber = number
    print("The greatest decrease in losses: $" + str(minNumber))


write_file = open(os.path.join("Analysis", "pybank_results.txt"), 'w+')
write_file.write(f"Total number of months:  {row_count}")
write_file.write(f", Total profit: ${row_profit}")
write_file.write(f", Total average change: ${average}")
write_file.write(f", The greatest increase in profits: ${maxNumber}")
write_file.write(f", The greatest decrease in losses: ${minNumber}")

