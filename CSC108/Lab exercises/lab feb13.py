names = ['Bob', 'Ho' , 'Zahara' , ' Amitabha' , 'Dov' , ' Maria']
print names[2:5]
print names[2]
print names[3:]

#2  list.remove(value)

#3
listthree = ["i am well"]
listthree.insert(0, 'How are you?')
print listthree

#4
listfour = [2, 4, 99, 0, -3.5, 86.9, -101]
listfour.sort()
listfour.reverse()
print listfour

#5
def every_third(list):
    listfive = []
    index = 0
    while index < len(list) :
        listfive.append(list[index])
        index += 3
    print listfive
#6
def every_ith(list, i):
    listsix = []
    index = 0
    while index < len(list):
        listsix.append(list[i])
        index +=1
    print listsix

#while loops

def print_list(list):
    index = 0
    while index < len(list):
        print list[index]
        index += 1

def print_list_even(list):
    index = 0
    while index < len(list):
        print list[index]
        index += 2

def print_list_reverse(list):
    index = len(list) - 1
    while index >= 0:
        print list[index]
        index -= 1

def sum_elements(list):
    sum = 0
    index = 0
    while (sum <=100) and (index < len(list)):
        sum = sum + list[index]
        index += 1
    print sum

def duplicates(list):
    index  = 0
    index2 = 1
    while index < len(list) and index2 <len(list):
        if list[index] == list[index2]:
            return True
        index  += 1
        index2 += 1
    return False


#nested lists

pets = [['shoji', 'cat', 18],['hanako', 'dog', 15],['sir toby', 'cat', 10],['sachiko', 'cat', 7],['sasha', 'dog', 3],['lopez', 'dog', 13]]

#1
for x in pets:
    print x[:]
    
#2
for x in pets:
    print x[1]
#3
numberofdogs = 0
for x in pets:
    for y in x:
        if y == 'dog':
            numberofdogs += 1
print numberofdogs

#4
totalage = 0
for x in pets:
    totalage += x[2]
print totalage

#5
def nested_lengths(list):
    totlist = []
    for x in list:
        totlist.append(len(x))
    return totlist
        
        
if __name__ == "__main__":
    l = [0,1,1,3,4,5,6,7]
    ll=[[1,2,3],[4,5,6],[7,8,9],[10,11,235,12]]