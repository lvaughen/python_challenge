# Modules
import os
import csv

# Set path for file
csvelect = os.path.join('Resources', 'election_data.csv')



# Open the CSV
with open(csvelect) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # print(csvreader)

    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")


    row_count = []
    voter_id = []
    elect_county = []
    elect_candidate = []

    # Read each row of data after the header
    for row in csvreader:
        # print(row)
        row_count.append(row)
        voter_id.append(row[0])
        elect_county.append(row[1])
        elect_candidate.append(row[2])

# Calculations

    vote_tot = 0
    cand_vot = []
    ind_vot = ['0','0','0','0','0']
    vot_perc = []

    vote_tot = len(row_count)
    print(vote_tot)

    cand_set = list(set(elect_candidate))
    print(cand_set)

    cand_num = len(cand_set)
    print(cand_num)


    for row in elect_candidate:
        for num in range(cand_num):
            # print(f'Candidate {row}')
            # print(cand_set[num])
            
            if row == cand_set[num]:
                ind_vot[num] = int(ind_vot[num]) + 1
                #print("match")

print(ind_vot)

# calculate percent of vote

for num in range(cand_num):
    vot_perc.append(ind_vot[num] / vote_tot)
    print(vot_perc)



# calculate the election winner
if ind_vot[0] > ind_vot [1]:
    if ind_vot[0] > ind_vot[2]:
        if ind_vot[0] > ind_vot[3]:
            winner = 0
        else:
            winner = 3
    elif ind_vot[2] > ind_vot[3]:
        winner = 2
    else:
        winner = 3

elif ind_vot[1] > ind_vot[2]:
    if ind_vot[1] > ind_vot[3]:
            winner = 1
    else:
            winner = 3
elif ind_vot[2] > ind_vot[3]:
    winner = 2

else:
    winner =3

#print(cand_set[winner])


# print output
report_data = f"""
Election Results
----------------------------
Total Votes: {vote_tot}
----------------------------
"""

print("Election Results")
print('----------------------------')
print(f'Total Votes: {vote_tot}')
print('----------------------------')

# for num in range(cand_num):
for num in range(cand_num):
    report_data += f' {cand_set[num]} {str(vot_perc[num])}% ({ind_vot[num]})\n'

report_data += f"""
---------------------------
Winner: {cand_set[winner]}
----------------------------
"""

print(report_data)






# file output
# Specify the file to write to
output_path = os.path.join("Analysis","results.csv")

# # Open the file using "write" mode. Specify the variable to hold the contents
# # with open("results.csv", 'w') as csvout:
with open(output_path, 'w') as csvout:
#     # csvout.writelines(ouput_list)

#         # csvwriter = csv.writer(csvout, delimiter=",")
#         # csvwriter.writerow(output_list)

    csvout.write(report_data)
    