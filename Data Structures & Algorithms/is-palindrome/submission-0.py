class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for c in s:
            
            if ("0"<=c <= "9") or ("a"<=c.lower()<="z"):
                # print(c.lower())
                temp+=c.lower()
        # print(temp)

        # print(temp[::-1])
        return temp==temp[::-1]
        