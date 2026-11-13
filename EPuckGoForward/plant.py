import classes
import math
class plant(classes.SM):
    def __init__(self,d,TIME_STEP,pos,gs,er):

        self.er=er
        self.d=d
        self.gs=gs
        self.dt=TIME_STEP
        self.startState=pos
    def getNextValues(self,state,inp):
        if inp is None:
            return(state,state)
        x,y,o=state
        vl,vr=inp
        # computing v and 0.dot
        v=(vl+vr)/2
        o_dot=(vr-vl)/self.d
        #now finding new positions
        x+=v*math.cos(o)*self.dt
        y+=v*math.sin(o)*self.dt
        o+=o_dot*self.dt
        news=(x,y,o)
        return(news,state)

   
    
    
        



