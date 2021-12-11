import gmpy2
from scripts.lib import *
from math import pi, sqrt


# tangential velocity
# and its algebraic alternatives

# return velocity (single dimension)
def tan_velocity(radius: mpnum, time: mpnum):
    return (mpnum(str(2*pi))*radius)/time

# return velocity from acceleration and radius
def velocity_from_tan(acceleration, radius):
    return sqrt(acceleration*radius)

# return radius from tangential acceleration
def radius_from_tan(acceleration, velocity):
    return velocity**2/acceleration


# centripital acceleration and its
# algebraic representations

# returns acceleration
def centripital_from_velocity(velocity: mpnum, radius: mpnum):
    output = velocity.pow(2)/radius
    return output

# takes time for a revolution, and returns acceleration
def centripital_from_time(time, radius):
    output = (4*(pi**2)*radius)/(time**2)
    return output

# returns radius from centripital acceleration, and time
def radius_from_centripital(acceleration, time):
    return sqrt((time**2*acceleration)/(4*pi**2))

# returns time from centripital acceleration, and radius
def time_from_centripital(acceleration, radius):
    return sqrt((4*pi**2*radius)/acceleration)