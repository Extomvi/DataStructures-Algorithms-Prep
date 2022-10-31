"""
Designing a leaderboard
"""
# Time complexity of O(nlogK)
class Leaderboard:

    def __init__(self):
        self.scores = {}
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = 0
        self.scores[playerId] += score
        

    def top(self, K: int) -> int:
        print(self.scores)
        heap = []
        for val in self.scores.values():
            heapq.heappush(heap, val)
            # print(heap)
            if len(heap) > K:
                heapq.heappop(heap) #remove from the head of the heap -> the smallest value in the heap
        # print(heap)
        top = 0
        for i in heap:
            top += i
        return top
        

    def reset(self, playerId: int) -> None:
        del self.scores[playerId]

# Time complexity of O(nlogn)
class Leaderboard:

    def __init__(self):
        self.scores = {}
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = 0
        self.scores[playerId] += score
        

    def top(self, K: int) -> int:
        values = [value for key, value in sorted(self.scores.items(), key=lambda X: X[1])]
        values.sort(reverse = True)
        total = 0
        for i in values[:K]:
            total += i
        return total
            
        

    def reset(self, playerId: int) -> None:
        del self.scores[playerId]
    