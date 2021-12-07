from lib.lib import *
from math import pi


# return velocity (single dimension)
def tan_velocity(radius: mpnum, time: mpnum):
    return (mpnum(str(2*pi))*radius)/time

# returns acceleration
def centripital_from_velocity(velocity: mpnum, radius: mpnum):
    output = velocity.pow(2)/radius
    return output
