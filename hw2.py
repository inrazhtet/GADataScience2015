# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 10:59:16 2015

@author: zarnihtet
"""
'''
1 Using tab delimiter to handle the tsv file
'''
import csv
with open('chipotle.tsv', mode = 'rU') as f:
    file_nested_list = [row for row in csv.reader(f, delimiter = '\t')]
#print(file_nested_list)

'''    
2 Separating Head and Data
'''
header = file_nested_list[0]
data = file_nested_list[1:]
#print(data)

'''
3 Average Price of an order
First I am going to find the total number of orders
'''
num_orders = []
sum_orders = sum([(float(row[1])) for row in data])
#print(sum_orders)

num_rev = []
total_rev = sum([(float(row[4][1:])) for row in data])
#print(total_rev)

avg_order_price = total_rev/sum_orders
print(avg_order_price)

'''
4  Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''

soda_list = []
usoda_list = []
soda_list = [(row[3]) for row in data if ((row[2] == 'Canned Soda') | (row[2] == 'Canned Soft Drink'))]
#print(soda_list)
for row in soda_list:
    if row in usoda_list:
        continue
    else:
        usoda_list.append(row)
print(usoda_list)

'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!

'''
burrito_count = len([row [2] for row in data if row[2].find('Burrito')!= -1])
#print(burrito_count)

sum_toppings = 0
tmp = []
for row in data:
    if row[2].find('Burrito')!= -1:
        #print('success')
        tmp = row[3].split(',')
        sum_toppings += len(tmp)
#print(sum_toppings)    

avg_toppings = sum_toppings/burrito_count
#print(avg_toppings)

'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''
chips = []
uchips = []
order_counts = []
chips =[row[2] for row in data if row[2].find('Chips')!= -1]
for row in chips:
    if row in uchips:
        continue
    else:
        uchips.append(row)
#print(uchips)

for row in uchips:
    count_sum = 0
    for rows in data:
        if row == rows[2]:
            count_sum += int(rows[1])
    order_counts.append(count_sum)
#print(order_counts)
            
chip_orders = dict(zip(uchips,order_counts))
print(chip_orders)



    
