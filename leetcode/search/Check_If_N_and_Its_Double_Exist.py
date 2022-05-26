class Solution:
    def checkIfExist(self, arr) -> bool:
        seen = ()
        for i in range(len(arr)):
            if arr[i] * 2 in seen or arr[i] % 2 == 0 and arr[i] // 2 in seen:
                return True
            seen[arr[i]] = i
            print(seen)
        return False


a = Solution()
a.checkIfExist(arr=[2, 3, 5, 7, 3, 5, 8, 9])
print(5 // 2)
