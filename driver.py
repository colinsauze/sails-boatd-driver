# boatd driver to interface with sailsd

# Copyright 2016 Louis Taylor <louis@kragniz.eu>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import math

import boatd
import sailsd


class SailsdDriver(boatd.BaseBoatdDriver):
    def __init__(self):
        self.reconnect()

    def reconnect(self):
        self.boat = sailsd.Boat(auto_update=True)
        self.wind = sailsd.Wind(auto_update=True)

    def heading(self):
        return math.degrees(self.boat.heading) % 360

    def absolute_wind_direction(self):
        #despite the name of this function we need to return relative/apparent wind direction
        #internally sails stores absolute wind direction 
        #convert by subtracting heading from this

        #sails also has the wind coordinates 180 degrees out,fix this first
        #abs_wind = ( (self.wind.angle) + 180 ) % 360
        abs_wind = (self.wind.angle ) % 360
        print("self.wind.angle=",self.wind.angle)
        print("abs_wind=",abs_wind)
        return abs_wind

    def apparent_wind_direction(self):
        #convert to relative wind
        abs_wind = ( self.wind.angle  ) % 360
        #abs_wind = self.wind.angle

        heading = math.degrees(self.boat.heading) % 360
        print("heading=",heading)
        rel_wind = (abs_wind - heading) % 360
        print("rel_wind=",rel_wind)
        return rel_wind

    def wind_speed(self):
        return None

    def position(self):
        return (self.boat.latitude, self.boat.longitude)

    def rudder(self, angle):
        if angle > 45:
            angle = 45
        elif angle < -45:
            angle = -45

        self.boat.rudder_angle = math.radians(angle)

    def sail(self, angle):
        self.boat.sheet_length = abs(angle)/50

driver = SailsdDriver()
