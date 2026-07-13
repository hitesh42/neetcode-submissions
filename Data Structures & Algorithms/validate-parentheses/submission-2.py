class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            # if (c=='{') or (c=='(') or (c=='['):
            if (len(stack)>0) and ((stack[-1]=='(' and c==')') or (stack[-1]=='[' and c==']') or (stack[-1]=='{' and c=='}')):
                stack.pop()
            else:
                stack.append(c)
            # print(stack[-1])
            
            # else:
            #     if len(stack):
            #         stack.pop()

        if not len(stack):
            return True
        else:
            return False