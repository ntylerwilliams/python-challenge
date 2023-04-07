import os
import csv

voteTotal = 0
candidates = {}


resourcePath = os.path.join(".", "Resources", "election_data.csv")
with open(resourcePath, "r") as file:
    pollCSV = csv.reader(file)
    header = next(pollCSV)

    for index, row in enumerate(pollCSV):
        voteTotal = voteTotal + 1
        
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

print("Election Results")
print("-------------------------")
print(f"Total Votes: {voteTotal}")
for candidate in candidates:
    print(f"{candidate}: {100*(candidates[candidate]/voteTotal):.3f}% ({candidates[candidate]})")
print("-------------------------")
winner = max(candidates.values())
for candidate in candidates:
    if candidates[candidate] == winner:
        print(f"Winner: {candidate}")
print("-------------------------")

outputFile = os.path.join(".", "analysis", "analysis.txt")
with open(outputFile, "w") as file:
    file.write(f"Election Results\n")
    file.write(f"-------------------------\n")
    file.write(f"Total Votes: {voteTotal}\n")
    file.write("-------------------------\n")
    for candidate in candidates:
        file.write(f"{candidate}: {100*(candidates[candidate]/voteTotal):.3f}% ({candidates[candidate]})\n")
    file.write("-------------------------\n")
    winner = max(candidates.values())
    for candidate in candidates:
        if candidates[candidate] == winner:
            file.write(f"Winner: {candidate}\n")
    file.write("-------------------------")
        