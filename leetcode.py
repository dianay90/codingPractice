import llist
from llist import sllist,sllistnode
from collections import deque

class Solution:
    class Solution:
    def groupAnagrams(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
    def search(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target: #if the middle point equals the target
                return mid
            elif nums[mid] >= nums[start]: #if the middle points is greater than or equal to the start 
                if target >= nums[start] and target < nums[mid]:#the target is great than start and target is before middle point, search first half
                    end = mid - 1
                else:
                    start = mid + 1 #if that's not true search second half
            else:
                if target <= nums[end] and target > nums[mid]: #if target less than nums end and greater than the mid
                    start = mid + 1 #search last half
                else:
                    end = mid - 1 #search front half
        return -1
    
    def search_diana(self, nums, target):

        start,end =0, len(nums)-1 
        while start <= end: 
            mid = start + (end-start) //2

            if nums[mid] == target: 
                return mid
            elif nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid -1
                else: 
                    start = mid + 1

            else: 
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1 
                else: 
                    end = mid -1 
            return -1 

    def subsets(self, nums):
        n = len(nums)
        output = [[]]
        
        for num in nums:
            #output += [curr + [num] for curr in output]
            for curr in output:
                output = output + [curr + [num]]

        return output
    def subsets2(self, nums):
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
            
            #for curr in output:
             #   output = output + [curr + [num]]
        return output

    def levelOrderBottom(self, root):
        levels = []
        next_level = deque([root])
        
        while root and next_level:
            curr_level = next_level
            next_level = deque()
            levels.append([])
            
            for node in curr_level:
                # append the current node value
                levels[-1].append(node.val)
                # process child nodes for the next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                    
        return levels[::-1]


    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        
        level = 0
        queue = deque([root,])
        while queue:
            # start the current level
            levels.append([])
            # number of elements in the current level 
            level_length = len(queue)
            
            for i in range(level_length):
                # this is kinda like a standard pop
                node = queue.popleft()
                # fulfill the current level
                levels[level].append(node.val)
                
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # go to next level
            level += 1
        
        return levels

    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack

    def longestCommonPrefix(self, strs):
        prefix=""
        if len(strs)==0: return prefix
        
        for i in range(len(min(strs))):
            c=strs[0][i]
            if all(a[i]==c for a in strs):
                prefix+=c
            else:
                break
        return prefix

    def generateParenthesis(self, n):
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans

    def canAttendMeeting(self, intervals):
        intervals.sort()

        for i in range(0,len(intervals) -2 ):
            if intervals[i][-1] < intervals[i+1][0]:
                continue
            else:
                return False
        return True

    def intervalIntersection(self, A,B):

        ans = []
        i = j = 0

        while i < len(A) and j < len(B):
            # Let's check if A[i] intersects B[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                ans.append([lo, hi])

            # Remove the interval with the smallest endpoint
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ans
   
    def insert(self, intervals, newInterval):
        # init data
        new_start, new_end = newInterval
        idx, n = 0, len(intervals)
        output = []
        
        # add all intervals starting before newInterval
        while idx < n and new_start > intervals[idx][0]:
            output.append(intervals[idx])
            idx += 1
            
        # add newInterval
        # if there is no overlap, just add the interval
        if not output or output[-1][1] < new_start:
            output.append(newInterval)
        # if there is an overlap, merge with the last interval
        else:
            output[-1][1] = max(output[-1][1], new_end)
        
        # add next intervals, merge with newInterval if needed
        while idx < n:
            interval = intervals[idx]
            start, end = interval
            idx += 1
            # if there is no overlap, just add an interval
            if output[-1][1] < start:
                output.append(interval)
            # if there is an overlap, merge with the last interval
            else:
                output[-1][1] = max(output[-1][1], end)
        return output
    def removeDuplicates(self, nums):
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

    '''
    int maxarea=0, l= 0, r = height.length -1
    while (l<r):
        maxarea = Math.max(maxarea, Math.min(height[l],height[r]) * (r-1))
        if height[l] <height [r]
        l++ 
        else 
        r--

    return maxarea
    
    
    '''

    def lengthOfLongestSubstring(self, s):
            chars = [0] * 128

            left = right = 0

            res = 0
            while right < len(s):
                r = s[right]
                chars[ord(r)] += 1

                while chars[ord(r)] > 1:
                    l = s[left]
                    chars[ord(l)] -= 1
                    left += 1

                res = max(res, right - left + 1)

                right += 1
            return res

    def merge(self, intervals):

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
    def searchRange(self, nums, target):
        
        lower_bound = self.findBound(nums, target, True)
        if (lower_bound == -1):
            return [-1, -1]
        
        upper_bound = self.findBound(nums, target, False)
        
        return [lower_bound, upper_bound]
        
    def findBound(self, nums, target, isFirst: bool):
        
        N = len(nums)
        begin, end = 0, N - 1
        while begin <= end:
            mid = int((begin + end) / 2)    
            
            if nums[mid] == target:
                
                if isFirst:
                    # This means we found our lower bound.
                    if mid == begin or nums[mid - 1] < target:
                        return mid

                    # Search on the left side for the bound.
                    end = mid - 1
                else:
                    
                    # This means we found our upper bound.
                    if mid == end or nums[mid + 1] > target:
                        return mid
                    
                    # Search on the right side for the bound.
                    begin = mid + 1
            
            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1
        
        return -1
    def find_averages_of_subarrays(self, K, array):
        sum = 0
        listOfAverage = list()
        for i in range(len(array)):
            if i+K < len(array):
                for i in range(i,i+K):
                    #sum 
                    sum = sum + array[i]
                average = sum/K 
                listOfAverage.append(average)
                average = 0
                sum =0
            else:
                
                print(listOfAverage) 



#One away 

    def _replace(self, stringOne, stringTwo):
        difference = 0 
        #sortedStringOne= ''.join(sorted(stringOne))
        #sortedStringTwo= ''.join(sorted(stringTwo))
        for i in range(len(stringOne)):
            if stringOne[i] != stringTwo[i]:
                difference = difference + 1 
                if difference > 1: 
                    return False
        return True



    def _insert_and_remove(self, stringOne, stringTwo):
        differences = 0 

        sortedStringOne= ''.join(sorted(stringOne))
        sortedStringTwo= ''.join(sorted(stringTwo))

        if len(sortedStringOne) > len(sortedStringTwo):
            for i in range(len(sortedStringOne)):
                if differences >=1: 
                    if sortedStringOne[i] != sortedStringTwo[i-1]:
                        return False

                if sortedStringOne[i] != sortedStringTwo[i]:
                    # if they're not equal and sortedStrongOne is longer...
                        
                    differences = differences +1
                    


        else: 
             for i in range(len(sortedStringTwo)):
                if differences >=1: 
                    if sortedStringTwo[i] != sortedStringOne[i-1]:
                        return False
                    else:
                        continue

                if sortedStringTwo[i] != sortedStringOne[i]:
                    # if they're not equal and sortedStrongOne is longer...
                        
                    differences = differences +1
        return True

    def oneAway(self, stringOne, stringTwo):
        lengthStringOne = len(stringOne)
        lengthStringTwo = len(stringTwo)

        if abs(lengthStringOne-lengthStringTwo)>=2:
            return False
        else:
            # Length only varies by 1 
            if abs(lengthStringOne-lengthStringTwo)==1:
                value = self._insert_and_remove(stringOne,stringTwo)
                print(value)
                if value:
                    print("can insert or remove")
                else: 
                    print("NO - cannot insert or remove")
            else: 
                value = self._replace(stringOne, stringTwo)
                print(value)
                if value: 
                    print("can replace")
                else: 
                    print("NO- cannot replace")


            print("woof")

        
# Two Sums 
    def twoSum(self, nums, target):
        # array of integers num 
        # integer target 
        #return indices of the two numbers such that they add up to target
        
        targetList = list()
                            
        for i in nums: 
            print(i)
            otherHalf = target - i
            if otherHalf in nums: 
                returnList = list()
                returnList.append(nums.index(i))
                returnList.append(nums.index(otherHalf))
                return returnList
        # return a list of ints 


    def addTwoNumbers(self, list1, list2):

        arrayOne = list() 
        arrayTwo = list() 
        
        while list1.size > 0: 
            arrayOne.append(list1.pop())
        while list2.size > 0: 
            arrayTwo.append(list2.pop())

        strings = [str(integer) for integer in arrayOne]
        a_string = "".join(strings)
        an_integerOne = int(a_string)

        strings = [str(integer) for integer in arrayTwo]
        a_string = "".join(strings)
        an_integerTwo = int(a_string)

        sum = an_integerOne + an_integerTwo
        sum = str(sum)
        list3 = sllist([])
        for x in sum:   
            list3.append(x)


        return list3
#RUFF
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

blue = Solution()

nums = [4,5,6,7,0,1,2]
target = 2
searchReturn = blue.search(nums,target)

nums = [1,2,3]
first_set = blue.subsets(nums)
second_set = blue.subsets2(nums)
root =  TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


blue.levelOrderBottom(root)

#root = [3,9,20,None,None,15,7]
treeLevel = blue.levelOrder(root)


s = "()[]{}"
stack = blue.isValid(s)
print(stack)

strs = ["flower","flow","flight"]

blue.longestCommonPrefix(strs)

blue.generateParenthesis(3)



#firstList = [[0,2],[5,10],[13,23],[24,25]]
#secondList = [[1,5],[8,12],[15,24],[25,26]]

intervals = [[7,10],[2,4]]
blue.canAttendMeeting(intervals)
firstList = [[0,0],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
blue.intervalIntersection(firstList, secondList)

intervals = [[1,3],[6,9]]
newInterval = [2,5]

interval = blue.insert(intervals, newInterval)
print(interval)


nums = [1,1,2]
blue.removeDuplicates(nums)
s = "abcabcbb"
blue.lengthOfLongestSubstring(s)
intervals = [[1,3],[8,10],[15,18],[2,6]]
blue.merge(intervals)

nums = [5,7,7,7,7,8,8,8,10]
target = 8
blue.searchRange(nums,target)

result = blue.find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])

string1 = "pale"

string2 = "ple"

print(string1)
print(string2)

#blue.oneAway(string1,string2)

lst1 = sllist([9,9,9,9,9,9,9])
lst2 = sllist([9,9,9,9])

fullList= blue.addTwoNumbers(lst1,lst2)
print(fullList)
#Two sums 

print("hey")


nums = [2,7,11,15]


target = 9
returnedList = blue.twoSum(nums, target)
print(returnedList)


