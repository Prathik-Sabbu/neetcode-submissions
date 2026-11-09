class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if (i == '/'):
                second = stack.pop()
                first = stack.pop()
                first = int(first / second)
                stack.append(first)
            elif (i == '+'):
                second = stack.pop()
                first = stack.pop()
                first += second
                stack.append(first)
            elif (i == '-'):
                second = stack.pop()
                first = stack.pop()
                first -= second
                stack.append(first)
            elif (i == '*'):
                second = stack.pop()
                first = stack.pop()
                first *= second
                stack.append(first)
            else:
                stack.append(int(i))
        return int(stack.pop())
            