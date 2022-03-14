from random import randint
from time import sleep,time
from fei.ppds import Thread, Semaphore, print, Event, Mutex

class SharedData:
    def __init__(self):
        self.ad = Semaphore(1)
        self.ts = Semaphore(1)
        self.ls_monitor = LS()
        self.ls_sensor = LS()
        self.vd = Event()

class LS:
    def __init__(self):
        self.m = Mutex()
        self.c = 0

    def lock(self, sem):
        self.m.lock()
        self.c += 1
        if self.c == 1:
            sem.wait()

        self.m.unlock()
        return self.c

    def unlock(self, sem):
        self.m.lock()
        self.counter -= 1
        if self.counter == 0:
            sem.signal()

        self.mutex.unlock()

def monitor(monitor_id , shared):
    shared.valid_data.wait()
    while True:
        sleep(randint(40, 50)/1000)
        start_time = time()
        shared.turnstile.wait()
        monitor_counter = shared.ls_monitor.lock(shared.access_data)
        shared.turnstile.signal()
        read_time = time() - start_time
        print('monit: {:.2f},    pocet_citajucich_monitorov={:.2f}, trvanie_citania{:.3f}\n'.format(monitor_id,
                                                                                                    monitor_counter,
                                                                                                    read_time))
        shared.ls_monitor.unlock(shared.access_data)

def sensor(sensor_id,sensor_type, shared):
    while True:
        shared.ts.wait()
        shared.ts.signal()

        sensor_counter = shared.ls_sensor.lock(shared.ad)
        write_duration = 0
        if sensor_type == 0:
            write_duration = randint(10, 20) / 1000
        else:
            write_duration = randint(20, 25) / 1000

        print(f'cidlo {sensor_id}:  pocet_zapisujucich_cidiel={sensor_counter}, trvanie_zapisu={write_duration}\n')
        sleep(write_duration)
        shared.vd.signal()
        shared.ls_sensor.unlock(shared.ad)
        sleep(randint(50, 60) / 1000)
