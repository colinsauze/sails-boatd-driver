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
        self.boat = sailsd.Boat(auto_update=True)
        self.wind = sailsd.Wind(auto_update=True)

    def heading(self):
        return math.degrees(self.boat.heading) % 360

    def wind_direction(self):
        return math.degrees(self.wind.angle)

    def wind_speed(self):
        return None

    def position(self):
        return (self.boat.latitude, self.boat.longitude)

    def rudder(self, angle):
        self.boat.rudder_angle = math.radians(angle)

    def sail(self, angle):
        pass


driver = SailsdDriver()
