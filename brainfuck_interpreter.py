"""
This class (or rather pair of classes) acts as an interpreter for the esolang brainfuck(https://esolangs.org/wiki/Brainfuck).
For the time being, the variable text_to_be_interpreted contains whatever you want to interpret and must be hardcoded there.

Created by Ethan Lynch

"""

class Tape():
    def __init__(self):
        self.tape = [0]
        self.head = 0
    
    def moveLeft(self):
        if self.head == 0:
            self.tape.insert(0,0)
        else:
            self.head -= 1
        self.cleanUp()
    
    def moveRight(self):
        if self.head + 1 == len(self.tape):
            self.tape.append(0)
        self.head += 1
        self.cleanUp()

    def inc(self):
        self.tape[self.head] += 1
        if self.tape[self.head] == 256:
            self.tape[self.head] = 0

    def dec(self):
        self.tape[self.head] -= 1
        if self.tape[self.head] == -1:
            self.tape[self.head] = 255

    def printVal(self):
        print(chr(self.tape[self.head]),end='')
        
    def inputVal(self):
        #this could be made better but is fine for now
        self.tape[self.head] = ord(input("Please input a character: "))

    def show(self):
        self.cleanUp()
        print(self.tape)

    def cleanUp(self):
        while self.tape[0] == 0 and self.head != 0:
            self.tape.pop(0)
            self.head -= 1
        while self.tape[len(self.tape)-1] == 0 and self.head != len(self.tape)-1:
            self.tape.pop()

class BF():
    def __init__(self,instructions):
        self.tape = Tape()
        self.inst = instructions   
        self.instHead = 0
    
    def interpret(self):
        while self.instHead != len(self.inst):
            self.readChar()
        print()
        self.tape.show()
        
    def readChar(self):
        char = self.inst[self.instHead]
        if char == '+':
            self.tape.inc()
        elif char == '-':
            self.tape.dec()
        elif char == '<':
            self.tape.moveLeft()
        elif char == '>':
            self.tape.moveRight()
        elif char == '.':
            self.tape.printVal()
        elif char == ',':    
            self.tape.inputVal()
        elif char == '[':
            self.startLoop()
        elif char == ']':
            self.endLoop()
        else:
            pass
        self.instHead +=1

    def startLoop(self): 
        if self.tape.tape[self.tape.head] == 0:
            depth = 0
            while True:
                if self.inst[self.instHead] == '[':
                    depth += 1
                elif self.inst[self.instHead] == ']':
                    depth -= 1
                
                if self.inst[self.instHead] != ']' and depth != 0:
                    self.instHead += 1   
                    break
                self.instHead += 1    
                
    def endLoop(self):
        if self.tape.tape[self.tape.head] != 0:
            depth = 0
            while True:
                if self.inst[self.instHead] == '[':
                    depth -= 1
                elif self.inst[self.instHead] == ']':
                    depth += 1

                if self.inst[self.instHead] == '[' and depth == 0:
                    break
                self.instHead -= 1

def main():

    text_to_be_interpreted = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."


    bf = BF(text_to_be_interpreted)
    bf.interpret()
    
    print('\n')



main()