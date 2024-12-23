class Car:

    def __init__(self,speed=0):
        self.speed= speed
        self.odometer=0
        self.time=0

    def say_state(self):
        print("I'm going {} mph".format(self.speed))
        print(__name__)

    def accelerate(self):
        self.speed+=5

    def brake(self):
        if self.speed<5:
            self.speed = 0
        else:
            self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time +=1

if __name__ == "__main__":
    my_car = Car()
    print("I'm a car!")
    print(__name__)

    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, show [O]dometer")
        if action not in "ABO" or len(action)!=1:
            print("i dont know how to do this")
            continue
        if action =='A':
            my_car.accelerate()
        if action == 'B':
            my_car.brake()

        if action == 'O':
            print("The car has driven {} miles ".format(my_car.odometer))

        my_car.step()
        my_car.say_state()
