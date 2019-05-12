#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

f = input("Enter file:")
handle= open(f)
if len(f) < 1 : f = "mbox-short.txt"
list1=list()
dict1=dict()
for line in handle:
    if line.startswith("From:"):
        continue
    if line.startswith("From"):
        list1=line.split()
        dict1[list1[1]]=dict1.get(list1[1],0)+1
        
maxno=None
maxemail=None
        
for k,v in dict1.items():
    if maxno==None or maxno<v:
        maxno=v
        maxemail=k
        
print(maxemail,maxno) 
