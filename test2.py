import json
import requests

 #//////////////TEST 1
def addup(List, K):
    for index,item in enumerate(List):
        if K - item in List[:index] + List[index+1:]:
            print (item)
    return False


X = [80, 98, 83, 92, 1, 38, 37, 54, 58, 89]
Y = 139

#print (addup(X,Y))
#////////////////////////////

#//////////////TEST 2
response = requests.get('https://mach-eight.uc.r.appspot.com/').json()
numbers = response['values']
target_number = 139

for i, number in enumerate(numbers[:-1]):  # note 1
    complementary = target_number - number
    if complementary in numbers[i+1:]:  # note 2
        print("Solution Found: {} and {}".format(number, complementary))
        break
else:  # note 3
    print("No solutions exist")

#/////////////////////////////

#////////////////////TEST 3

n = 181
n2 = n/2
numbers = [80, 98, 83, 92, 1, 38, 37, 54, 58, 89]
goodnums = {n-x for x in numbers if x<=n2} & {x for x in numbers if x>n2}
pairs = {(n-x, x) for x in goodnums}

#/////////////// TEST 4 ////////////////

#our two sum function which will return
#all pairs in the array that sum up to S
def twoSum(arr, S):

    sums = []
    hashTable = {}

        #check each element in array
    for i in arr:
    
        #alculate S - current element
        sumMinusElement = S - arr[i]

        #check if this number exists in hash table
        #if so then we found a pair of numbers that sum to S
        if not(hashTable[sumMinusElement]):
            sums.push([arr[i], sumMinusElement])
        

        #add the current number to the hash table
        hashTable[arr[i].toString()] = arr[i]


    #return all pairs of integers that sum to S
    return sums



twoSum([3, 5, 2, -4, 8, 11], 7)



