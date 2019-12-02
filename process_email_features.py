import os

file = open("dictionary.txt", mode='r')
dictlist = [None]*250
for i in range(250):
    dictin = file.readline()
    cutoff = 0
    for j in dictin:
        if(j=='['):
            break;
        cutoff+=1
    dictlist[i] = (dictin[0:cutoff], int(dictin[cutoff+1:len(dictin)-2]))
    #print("%d " + dictlist[i][0] + "[%d]" %(i, dictlist[i][1]))
    print("{}. {} [{}]".format(i, dictlist[i][0], dictlist[i][1]))
file.close()

trfeat_List = [None]*100
tefeat_List = [None]*260

trfeat = open("train-features.txt", mode='w+')
trlabe = open("train-labels.txt", mode='w+')

tefeat = open("test-features.txt", mode='w+')
telabe = open("test-labels.txt", mode='w+')

nstr = os.listdir("data/nonspam-train")
sptr = os.listdir("data/spam-train")

nste = os.listdir("data/nonspam-test")
spte = os.listdir("data/spam-test")

#print(len(dictlist))
emindx = 0
for i in nstr:
    trlabe.write("0\n")
    file = open(r"data/nonspam-train/" + i, mode = 'r')
    email = file.read().split(" ")
    #wdindx = 0
    for j in range(len(dictlist)):
        wc=0
        for k in email:
            if(dictlist[j][0] != None): 
                if(dictlist[j][0] == k): wc+=1
        if(wc>0): trfeat.write("%d %d %d\n" %(emindx, j, wc))
        #wdindx += 1
    emindx += 1
    if(emindx == 50): break;
    
for i in sptr:
    trlabe.write("1\n")
    file = open(r"data/spam-train/" + i, mode = 'r')
    email = file.read().split(" ")
    #wdindx = 0
    for j in range(len(dictlist)):
        wc=0
        for k in email:
            if(dictlist[j][0] != None): 
                if(dictlist[j][0] == k): wc+=1
        if(wc>0): trfeat.write("%d %d %d\n" %(emindx, j, wc))
        #wdindx += 1
    emindx += 1    
    if(emindx == 100): break;
#################################################################################
emindx = 0
for i in nste:
    telabe.write("0\n")
    file = open(r"data/nonspam-test/" + i, mode = 'r')
    email = file.read().split(" ")
    for j in range(len(dictlist)):
        wc=0
        for k in email:
            if(dictlist[j][0] != None): 
                if(dictlist[j][0] == k): wc+=1
        if(wc>0): tefeat.write("%d %d %d\n" %(emindx, j, wc))
        #wdindx += 1
    emindx += 1   

for i in spte:
    telabe.write("1\n")
    file = open(r"data/spam-test/" + i, mode = 'r')
    email = file.read().split(" ")
    for j in range(len(dictlist)):
        wc=0
        for k in email:
            if(dictlist[j][0] != None): 
                if(dictlist[j][0] == k): wc+=1
        if(wc>0): tefeat.write("%d %d %d\n" %(emindx, j, wc))
    emindx += 1   
