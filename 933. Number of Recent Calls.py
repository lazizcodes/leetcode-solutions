from collections import deque

class RecentCounter:

    def __init__(self):
        self.recent = deque()

    def ping(self, t: int) -> int:
        self.recent.append(t)
        while (self.recent) and (self.recent[0] < t - 3000):
            self.recent.popleft()
        return len(self.recent)