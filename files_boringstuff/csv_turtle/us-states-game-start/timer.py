import time


class CountDown:
    def __init__(self, time_secs):
        self.time_ = time_secs
        
    def start_count_down(self):
        got_to_zero = False
        while not got_to_zero:
            mins, secs = divmod(self.time_, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end='\r')
            time.sleep(1)
            self.time_ -= 1
            # import pdb; pdb.set_trace()
            if mins == 0 and secs == 0:
                got_to_zero = True
        return True


times = CountDown(2)
# tiempo = times.count_down()
if times.start_count_down():
    print('perdiste')
