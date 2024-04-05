class LUPrefix:

    def __init__(self, n: int):
        self.i = 0
        self.j = [0]*(n+1)
        self.n = n

    def upload(self, video: int) -> None:
        if video==1:
            self.i = 1
        self.j[video]=1
        while(self.i<self.n):
            if self.j[self.i+1]==1:
                self.i+=1
            else:
                break
    def longest(self) -> int:
        return self.i