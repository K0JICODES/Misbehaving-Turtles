import turtle
import random

class MisbehavingTurtle(turtle.Turtle):
    
    '''def forward(self,t):
        n = random.randint(1,100)
        print(n)
        if n <= 25:
            print('misbehaved')
            turtle.Turtle.forward(self,-t)
        else:
            turtle.Turtle.forward(self,t)'''
            
    def right(self,t):
        n = random.randint(1,100)
        print(n)
        if n <= 25:
            print('misbehaved')
            turtle.Turtle.right(self,-t)
        else:
            turtle.Turtle.right(self,t)   
            
    def left(self, t):
        self.right(-t)
    
                
                

# test case
# drawing an octagon and a square
def drawing_test(t):
    '''drawing_test(t)
     draws an octagon and square with t'''
    for i in range(8):
        t.forward(30)
        t.left(45)
    t.right(45)
    for i in range(4):
        t.forward(50)
        t.right(90)
        
# one nice turtle and one not-so-nice turtle
wn = turtle.Screen()
sugar = turtle.Turtle()
sugar.color('green')
drawing_test(sugar)
spice = MisbehavingTurtle()
spice.color('red')
print('misbehaving starts')
drawing_test(spice)
wn.mainloop()