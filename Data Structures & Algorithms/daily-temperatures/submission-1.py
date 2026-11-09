class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0]*len(temperatures)
        print(len(temperatures) - 1)
        actual_value_stack = []
        idex_value_stack = []

        for i, value in enumerate(temperatures):
            if not idex_value_stack:
                idex_value_stack.append(i)
            
            while idex_value_stack and (temperatures[idex_value_stack[-1]] < value):
                index = idex_value_stack.pop()
                result[index] = i - index

            idex_value_stack.append(i)

        return result
