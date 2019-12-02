import os

allwords = "";

#Load and concatenate all the emails in one string
#Files=dir('data/*/*.txt');
nste = os.listdir("data/nonspam-test")
spte = os.listdir("data/spam-test")
nstr = os.listdir("data/nonspam-train")
sptr = os.listdir("data/spam-train")
for i in nste:
    #print(i)
    file = open(r"data/nonspam-test/" + i, mode = 'r')
    allwords = allwords + file.read()
    file.close()

for i in spte:
    #print(i)
    file = open(r"data/spam-test/" + i, mode = 'r')
    allwords = allwords + file.read()
    file.close()


for i in nstr:
    #print(i)
    file = open(r"data/nonspam-train/" + i, mode = 'r')
    allwords = allwords + file.read()
    file.close()
    
    
for i in sptr:
    #print(i)
    file = open(r"data/spam-train/" + i, mode = 'r')
    allwords = allwords + file.read()
    file.close()
    
#print(allwords) #allwords is waaaay to long to print
words = allwords.split(" ")
dictionary = list(dict.fromkeys(words))
dlen = len(dictionary)
counts = [None]*dlen
counter = 0
counting = 0   # I am so good at naming variables
#I HOPE TO GOD THIS WORKS THE FIRST TIME
#I FORGOT TO SORT THEM HAHAHAHAHAHAHAHAHA
while(counter < dlen):
    for i in words:
        if(len(i)>1):
            if(i == dictionary[counter]):
                counting += 1
    print(dlen-counter)
    counts[counter] = counting  #I take it all back I am terrible at naming variables
    
    counting = 0
    counter += 1

#quickSort(counts, dictionary, 0, dlen-1)
for i in range(dlen): 
      
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, dlen): 
        if counts[min_idx] > counts[j]: 
            min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
    counts[i], counts[min_idx] = counts[min_idx], counts[i] 
    dictionary[i], dictionary[min_idx] = dictionary[min_idx], dictionary[i]

file = open("dictionary.txt", mode='w+')

for i in range(dlen-1, 0, -1):
    file.write(dictionary[i] + "[%d]\n" %counts[i])

file.close();
