from cont import controller
from classes import Cascade
from classes import Feedback
from plant import plant
def createmachines(d,pos,goal,k0,kp,er):
    myplant=plant(d,64/1000,pos,goal,er)
    test=controller(k0,kp,d,goal)
    return(myplant,test)
pos=(0,0,0)
goal=(15,3)
d=0.052
k0=3.2
kp=1.2
er=0.25
myplant,test=createmachines(d,pos,goal,k0,kp,er)


test1=Feedback(Cascade(test,myplant))
output=[]
for i in range(120):
    output+=[[None]]
inp=test1.transduce(output)
inp=inp.pop(-1)
print (inp)
print(f'position and goal{pos,goal}')

