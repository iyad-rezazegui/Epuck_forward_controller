
class SM:
    startState = None
    
    def start(self):
        self.state = self.startState

    def step(self, inp):
        if not self.done(self.state):
            (s, o) = self.getNextValues(self.state, inp)
            self.state = s
            return o

    def transduce(self, inputs):
        #self.start()
        j=0
        results = []
        for i in inputs:
            if not self.done(self.state):   # only step if done == True
                results.append(self.step(i))
                j+=1
        print(f"how many times it run: {j}")
        # else: skip (like continue)
        return results

    def done(self,state):
        return False
        


class Cascade(SM):
    def __init__(self, sm1, sm2):
        self.m1 = sm1
        self.m2 = sm2
        self.startState = (sm1.startState, sm2.startState)
    def start(self):
        self.m1.start()
        self.m2.start()
        self.state = (self.m1.state, self.m2.state)
    
    def getNextValues(self, state, inp):
        s1, s2 = state
        newS1, o1 = self.m1.getNextValues(s1, inp)
        newS2, o2 = self.m2.getNextValues(s2, o1)
        return ((newS1, newS2), o2)
    
    def done(self,state):
        s1,s2=state
        if self.m1.done(s1)==True or self.m2.done(s2)==True:
            return True


class Parallel(SM):
    def __init__(self, sm1, sm2):
        self.m1 = sm1
        self.m2 = sm2
        self.startState = (sm1.startState, sm2.startState)

    def getNextValues(self, state, inp):
        s1, s2 = state
        newS1, o1 = self.m1.getNextValues(s1, inp)
        newS2, o2 = self.m2.getNextValues(s2, inp)
        return ((newS1, newS2), (o1, o2))

class Feedback(SM):
    def __init__(self,sm1):
        self.m=sm1
        self.startState = self.m.startState
    
    def start(self):
        # initialize underlying SM
        self.m.start()
        self.state = self.startState
        
    def getNextValues(self,state,inp):
        s=state
        ignore,o=self.m.getNextValues(s,None)
        news,ignore=self.m.getNextValues(s,o)
        return (news,o)
     
    def done(self,state):
        if self.m.done(state)==True:
            return True
        



    

    