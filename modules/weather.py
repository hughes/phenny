#!/usr/bin/env python
"""
weather.py - Phenny Weather Module
"""

import re, urllib
import pywapi
import string


def f_weather(self, command):
    """.weather <location> - Show the weather at the given location."""

    query = command.group(2)
    if not query: 
        return self.msg(command.sender, 'Try .weather London, for example?')

    locations = pywapi.get_loc_id_from_weather_com(query)

    if 'count' not in locations or locations['count'] == 0:
        return self.msg(command.sender, "Couldn't find location for {0}".format(query))
      
    result = pywapi.get_weather_from_weather_com(locations[0][0])
    output = "{0} and {1}{2} in {3}".format(
        string.capitalize(result['current_conditions']['text']),
        result['current_conditions']['temperature'],
        result['units']['temperature'],
        locations[0][1])

    return self.msg(command.sender, output.encode('utf-8'))


f_weather.rule = (['weather'], r'(.*)')


if __name__ == '__main__': 
   print __doc__.strip()
