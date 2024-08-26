from taxi import Taxi
from request import Request
import threading
import time

taxi = Taxi()
print('Initial taxi locations:')
taxi.print_taxis()
time.sleep(20)


def choose_taxi():
    new_request = waiting_order_queue_list[0]
    request_x = new_request[0][0]  # first x of the request
    request_y = new_request[0][1]  # first y of the request

    try:  # if the length of the available taxi list is more than 0
        new_taxis_available_list = []
        for taxis in taxi.available_taxis:
            if taxis not in taxi.unavailable_taxis:
                new_taxis_available_list.append(taxis)
        chosen_taxi = new_taxis_available_list[0]
        for choose in new_taxis_available_list:
            first_distance = abs(request_x - choose[0]) + abs(request_y - choose[1])
            second_distance = abs(request_x - chosen_taxi[0] + abs(request_y - chosen_taxi[1]))
            if first_distance < second_distance:
                chosen_taxi = choose
        waiting_order_queue_list.remove(new_request)
        index = taxi.available_taxis.index(chosen_taxi)
        taxi.unavailable_taxis.append(chosen_taxi)
        t1 = threading.Thread(target=taxi.move, args=(index, request_x, request_y, new_request[1][0],
                                                      new_request[1][1]))
        t1.start()
    except IndexError:
        print('no available taxis')


waiting_order_queue_list = []
while True:
    request = Request()
    request.search_request()
    new = request.new_request[0]
    waiting_order_queue_list.append(new)
    choose_taxi()
    print('\nOrder Queue')
    if len(waiting_order_queue_list) > 0:
        print(f'waiting requests: {waiting_order_queue_list}\n')
    else:
        print('Empty\n')
    print('Taxi locations:')
    taxi.print_taxis()
    time.sleep(3)
