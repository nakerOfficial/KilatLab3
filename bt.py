class BT:
    final = []
    results = []
    start = []
    isNoShow = False

    def Generate(self, values):
        self.start = values
        self.final = [None for a in self.start]
        self.final = [None for a in self.start]
        self.backTracking()

        return  self.results

       
    def backTracking(self, k = 0):
        for a in self.start:
            self.final[k] = a
            if k == len(self.start)-1:
                self.tipar()
            else:
                self.backTracking(k = k + 1)

    def tipar(self):
        buff = []
        resStr = ''
        for a in self.final:
            if not next((x for x in buff if x == a), None):
                buff.append(a)
                resStr += str(a)

        if len(resStr) <= 12 and len(resStr) >= 6:
            self.results.append(resStr)