class RecentCounter:

    def __init__(self):

        self.q = [] 
        self.i = 0 
        self.j = 0
        

    def ping(self, t: int) -> int:

        self.q.append(t)
        self.j += 1
        while self.q[self.i] < t - 3000 :
            self.i += 1
        return self.j - self.i 

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)