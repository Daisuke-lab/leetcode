class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # you want to take an action when some cars meet
        # I want to make a for loop with miles range(target+1) => Really?
        # for loop with time would be better.
        # After 1 hour, you add speed to position. if car reaches target in the same hour
        # If the order of cars change, you want to change the speed of faster car
        # You have to keep track of the order, which is not efficient.
        # 0. make a hashmap {position: speed}
        # 1. you can sort first (descending)
        # 2. add speed
        # 3. if it's less than or equal to right side, change the right side speed
        # 4. create a hashmap everytime in for loop
        
        # you need count

        stack = []
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        for pos, speed in cars:
            time = (target - pos) / speed
            if len(stack) == 0 or stack[-1] < time:
                stack.append(time)
        return len(stack) 
        
        