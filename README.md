# about-tuple-list

## After converting the dictionary, add duplicate values ​​and convert back to tuple
## Change the tuple to a list and put the rank value, then change it back to the tuple and put it in rankedList
   curRank: current ranking, jointRank: joint rank number, sale: Sales based on current
   start with the second index
   If the sales are the same, the Rank remains the same, but jointRank increases by 1.
   If the value is smaller, add jointRank+1 to curRank
