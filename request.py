import random


class Request:
    def __init__(self):
        self.new_request = []

    # Create random request call, which cant be more than 2 km from x,y start to x,y end
    def search_request(self):
        search_request = True
        while search_request:
            x_start = round(random.randint(0, 20000) / 1000, 1)
            y_start = round(random.randint(0, 20000) / 1000, 1)
            x_end = round(random.randint(0, 20000) / 1000, 1)
            y_end = round(random.randint(0, 20000) / 1000, 1)
            if abs(x_start - x_end) < 2:
                if abs(y_start - y_end) < 2:
                    request = [x_start, y_start], [x_end, y_end]
                    self.new_request.append(request)
                    search_request = False
