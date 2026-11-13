from cont import controller
from classes import Cascade
from classes import Feedback
from plant import plant
from controller import Robot
robot = Robot()
lm = robot.getDevice('left wheel motor')
rm = robot.getDevice('right wheel motor')
lm.setPosition(float('inf'))
rm.setPosition(float('inf'))

def createmachines(d,pos,goal,k0,kp,er,lm,rm):
    myplant=plant(d,32/1000,pos,goal,er)
    test=controller(k0,kp,d,goal,er,lm,rm)
    return(myplant,test)
pos=(0,0,0)

goal=[(0,0), (4,1) , (10,2), (14,3), (17,4), (21,5), (23,5)]
d=2
k0=4
kp=1
er=0.5
myplant,test=createmachines(d,pos,goal,k0,kp,er,lm,rm)


test1=Feedback(Cascade(test,myplant))
test1.start()
while robot.step(32)!=-1:
    inp=test1.transduce([None])   
    print (inp)
print(f'position and goal{pos,goal}')

