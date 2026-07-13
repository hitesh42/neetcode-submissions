class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        # stack.append(tokens[0])
        for s in tokens:
            temp = s
            if s == "+":
                temp = int(stack.pop()) + int(stack.pop())
            elif s == "-":
                temp = -(int(stack.pop()) - int(stack.pop()))
            elif s == "*":
                temp = int(stack.pop())*int(stack.pop())
            elif s == "/":
                first = stack.pop()
                second = stack.pop()
                print(second)
                if int(second)==0:
                    print("here")
                    temp = 0
                else:
                    temp = 1/((int(first)/int(second)))
            stack.append(temp)
            print(stack)

            # stack.append(s)
            # if stack[-1] == "+":
            #     stack.pop()
            #     temp = stack[-1]+s

            # if s="+"
        # print(stack)
        res = int(stack.pop())
        return res