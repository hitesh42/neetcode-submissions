class MinStack:

    def __init__(self):
        self._stack = deque()
        self._minPrefixStack = deque() 

    def push(self, val: int) -> None:
        self._stack.append(val)
        if len(self._minPrefixStack)>0:
            self._minPrefixStack.append(min(self._stack[-1],val, self._minPrefixStack[-1]))
        else:
            self._minPrefixStack.append(min(self._stack[-1],val))

    def pop(self) -> None:
        self._stack.pop()
        self._minPrefixStack.pop()

    def top(self) -> int:
        return self._stack[-1]
        

    def getMin(self) -> int:
        return self._minPrefixStack[-1]
        
