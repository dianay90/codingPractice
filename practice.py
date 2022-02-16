
from collections import defaultdict
import collections
from re import L

'''
THREE WAYS TO REVERSE

'''
def reverse_string(string):
    reversed = ''
    for c in string: 
        reversed = c + reversed
    return reversed

def reverse_string2(string):
    #str= str.split('')
    '''
    Turn string into list so you can you use the reverse property
    turn it back into a string by doing ' ' . join(stringlist)
    
    '''
    stringlist = list(string)
    stringlist.reverse()
    new_string = ''.join(stringlist)
    return new_string 

def palindrome(string):
    #Another way to reverse  
    reversed = string[::-1]
    return string == reversed

def reverseInt(num):
    '''
    you can case an int as a string and then
    once you have a string cast that as a list... turn it into a list
    reverse it 

    then turn a list back into a string by doing "".join(string)
    
    '''
    string2 = str(num)
    string2 = list(string2)
    string2.reverse()

    joined= "".join(string2)
    
    string_to_int = int(joined)

    return string_to_int


def maxCharsInString(str):
    max = 0
    charMap =dict()

    for char in str:  
        if char in charMap:
            charMap[char] +=1
        else:
            charMap[char] =1
    for char in charMap: 
        if charMap[char] >max:
            max = charMap[char]

    return max

'''
def chunk_array(array,size):
    chunked = list() 
    for item in array: 
        last = list()

        if not last or last.length == size:
            chunked.append(item)
        else: 
            last.append(item)
    return chunked

'''
def chunk_array2(array,size):
    chunked = list()
    last = list() 

    for item in array:
        if len(chunked)!= size: 
            chunked.append(item)
        else: 
            #last = chunked[len(chunked) - 1]
            last.append(chunked)
            #chunked.clear()
    return last

def chunk_array3(array,size):

    chunked_list = list()
    chunk_size = size
    for i in range(0, len(array), chunk_size):
        chunked_list.append(array[i:i+chunk_size])
    print(chunked_list)

def chunk_array4(array,size):
    chunked_list = list() 
    chunk_size= size
    for i in range(0,len(array), chunk_size):
        chunked_list.append(array[i:i+chunk_size])
    print(chunked_list)

def put_in_char_map(string):
    charMap = dict()
    for c in string: 
        if c not in charMap: 
            charMap[c] = 1
        else: 
            charMap[c] +=1
    return charMap 

def anagrams_version1(str1, str2): #hashmap 
    charmapA = put_in_char_map(str1)
    charmapB = put_in_char_map(str2)

    if len(charmapA) != len(charmapB):
        return False 
    for key in charmapA: 
        if key in charmapB: 
            if charmapA[key] != charmapB[key]:
                return False 
        else: 
            return False 
    return True

def anagrams_version2(str1, str2):
    print()
    '''
    Use sorted on the strings because the strings are not lists
    
    '''
    string1List = sorted(str1)
    string2List= sorted(str2)

    #turn them back into strings
    string1 = ''.join(string1List)
    string2 = ''.join(string2List)


    if string1 == string2: 
        return True 

    return False 


def steps(n):
    row = n 
    column = n
    stair = ''

    for r in range(0,row): 
        stair += '\n'

        for c in range(0,column): 
            if c <= r: 
                stair += '#'
            else: 
                stair += ' '
    print(stair)

def vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowelCount = 0
    for char in string:
        if char in vowels:
            vowelCount +=1
    return vowelCount


def fibonacci_iterative(n):
    fib_list= list()
    fib_list = [0] * (n+1)
    for i in range(0,n+1):
        if i == 0:
            fib_list[i] = 0
        elif i ==1:
            fib_list[i] = 1
        else:
            fib_list[i] = fib_list[i-1] + fib_list[i-2]
    print(fib_list)
    return fib_list[n]

def two_sum( nums, target):
    
    hashmap = dict()
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return[i,hashmap[complement]]
        hashmap[nums[i]] =i 
'''
def group_anagrams(strs):
    ans = collections.defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return ans.values()
'''

#Sort the string and return a tuple and append to a dictionary 
#GROUP ANAGRAMS 
def group_anagrams_diana(strs):
    ans= dict()
    for s in strs: 
        sorted_string_tuple = tuple(sorted(s))
        if sorted_string_tuple in ans: 
            ans[sorted_string_tuple].append(s)
        else: 
            ans[sorted_string_tuple] = [s]
    return ans.values 
strs = ["eat","tea","tan","ate","nat","bat"]

'''
removeElement(int[] nums, int val) {
    int i = 0;
    int n = nums.length;
    while (i < n) {
        if (nums[i] == val) {
            nums[i] = nums[n - 1];
            // reduce array size by one
            n--;
        } else {
            i++;
        }
    }
    return n;
}
'''

def remove_element(nums, val):
    n = len(nums)
    for i in range(0,len(nums)):
        if nums[i] == val: 
            nums[i] = nums[n-1]
        else: 
            continue
    return nums 

def removeDuplicates( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    len_ = 1
    if len(nums)==0:
        return 0
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[len_] = nums[i]
            len_ +=1
    return len_

def remove_duplicates_v2(nums):

    slow_length = 1
    if len(nums) == 0: 
        return 0 
    for i in range(0,len(nums)-1):
        if nums[i]!= nums[i+1]:
            nums[slow_length] = nums[i+1]
            slow_length +=1
    return slow_length

#binary search 

def searchInsert( nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return left

def searchInsertv2(nums, target):
    left, right = 0, lens(nums) -1 
    while left <=right: 
        pivot = (left+right) //2
        if nums[pivot] == target:
            return pivot
        if target < nums[pivot]:
            right = pivot -1 
        else: 
            left= pivot + 1 
    return left 

def majority_element(nums):
    nums_holder = dict() 
   
    threshold = len(nums)/2
    for x in nums: 
        if x not in nums_holder: 
            nums_holder[x] = 1
        else: 
            nums_holder[x] +=1
            if nums_holder[x] > threshold: 
                return x
    return None 
    
def majority_elementv2(nums):
    nums_holder = dict()
    
    max = 0
    majority_element = 0 
    threshold = len(nums)/2
    for x in nums: 
        if x not in nums_holder: 
            nums_holder[x] = 1
        else: 
            nums_holder[x] +=1
            if nums_holder[x] > max: 
                max = nums_holder[x] 
                majority_element = x
    return majority_element

def two_sumv2(nums, target): #kind
    sum_dictionary = dict() 
    # will store value, index
    
    for x in nums: 
        complement = target - x
        if complement in sum_dictionary: 
            return[sum_dictionary[complement],nums.index(x)]
    
        else: 
            sum_dictionary[x]= nums.index(x)

    return None 
def two_anagrams_same_hash(string1, string2):
    char_map_string1 = dict()
    char_map_string2 = dict() 

    for x in string1:
        if x not in char_map_string1: 
            char_map_string1[x] = 1
        else: 
            char_map_string1[x] += 1
    
    for x in string2: 
        if x not in char_map_string2: 
            char_map_string2[x] =1
        else: 
            char_map_string2[x] +=1
    if len(char_map_string1) != len(char_map_string2): 
        return False
    
    return char_map_string2 == char_map_string1
string1= "dol"
string2= "god"

value = two_anagrams_same_hash(string1, string2)
nums = [3,1,2,4,3]
target = 7
value1 = two_sumv2(nums,target)

value2 = two_sum(nums,target)


number = majority_elementv2(nums)
#number = majority_element(nums)
nums = [1,3,5,6]
target = 4
searchInsert(nums, target)

nums = [0,0,1,1,1,2,2,3,3,4]
#output= removeDuplicates(nums)
output = remove_duplicates_v2(nums)
#values= group_anagrams(strs)

nums = [3,2,2,3]
val = 3
remove_element(nums, val)
values = group_anagrams_diana(strs)


fibonacci_iterative(4)
steps(4)

string1 = "dog"
string2 = "godd"

reversed = reverse_string(string1)
reversed2= reverse_string2(string2)
count = vowels(string1)
print(count)

#value  = anagrams_version1(string1, string2)
#print(value)

value  = anagrams_version2(string1, string2)
print(value)

array = [1,2,3,4,5]

chunked_array1= chunk_array3(array,3)

chunked_array2= chunk_array2(array,3)

print("array prints")

print(array[0:2])
size = 2

#chunk_array3(array,size)
string = "elepahhhhe"
max = maxCharsInString(string)

num = 300
reversed_num = reverseInt(num)


string = "cat"
string_reverse = reverse_string(string)
print(string_reverse)

string = "frog"
result = palindrome(string)

nums = [31,22,33,4,5]
target = 37

sum =two_sum(nums,target)


print('')


