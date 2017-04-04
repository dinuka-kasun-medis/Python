class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Car:
    def __init__(self,no_plate):
        self.number_of_time=0
        self.no_plate = no_plate

    def get_count(self):
        self.number_of_time+=1


car_park = Queue()
tem_park = Queue()
waiting_list = Queue()


class Car_Park:
    def check_availability(self):
        if (car_park.size() != 10):
            return True
        else:
            return False

    def park_car(self, car):
        if (self.check_availability() == True):
            car_park.enqueue(car)
            car.get_count()
            print(car.no_plate," car was parked...")

        else:
            self.add_waiting(car)
            print(car.no_plate," car was added to waiting list...")

    def out_car(self, vehicl):
        removed='no'
        while not (car_park.isEmpty()):
            car=car_park.dequeue()
            car.get_count()
            if (car.no_plate == vehicl.no_plate):
                removed = 'yes'
                print('Out =',vehicl.no_plate ,' ROOM AVAILABLE!!')
            else:
                tem_park.enqueue(car)

        while not (tem_park.isEmpty()):
            car_park.enqueue(tem_park.dequeue())

        if(removed == 'yes'):
            self.get_waiting()

    def add_waiting(self, plate_no):
        waiting_list.enqueue(plate_no)

    def print_carPark(self):
        for i in range(0,len(car_park.items)):
            car=car_park.items[i]
            print('car , ',car.no_plate,' ','Moves',car.number_of_time)

        print('')

        if(self.check_availability()==True):
            print("There are ", (10 - car_park.size()), " rooms available...")
        else:
            print("\nThere are no rooms....\nPlease wait...")

    def get_waiting(self):
        if not(waiting_list.isEmpty()):
            c.park_car(waiting_list.dequeue())

c=Car_Park()

print('---------------------------------------------------------------------')
print('\na:arrive\nd:departure')
print("check : To show current status of the garage\n---------------------------------------------------------------------\n\n")

while True:
    command=input("Enter the command : ")
    if (command=='a'):
        no_plate = input("Enter the no plate : ")
        c.park_car(Car(no_plate))
        continue

    elif(command=='d'):
        no_plate = input("Enter the no plate : ")
        c.out_car(Car(no_plate))
        continue

    elif(command=='check'):
        c.print_carPark()
        continue

    else:
        print('Somthing wrong....\n')
