##### HomeWork 1

..1. Look at the head and the tail of chipotle.tsv in the data subdirectory of this repo. Think for a minute about how the data is structured. What do you think each column means? What do you think each row means? Tell me! (If you're unsure, look at more of the file contents.)

'''Commandline
head -10 chipotle.tsv
tail chipotle.tsv
'''
The data is on food orders. The column variables enumerate the food order, the type of food, the ingredients, the price.
The row variable as a line is a food item. Some have multiple orders of the same type of food.

..2. How many orders do there appear to be?

To answer this question, I believe I would have to sum up the order quantity column. How to go about doing this?

'''CommandLine First Step
cat chipotle.tsv | awk '{ print $2 }' > total.csv
'''
I printed out all the lines from the chipotle file. Then, I piped it into the command awk which is a pattern-matching function. For my purposes, I wanted only the second column so I use **$2** which specifies that. The next step requires me to add those numbers up. Therefore, I piped the cleaned results to a csv file. I have referenced the following sources for this usage.
[For usage of awk](http://unix.stackexchange.com/questions/25138/how-to-print-certain-columns-by-name)

'''CommandLine Second Step
paste -s -d "+" total.csv | bc
'''
The paste function concatenates all the separate lines from total.csv in a single line. It is specified by the *-s* argument. The *-d* argument puts in *+* instead of the tabs that have replaced the */n* due to the *-s* argument. Then, we piped the results to **bc** function. **bc** function evaluates expressions by its given nature which in our case is *+*. This works out well for us and our final result is **4972**. I have referenced the following sources for this usage.

[For usage of paste and bc](http://www.linuxandlife.com/2013/09/5-different-command-methods-to-get-sum.html)

..3. How many lines are in this file?

'''Command Line
wc -l chipotle.tsv
'''
There are **4623** lines in this Chipotle file.

..4. Which burrito is more popular, steak or chicken?

'''Command Line
cut -f3 chipotle.tsv | sort | uniq -c | sort | grep -e 'Chicken Burrito' -e 'Steak Burrito'
'''

[Using Kevin's video] (https://www.youtube.com/watch?v=jq5kt_0VDgQ), I have cut out the item_name column. Then, I sorted it so that I can get all the unique values of each item and count it. I sort that one again just for aesthetic purposes (it's good in my eyes to see ascending or descending order and you can easily find the max and min) and search for patterns matching Chicken Burrito and Steak Burrito. The -e argument in grep allows you to search for multiple patterns.

[For Grep Argument with e](http://unix.stackexchange.com/questions/25821/grep-how-to-add-an-or-condition)

The results come out like the following:
**  368 Steak Burrito **
**  553 Chicken Burrito **

The answer is that ** Chicken Burrito ** is more popular.

..5. Do chicken burritos more often have black beans or pinto beans?

Essentially, we want to know the number of chicken burritos that have black beans or pinto beans. For this, I am unable to utilize regular expression to find an "AND" case to match both word patterns that I may need to match.

'''Command Line 1
cut -f3,4 chipotle.tsv | ack 'Chicken Burrito' | ack 'Black Beans' | wc -l
     282
'''

I first cut out the columns I am concerned with and parsed out the lines with Chicken Burito. Then, I parsed out the lines with Black beans then, I did a line count.

For Black Beans, it looks like we have 282 Chicken Burritos that contain it.

'''Command Line 2
cut -f3,4 chipotle.tsv | ack 'Chicken Burrito' | ack 'Pinto Beans' | wc -l
     105
'''
It's the same process for the Pinto Beans. 
I have 105 Pinto Beans Chicken Burrito. It's obvious that Black Beans are more popular of the two.

..6.Make a list of all of the CSV or TSV files in the DAT8 repo (using a single command). Think about how wildcard characters can help you with this task.

'''Command Line 1
find . -name *.csv -o -name *.tsv
'''

We want to find all the files in DAT8 that has *.csv* and *.tsv.*
The way to go is to catch both patterns with an OR case which you use *-o* for.
*\*.csv* and *\*.tsv* with the \* matches for any file ending with *.csv* and *.tsv*


..7. Count the approximate number of occurrences of the word "dictionary" (regardless of case) across all files in the DAT8 repo.

'''Command Line 1
ack -r -i 'dictionary' . | wc -l
'''

Using *ack -r* I am able to recursively search through the entire directory. When I apply *-i*, I am able to ignore upper or lower cases of my pattern. Then, I piped it through to *wc* to count the number of *lines* as the output specifies the line that contains the pattern.
The answer is 15.












