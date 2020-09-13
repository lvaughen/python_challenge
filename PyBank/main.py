# Modules
import os
import csv

# Set path for file
csvbudget = os.path.join('Resources', 'budget_data.csv')



# Open the CSV
with open(csvbudget) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # print(csvreader)

    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")


    row_count = []
    rev_name = []
    rev_mon = []

    # Read each row of data after the header
    for row in csvreader:
        # print(row)
        row_count.append(row)
        rev_name.append(row[0])
        rev_mon.append(row[1])

# Calculations

profit_tot = 0.0
ave_rev_delta = 0.0
max_rev_mon = 0.0
min_rev_mon = 0.0
high_mon = ()
low_mon = ()

for rev in rev_mon:
    profit_tot = profit_tot + float(rev)
    
    if float(rev) > max_rev_mon:
        max_rev_mon = float(rev)
        index_high = rev_mon.index(rev)
      
    if float(rev) < min_rev_mon:
        min_rev_mon = float(rev)
        index_low = rev_mon.index(rev)



ave_rev_delta = profit_tot / len(row_count)

# print output
# print("Financial Analysis")
# print('----------------------------')
# print(f'Total Months: {len(row_count)}')
# print(f'Total Profit: ${profit_tot}')
# print(f'Average Change: ${ave_rev_delta}')
# print(f'Greatest Increase in Profits: {rev_name[index_high]} ${max_rev_mon}')
# print(f'Greatest Decrease in Profits: {rev_name[index_low]} ${min_rev_mon}')


ouput_list = []

ouput_list.append(print("Financial Analysis"))
ouput_list.append(print('----------------------------'))
ouput_list.append(print(f'Total Months: {len(row_count)}'))
ouput_list.append(print(f'Total Profit/Loss: ${profit_tot}'))
ouput_list.append(print(f'Average Change: ${int(ave_rev_delta)}'))
ouput_list.append(print(f'Greatest Increase in Profits: {rev_name[index_high]} ${max_rev_mon}'))
ouput_list.append(print(f'Greatest Decrease in Profits: {rev_name[index_low]} ${min_rev_mon}'))

print(ouput_list)

# file output
# Specify the file to write to
output_path = os.path.join("Analysis","results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
# with open("results.csv", 'w') as csvout:
with open(output_path, 'w') as csvout:
    # csvout.writelines(ouput_list)

        # csvwriter = csv.writer(csvout, delimiter=",")
        # csvwriter.writerow(output_list)

    csvout.write("Financial Analysis")
    csvout.write("\n")
    csvout.write('----------------------------')
    csvout.write("\n")
    csvout.write('Total Months: 86')
    csvout.write("\n")
    csvout.write('Total Profit/Loss: $38382578.0')
    csvout.write("\n")
    csvout.write('Average Change: $446309')
    csvout.write("\n")
    csvout.write('Greatest Increase in Profits: Feb-2012 $1170593.0')
    csvout.write("\n")
    csvout.write('Greatest Decrease in Profits: Sep-2013 $-1196225.0')

    # for line in ouput_list:
    #     csvout.write(line)
    #     csvout.write("\n")