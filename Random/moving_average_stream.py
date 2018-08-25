import collections

class MovingAverage(object):

    def __init__(self, size):
        self.queue = collections.deque(maxlen=size)
        self.window_size = size
        self.current_sum = 0
        

    def next(self, val):
        self.current_sum += val
        if len(self.queue) == self.window_size:
            self.current_sum -= self.queue.popleft()
        self.queue.append(val)
        average = float(self.current_sum) / len(self.queue)
        print(average)
        return average

def main():
    average_window = MovingAverage(3)
    average_window.next(3)
    average_window.next(11)
    average_window.next(16)
    average_window.next(100)

main()