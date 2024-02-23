import turtle as t
from disk import Disk

class Pole(object):
    def __init__(self, name="", xpos = 0, ypos = 0, thick = 10, length = 100) :
        self.pname = name
        self.stack = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length

    def showpole(self):
        t.penup()
        t.goto(self.pxpos, self.pypos)
        t.pendown()
        t.fd(self.pthick / 2)
        t.lt(90)
        t.fd(self.plength)
        t.lt(90)
        t.fd(self.pthick)
        t.lt(90)
        t.fd(self.plength)
        t.lt(90)
        t.fd(self.pthick / 2)
        t.penup()
        t.goto(self.pxpos, self.pypos)
        t.pendown()
        # t.done()

    def pushdisk(self, disk):
        disk.showdisk()
        disk.newpos(self.pxpos, self.toppos)
        self.stack.append(disk)
        self.toppos += disk.dheight

    def popdisk(self):
        if not self.stack:
            return None 

        self.toppos -= self.stack[-1].dheight
        a = self.stack.pop()
        a.cleardisk()
        return a
    
# def main():
#     t.speed(50)

#     pole2 = Pole("Pole 2", 0, -50)

#     pole2.showpole()


# if __name__ == "__main__":
#     main()