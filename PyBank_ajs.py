

import csv
import os

file_in = os.path.join("bootcamp", "budget_data.csv")
file_out = os.path.join("bootcamp", "budget_analysis.txt")

total_months = 0 # 2 (after first for loop iteration)
month_of_change = []
net_change_series = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999]
total_net = 0 # 867884 (after first for loop iteration)

# Read the csv and convert it into a list of dictionaries
with open(file_in) as final_data:
    # reader -> kind of like a robot that will do something for us
    reader = csv.reader(final_data)

    # Read the header row
    header = next(reader)

    first_row = next(reader) # [Jan-2010,867884]
    total_months = total_months + 1 # tallying months
    total_net = total_net + int(first_row[1]) # 0 + 867884
    prev_net = int(first_row[1]) # 867884

    #                                   row[0]   row[1]
    for row in reader: # current row: [Feb-2010, 984655]

        # Track the total
        total_months = total_months + 1
        total_net = total_net + int(row[1]) # 867884 + 984655

        # Track the net change
        net_change = int(row[1]) - prev_net # 984655 - 867884 = ~120,000
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Calculate the Average Net Change
net_monthly_avg = sum(net_change_series) / len(net_change_series)

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(file_out, "w") as txt_file:
    txt_file.write(output)