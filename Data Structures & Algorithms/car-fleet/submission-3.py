class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        result = []
        hours = []
        fleet = 0
        mapping = {}
        position_set = set(position)

        position_set = sorted(position_set, reverse=True)

        for i, value in enumerate(position):
            mapping[value] = speed[i]


        for i, value in enumerate(position_set):
            hours.append((target-value)/mapping[value])


        for value in hours:           
            while result and (result[-1] < value):
                result.pop()

            if not result:
                result.append(value)
                fleet += 1

            else:
                result.append(value)

        return fleet
        

        