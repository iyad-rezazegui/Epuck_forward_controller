
import classes   
import math 
class controller(classes.SM):
    maxvelocity0=6.28
    mo=3.14/2+0.1
    def __init__(self,k0,kp,d,gs,er,lm=None,rm=None):
        startState=None
        self.rm=rm
        self.er=er
        self.lm=lm
        self.k0=k0
        self.kp=kp
        self.d=d
        self.g=(0,0)
        self.startState=gs
    def getNextValues(self,state,inp):
    
        if inp is None :
            return(state,None)
        print(f'state is {state}')
        self.g=state[0]
        x_g,y_g=self.g
        x,y,o=inp
        cond = self.change(inp)
        if cond :
            news=state[1:]
        else:
            news=state
        x_g,y_g=self.g
        o_g=math.atan2((y_g-y),(x_g-x))
        angle_error=o_g-o
        o_dot=(angle_error)*self.k0
        o_dot=min(o_dot,self.mo)
        if o_dot<0:
            o_dot=min(o_dot,-self.mo)

        print(f"the o is {o_dot}")
        v =  math.sqrt((x_g - x)**2 + (y_g - y)**2) * self.kp
        #computing vl and vr :
        vl=v-(o_dot*self.d)/2
        vr=v+(o_dot*self.d)/2
        vl = min(vl, self.maxvelocity0)
        if vl<0:
            vl = max(vl, -self.maxvelocity0)
        vr = min(vr, self.maxvelocity0)
        if vr<0:
            vr = max(vr, -self.maxvelocity0)
        # modifying the wheel speed
        if cond:
            vl,vr=0,0
        self.lm.setVelocity(vl)
        self.rm.setVelocity(vr)
        print(f"speeds vl,vr :{vl,vr}")
       
        return (news,(vl,vr))
    
    def done(self,state):
        if state==[]:
            return True
    def change(self,inp):
        x,y,ignore=inp
        xg,yg=self.g
        xe=abs(xg-x)
        ye=abs(yg-y)
        if ye<self.er and xe<self.er:
            return True
        return False
   


   
     
   

    







    


