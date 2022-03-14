import math
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
        self.c -= 1
        if self.c == 0:
            sem.signal()

        self.m.unlock()

def monitor(monitor_id , shared):
    shared.vd.wait()
    while True:
        read_duration = randint(40, 50)/1000
        sleep(read_duration)
        shared.ts.wait()
        monitor_counter = shared.ls_monitor.lock(shared.ad)
        shared.ts.signal()
        print('monit: {:2d},    pocet_citajucich_monitorov={:2d}, trvanie_citania{:3d}\n'.format(monitor_id,
                                                                                                    monitor_counter,
                                                                                                    math.floor(
                                                                                                        read_duration*1000)))
        shared.ls_monitor.unlock(shared.ad)

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

        print('cidlo {:2d}:  pocet_zapisujucich_cidiel={:2d}, trvanie_zapisu={:3d}\n'.format(sensor_id,
                                                                                             sensor_counter,
                                                                                             math.floor(write_duration*1000)))
        sleep(write_duration)
        shared.vd.signal()
        shared.ls_sensor.unlock(shared.ad)
        sleep(randint(50, 60) / 1000)

shared = SharedData()
sensors = [Thread(sensor, i, 0, shared) for i in range(2)]
sensors.append(Thread(sensor, 2, 1, shared))
monitors = [Thread(monitor, j, shared) for j in range(8)]

for thread in monitors + sensors:
    thread.join()
