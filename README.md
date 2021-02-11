# Internship tasks 
## Each task can be found in separate file respectively to file name 
### Each task was created using python 3.9.0

### 1. Task One

Program reads the "input.txt" file found in project directory and generates the "output.txt" file.

The "input.txt" file contains binary information of objects represented by 8 consecutive bits, consisting of 3 fields:

- the first 4 bits represent an object identification number written in binary mode

- 3 consecutive bits represent the message

- 1 last bit is a control bit - if the object number is even, this bit will have a value of 0, otherwise it will be 1


The output file contain information:

- first line, the number of all loaded objects

- second line the number of  defective objects -containing errors

- third line all correct objects that did not contain errors, saved in the form and order in which they appeared in the file "input.txt"

 
An object contains errors if:

- the message consists only of bits equal to 0

- the control bit has an invalid value

To run program, run file in project directory:
```bash
python task_one.py
```


### 2. Task two 

Program which, depending on the selected application operation mode:

- convert decimal numbers to binary

- convert binary numbers to decimals

Run program and follow instructions. Result will be printed on the screen.

```bash
python task_two.py
```

### 3. Task Three

Car simulation application that, by displaying logs in the console, simulate in real time the operation of the car's on-board computer,
logging basic telemetry while driving (e.g. speed, steering wheel radius, engine temperature, etc.) with different sampling rates, at the level of seconds.
Application is based on OOP.
Simulation is calculated mainly based on car horse power defined while creating object car, also it depends of roads type (maximal speed and road distance)

Roads can be altered simply by changing or adding objects in road class and adding road to trip class as shown below:

```python
# creating roads, specify max speed in m/s,
# distance in m and optionally turn in angles (default = 0)
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
```

Also car object can be altered 

```python
# create car with id and horse power
car = Car("OK28282", 200)
```

To run simulation:

```bash
python task_three.py
```
