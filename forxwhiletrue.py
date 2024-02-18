import sys
class forxwhileTrue:
    def __init__(self, x=0, boolean=True):
        self.x = x
        self.boolean = boolean
        while boolean:
            #enter the program here with conditionals set to change the Boolean value at triggers
            self.x += 1
            continue
class forx(forxwhileTrue):
    def __init__(self):
        super(forx, self).__init__()

{lambda: forx
    .type(forxwhileTrue)
    .value(sys.argv[1])
    .trigger(False)
}