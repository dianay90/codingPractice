



def reverseInt(num):

    string2 = str(num)
    string2 = list(string2)
    string2.reverse()

    joined= "".join(string2)
    
    string_to_int = int(joined)

    return string_to_int

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

grouped = group_anagrams_diana(strs)
num = 10 
blue  = str(num)

print(type(blue))

reversedInt= reverseInt(num)

print('')

dict1= {"dog": 1, "cat":2}
dict2= {"dog": 2, "cat":2}


print(dict1 == dict2)
print("")