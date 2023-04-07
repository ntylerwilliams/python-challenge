import os
import csv

months = 0
netIncome = 0
changes = []
year_months = []
prev = 0

resourcePath = os.path.join(".", "Resources", "budget_data.csv")
with open(resourcePath, "r") as file:
    bankCSV = csv.reader(file)
    header = next(bankCSV)

    for index, row in enumerate(bankCSV):
        months = (months + 1)
        netIncome = netIncome + int(row[1])
        if index > 0:
            changes.append(int(row[1]) - prev)
            year_months.append(row[0])
        prev = int(row[1])

meanChange = sum(changes) / len(changes)
minVal = min(changes)
maxVal = max(changes)
minIndex = changes.index(minVal)
maxIndex = changes.index(maxVal)
minIncreaseD = year_months[minIndex]
maxIncreaseD = year_months[maxIndex]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${netIncome}")
print(f"Average Change: ${meanChange:0.2f}")
print(f"Greatest Increase in Profits: {maxIncreaseD} (${maxVal})")
print(f"Greatest Decrease in Profits: {minIncreaseD} (${minVal})")

outputFile = os.path.join(".", "analysis", "analysis.txt")
with open(outputFile, "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {months}\n")
    file.write(f"Total: ${netIncome}\n")
    file.write(f"Average Change: ${meanChange:0.2f}\n")
    file.write(f"Greatest Increase in Profits: {maxIncreaseD} (${maxVal})\n")
    file.write(f"Greatest Decrease in Profits: {minIncreaseD} (${minVal})")