# Csharp random is dumb, so we have to reimplement it's RNG here
class CSRandom:
    def __init__(self, seed):
        # initialize
        self.MAX_INT = 0x7FFFFFFF
        self.MIN_INT = 0x80000000
        self.seed = seed
        MSEED = 0x09A4EC86
        seedarray = [0]*56

        sub = self.MAX_INT if (seed == self.MIN_INT) else abs(seed)
        mj = MSEED - sub

        seedarray[55] = mj
        mk = 1
        for i in range(1, 55):
            ii = (21*i) % 55
            seedarray[ii] = mk
            mk = mj - mk
            if mk < 0:
                mk += self.MAX_INT
            mj = seedarray[ii]

        for k in range(1, 5):
            for i in range(1, 56):
                seedarray[i] -= seedarray[1+(i+30) % 55]
                if seedarray[i] < 0:
                    seedarray[i] += self.MAX_INT
        self._inext = 0
        self._inextp = 21
        self._seed = 1
        self._seedarray = seedarray

    def __sample(self):
        locINext = self._inext
        locINextp = self._inextp

        locINext = 1 if (locINext+1 >= 56) else locINext+1
        locINextp = 1 if (locINextp+1 >= 56) else locINextp+1

        retVal = self._seedarray[locINext]-self._seedarray[locINextp]
        if retVal == self.MAX_INT:
            retVal -= 1
        if retVal < 0:
            retVal += self.MAX_INT

        self._seedarray[locINext] = retVal

        self._inext = locINext
        self._inextp = locINextp

        return retVal

    def __sample_lr(self):
        res = self.__sample()
        if self.__sample() % 2 == 0:
            res = -res
        return (res + self.MAX_INT - 1)/(2.0*self.MAX_INT-1)

    def sample(self):
        return self.__sample()*(1.0/self.MAX_INT)

    def next(self, min_val=0.5, max_val=0.5):
        if min_val == 0.5 and max_val == 0.5:
            return self.__sample()
        elif min_val != 0.5 and max_val == 0.5:
            return int(self.sample()*min_val)
        else:
            ran = max_val - min_val
            if ran <= self.MAX_INT:
                return int(ran*self.sample()) + min_val
            else:
                return int(ran*self.__sample_lr()) + min_val
