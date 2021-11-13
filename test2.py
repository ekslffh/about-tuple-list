# DATA AREA
data = [('apple', 5),('beer', 2),('pencil', 1),
        ('beer', 2),('book', 8),('apple', 9),
        ('paper', 3),('pencil', 13),('orange', 6)]

# SORT_SALES
# After converting the dictionary, add duplicate values ​​and convert back to tuple
salesRateDic = {}
for i,v in data:
    if i not in salesRateDic:
        salesRateDic[i]=v
    else:
        salesRateDic[i]+=v
salesRateTuple= list(salesRateDic.items())
salesRateTuple.sort(key=lambda x:x[1], reverse=True)
print(salesRateTuple)

# SALES_SUMMARY
# Change the tuple to a list and put the rank value, then change it back to the tuple and put it in rankedList
rankedList=[]
tempList=list(salesRateTuple[0])
tempList.append(1)
rankedList.append(tuple(tempList))
# curRank: current ranking, jointRank: joint rank number, sale: Sales based on current
curRank=1
jointRank=0
curSale=rankedList[0][1]
# start with the second index
for i in salesRateTuple[1:]:
    # If the sales are the same, the Rank remains the same, but jointRank increases by 1.
    if curSale==i[1]:
        jointRank+=1
    # If the value is smaller, add jointRank+1 to curRank
    else:
        curRank+=jointRank+1
        jointRank=0
    tempList=list(i)
    tempList.append(curRank)
    rankedList.append(tuple(tempList))

print(rankedList)