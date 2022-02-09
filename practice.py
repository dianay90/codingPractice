


from matplotlib.container import StemContainer


def reverse_string(str):
    reversed = ''
    for c in str: 
        reversed = c + reversed
    return reversed

def reverse_string2(str):
    #str= str.split('')
    stringlist = list(str)
    stringlist.reverse()
    return str 

def palindrome(str):
    reversed = str[::-1]
    return str == reversed

def reverseInt(integer):
    string = str(integer)
    string = list(string)
    string.reverse()

    joined= "".join(string)
    
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
        if charMap[char] >1:
            max = charMap[char]
            maxChar = char

    return max
def chunk_array(array,size):

    chunked = list() 
    for item in array: 
        last = list()

        if not last or last.length == size:
            chunked.append(item)
        else: 
            last.append(item)
    return chunked
def chunk_array2(array,size):
    chunked = list()
    last = list() 

    for item in array:
        
        if len(chunked)!= size: 
            chunked.append(item)
        else: 
            last = chunked(len(chunked) - 1)
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
    string1List = sorted(str1)
    string2List= sorted(str2)

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


fibonacci_iterative(4)
steps(4)

string1 = "dog"
string2 = "godd"

count = vowels(string1)
print(count)

#value  = anagrams_version1(string1, string2)
#print(value)

value  = anagrams_version2(string1, string2)
print(value)

array = [1,2,3,4,5]
print("array prints")
print(array[0:2])
size = 2
#chunk_array3(array,size)
str = "elephaaaante"
max = maxCharsInString(str)

num = 300
#revserdnum = reverseInt(num)



string = "cat"
string_reverse = reverse_string(string)
print(string_reverse)

string = "dog"
result = palindrome(string)






print('')