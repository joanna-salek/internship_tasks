#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time


class Road:
    # class representing straight road with maximal speed allowed in m/s, distance in m and turn in angles
    def __init__(self, max_speed, distance, turn=0):
        self.max_speed = max_speed
        self.distance = distance
        self.turn = turn


class Trip:
    # class to load all roads in one trip
    def __init__(self):
        self.roads = []

    def add_road(self, road):
        self.roads.append(road)


# creating roads, specify max speed in m/s,
# distance in m and optionally turn in angles
road_1 = Road(30, 10, 90)
road_2 = Road(50, 160, 45)
road_3 = Road(10, 12)
road_4 = Road(30, 20, -900)
road_5 = Road(27, 100, -30)
road_6 = Road(7, 15, 25)

# and adding them to trip class
trip = Trip()
trip.add_road(road_1)
trip.add_road(road_2)
trip.add_road(road_3)
trip.add_road(road_4)
trip.add_road(road_5)
trip.add_road(road_6)


# some useful methods for class Car

def m_speed(h_p):
    # calculate max speed based on horse power
    if h_p <= 70:
        return 17
    elif 70 < h_p <= 100:
        return 22.5
    elif 100 < h_p <= 150:
        return 28
    elif h_p > 150:
        return 38


def e_speed(h_p, v):
    # calculate engine speed based on car velocity and horse power
    es = 1700
    if h_p <= 70:
        es += 500
    elif 70 < h_p <= 100:
        es += 300
    elif 100 < h_p <= 150:
        es += 100
    if 50 < v <= 70:
        es += 100
    elif 70 < v <= 100:
        es += 300
    elif 100 < v <= 140:
        es += 1000
    elif v > 35:
        es += 1500
    return es


def check_gear(v):
    # check gear based on current velocity
    if v <= 7:
        return 1
    elif 7 < v <= 9.7:
        return 2
    elif 9.7 < v <= 12.5:
        return 3
    elif 12.5 < v <= 16.7:
        return 4
    else:
        return 5


def e_temperature(e_speed):
    # check engine temperature based on current engine speed
    temperature = 80
    if 2500 <= e_speed <= 3000:
        return temperature + 3
    elif 3000 < e_speed <= 4000:
        return temperature + 7
    elif e_speed > 4000:
        return temperature + 10
    else:
        return temperature


def s_wheel(angle):
    # returns angle in range 0 to 360
    while True:
        if 360 > angle >= 0:
            break
        elif angle >= 360:
            angle -= 360
        elif angle < 0:
            angle += 360
    return angle


class Car:
    # create car
    def __init__(self, car_id, horse_power):
        self.id = car_id
        self.horse_power = horse_power
        self.turn = 0
        self.distance = 0
        self.engine_temp = 0
        self.engine_speed = 0
        self.speed = 0
        self.max_speed = m_speed(self.horse_power)
        self.gear = "neutral"
        self.time = time.time()
        print("Starting position\n")
        self.show_logs()

    def accelerate(self):
        # car acceleration
        print("Accelerating\n")
        self.engine_temp += 20
        self.gear = 1
        self.engine_speed = 1600
        self.speed = 5
        self.distance += 5
        self.show_logs()

    def breaking(self):
        # car breaking
        print("Breaking\n")
        self.engine_temp -= 5
        self.gear = 2
        self.engine_speed = 1500
        self.speed = 5
        self.distance += 5
        self.turn = 0
        self.show_logs()

    def next_position(self):
        # generate next car position
        self.accelerate()
        for road in trip.roads:
            self.turn = s_wheel(self.turn + road.turn)
            if road.max_speed < self.max_speed:
                self.speed = road.max_speed
            else:
                self.speed = self.max_speed
            self.distance += road.distance
            self.engine_speed = e_speed(self.horse_power, self.speed)
            self.gear = check_gear(self.speed)
            self.engine_temp = e_temperature(self.engine_speed)
            # wait as many seconds as car need to drive this road
            time.sleep(road.distance / self.speed)
            self.show_logs()
        self.breaking()

    def show_logs(self):
        # present current logs
        print("Current velocity in m/s: ", self.speed)
        print("Current Engine Speed: ", self.engine_speed)
        print("Current gear: ", self.gear)
        print("Distance in m:", self.distance)
        print("Steering wheel angle: ", self.turn)
        print("Engine temperature: ", self.engine_temp, "\n")


# create car with id and horse power
car = Car("OK28282", 200)

# start car trip
car.next_position()
