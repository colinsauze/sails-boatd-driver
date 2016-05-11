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

driver = boatd.Driver()

boat = sailsd.Boat(auto_update=True)
wind = sailsd.Wind(auto_update=True)

@driver.heading
def sailsd_heading():
    return math.degrees(sailsd.heading) % 360

@driver.wind_direction
def sailsd_wind():
    return math.degrees(wind.angle)

@driver.position
def sailsd_lat_long():
    return (sailsd.latitude, sailsd.longitude)

@driver.rudder
def sailsd_set_rudder(angle):
    boat.rudder_angle = math.radians(angle)
