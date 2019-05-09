#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
handle = open(fname)

answer=dict()
for line in handle:
    if line.startswith("From:"):
        continue 
    if line.startswith("From"):
        templine=line.split()
        date=templine[5]
        date=date.split(":")
        hour=date[0]
        answer[hour]=answer.get(hour,0)+1

for k,v in (sorted([(k,v) for k,v in answer.items()])):
    print(k,v)
