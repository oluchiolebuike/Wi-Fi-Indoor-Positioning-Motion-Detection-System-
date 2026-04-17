class KalmanFilter1D:
    def __init__(self, q=0.1, r=1):
        self.q = q
        self.r = r
        self.x = 0
        self.p = 1

    def update(self, measurement):
        self.p = self.p + self.q
        k = self.p / (self.p + self.r)

        self.x = self.x + k * (measurement - self.x)
        self.p = (1 - k) * self.p

        return self.x