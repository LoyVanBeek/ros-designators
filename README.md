[![Build Status](https://travis-ci.org/LoyVanBeek/ros-designators.svg?branch=master)](https://travis-ci.org/LoyVanBeek/ros-designators)
ros-designators
===============

A Designator encapsulates the resolution of a value.
The 'description' of a value can be defined at write-time of the robot behavior, but the resolution of that value happens at runtime.
For example, there could be a designator called 'drink_location'
It may not be possible to know this location at write-time, but we can encapsulate the process of determining this location in a Designator.

The drink_location-designator may query a database, await the result of a perception module, whatever is needed to resolve the drink_location.
