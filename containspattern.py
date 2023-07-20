from typing import List

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr) - m):
            pattern_match = arr[i:(i+m+1)]
            print("looking for pattern:", pattern_match)
            for j in range(i+m, len(arr),m):
                candidate = arr[j:(j+m+1)]
                print("\tcandidate", candidate)


        return True


#arr = [1,2,4,4,4,4]
#m = 1
#k = 3

arr = [1,2,1,2,1,3]
m = 2
k = 3
s = Solution()
print(s.containsPattern(arr, m, k))
