class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek (self):
        return self.items[len(self.items)-1]
    def isEmpty (self):
        return self.items==[]
    def size(self):
        return len(self.items)


stack =Stack()
operators = ['*','/','+','-']

class post_fix:
    def __init__(self,expression):
        self.temp_count=1

        for i in expression:
            if not (i in operators):
                stack.push(i)

            elif(i is '*'):
                second = stack.pop()
                first = stack.pop()
                print('LD   ', first)
                print('ML   ', second)
                print('ST   ', 'Temp',self.temp_count)
                stack.push('Temp '+str(self.temp_count))
                self.temp_count+=1

            elif (i is '/'):
                second = stack.pop()
                first = stack.pop()
                print('LD   ', first)
                print('DV   ', second)
                print('ST   ', 'Temp',self.temp_count)
                stack.push('Temp '+str(self.temp_count))
                self.temp_count += 1

            elif (i is '+'):
                second = stack.pop()
                first = stack.pop()
                print('LD   ', first)
                print('AD   ', second)
                print('ST   ', 'Temp',self.temp_count)
                stack.push('Temp '+str(self.temp_count))
                self.temp_count += 1

            elif (i is '-'):
                second = stack.pop()
                first = stack.pop()
                print('LD   ', first)
                print('SB   ', second)
                print('ST   ', 'Temp',self.temp_count)
                stack.push('Temp '+str(self.temp_count))
                self.temp_count += 1

pfix=input("Pleasee enter the postfix expression :")
post_fix(pfix)#'ABC*+DE-/')




