class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0]*len(temperatures)
        print(len(temperatures) - 1)
        actual_value_stack = []
        idex_value_stack = []
        count = 0

        for i, value in enumerate(temperatures):
            count += 1
            if not actual_value_stack:
                actual_value_stack.append(value)
                idex_value_stack.append(i)
            
            while actual_value_stack and (actual_value_stack[-1] < value):
                temp = actual_value_stack.pop()
                index = idex_value_stack.pop()
                result[index] = count - index - 1

            actual_value_stack.append(value)
            idex_value_stack.append(i)

        return result
