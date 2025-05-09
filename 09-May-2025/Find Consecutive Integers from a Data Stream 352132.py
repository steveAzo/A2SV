# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.count = 0
        self.k = k
        self.value = value
        

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num == self.value:
            self.count += 1

        while len(self.queue) > self.k:
            popped_val = self.queue.popleft()
            if popped_val == self.value:
                self.count -= 1
        
        return self.k == self.count
            

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)