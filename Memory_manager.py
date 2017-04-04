class Partition:
    def __init__(self,pid,size):
        self.size = size
        self.pid = pid
        self.isFree = True
        self.next = None


class Memory:
    def __init__(self,memorySize,os_allocated):
        self.head = None
        self.memorySize = memorySize
        self.os_allocated = os_allocated
        self.process_memory = memorySize - os_allocated
        self.total_space = os_allocated
        os = Partition('OS',os_allocated)
        self.head = os
        free = Partition('Free',self.process_memory)
        self.head.next = free

    def start_process(self,pid,size):
        new_process = Partition(pid,size)

        running_process = self.head
        state = False

        while (running_process!=None):
            if(running_process.pid == 'Free'):
                if(running_process.size==size):
                    running_process.pid=pid
                    print(running_process.pid)
                    state = True

                if(running_process.size>size):
                    running_process.pid = pid
                    remaining_space = running_process.size - size
                    running_process.size = size
                    free = Partition('Free', remaining_space)
                    free.next = running_process.next
                    running_process.next = free
                    state = True

                if(state==True):
                    print(pid,' was added...')
                    break

                if (state == False):
                    print('Sorry! ',pid,' was  not added...','\nTrere is no enough memory...')
                    break

            else:
                running_process = running_process.next

    def terminate_process(self,pid):
        super_previous = None
        previous = None
        running_process = self.head
        terminated = False

        while (running_process.pid!=pid):
            if (running_process.next!= None):
                super_previous = previous
                previous = running_process
                running_process = running_process.next
            else:
                break

        if(running_process.pid==pid):
            if(previous.pid == 'Free' and running_process.next.pid=='Free'):
                running_process.size = running_process.size + previous.size + running_process.next.size
                super_previous.next = running_process
                running_process.next = running_process.next.next

            elif previous.pid == 'Free':
                running_process.size = running_process.size + previous.size
                super_previous.next = running_process

            elif running_process.next.pid == 'Free':
                running_process.size = running_process.size + running_process.next.size
                running_process.next = running_process.next.next

            running_process.pid = 'Free'
            terminated = True

        if (terminated == True):
            print('\n',pid, ' was terminated')

        else:
            print('\n',pid, ' not found...')

    def show_memory(self):

        running_process = self.head

        while (running_process != None):
            print(running_process.pid," => ",running_process.size,'\n===========================================')
            running_process=running_process.next

print('-----------------------------------------------------------')
print('|******************** Memory Manager *********************|')
print('-----------------------------------------------------------')

tot_memory = int(input('Input total Memory size : '))
os_memory = int(input('Input O\S Memory size : '))

print('-----------------------------------------------------------')
m=Memory(tot_memory,os_memory)

print('N -> to add new process')
print('T -> to terminate a process')
print('S -> to show memory')
print('E -> to End')
print('-----------------------------------------------------------\n')

while True:
    command = input('Input command : ')

    if(command is 'N'):
        pid = input('Input PID : ')
        size = int(input('Input Memory size : '))
        m.start_process(pid, size)
        print('-----------------------------------------------------------')

    if (command is 'T'):
        pid = input('Input PID : ')
        m.terminate_process(pid)
        print('-----------------------------------------------------------')

    if (command is 'S'):
        m.show_memory()
        print('-----------------------------------------------------------')

    if (command is 'E'):
        print('-----------------------------------------------------------')
        print('----------------------***************----------------------')
        print('-----------------------------------------------------------')
        break

