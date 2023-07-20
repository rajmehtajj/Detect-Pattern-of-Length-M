from typing import List

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        matches_found = 0
        for i in range(len(arr) - m):
            pattern = arr[i:(i+m)]
            print("looking for pattern:", pattern)
            for j in range(i+m, len(arr),m):
                candidate = arr[j:(j+m)]
                print("\tcandidate", candidate)

                if (candidate == pattern):
                    matches_found += 1
                    print("match found:", matches_found)
                    if matches_found == k:
                        return True
                else:
                    break


        return False


#arr = [1,2,4,4,4,4]
#m = 1
#k = 3

arr = [1,2,1,2,1,3]
#arr = [10,20,30,40,50,30,40,80,90]
m = 3
k = 2
s = Solution()
print(s.containsPattern(arr, m, k))
