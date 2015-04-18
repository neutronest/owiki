#-*- coding:utf-8 -*-

class tiantong(object):


    val = "456"
    def __init__(self):
        self.v = "123"
        return

    def change_val(self):
        self.val = "4567"

class Trainer:

    inputs = [0, 0, 0, 0, 0]
    def __init__(self, x, y, a):
        self.inputs = [0, 0, 0]
        self.inputs[3] = 42
        return

if __name__ == "__main__":
    c1 = Trainer(1, 1, 1)


    print c1.inputs
    print Trainer.inputs
    """
    tian = tiantong() # tian.v = "123" tian.val="456"
    tian.change_val() # tian.val = "4567"
    print tian.val # "4567" the instance-level val changed
    print "--------"
    print tiantong.val #"456" the class-level val changed
    """
