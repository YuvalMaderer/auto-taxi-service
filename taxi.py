import random
import time


class Taxi:
    def __init__(self):
        self.available_taxis = []
        self.unavailable_taxis = []
        self.create_taxis()
        self.position = ''

    # Crate 10 taxis and add them to the taxi's list
    def create_taxis(self):
        for init in range(10):
            x = round(random.randint(0, 20_000)/1000, 1)
            y = round(random.randint(0, 20_000)/1000, 1)
            taxi_location = [x, y]
            self.available_taxis.append(taxi_location)

    # Print the taxis to the board and their position
    def print_taxis(self):
        p = 0
        for t in self.available_taxis:
            if t in self.unavailable_taxis:
                self.position = '(driving)'
            else:
                self.position = '(standing)'
            printer = (f'Taxi-{p + 1}: {round(self.available_taxis[p][0], 1)}Km,'
                       f' {round(self.available_taxis[p][1], 1)}Km, {self.position}')
            p += 1
            print(printer)

    # add 0.020 meters to taxi's x/y every 1 second from its current location until get to the request's x and y end
    def move(self, taxi_num, i, j, i_end, j_end):
        current_taxi = self.available_taxis[taxi_num]
        while round(current_taxi[0], 1) != i or round(current_taxi[1], 1) != j:  # from current taxi location
            # until request's x/y start
            if i > current_taxi[0]:
                current_taxi[0] += 0.020
            elif i < current_taxi[0]:
                current_taxi[0] -= 0.020

            time.sleep(1)
            if j < current_taxi[1]:
                current_taxi[1] -= 0.020
            elif j > current_taxi[1]:
                current_taxi[1] += 0.020

            time.sleep(1)

        while round(current_taxi[0], 1) != i_end or round(current_taxi[1], 1) != j_end:  # from current taxi location
            # until request's x/y end
            if i_end > current_taxi[0]:
                current_taxi[0] += 0.020
            elif i_end < current_taxi[0]:
                current_taxi[0] -= 0.020

            time.sleep(1)

            if j_end < current_taxi[1]:
                current_taxi[1] -= 0.020
            elif j_end > current_taxi[1]:
                current_taxi[1] += 0.020

            time.sleep(1)

        self.unavailable_taxis.remove(current_taxi)
