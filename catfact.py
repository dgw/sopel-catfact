# coding=utf-8
"""
catfact.py - Sopel cat facts module
Copyright 2018 dgw
Licensed under the Eiffel Forum License 2

https://sopel.chat
"""
from __future__ import unicode_literals, absolute_import, print_function, division

import requests

from sopel.module import commands, example

@commands('catfact')
@example('.catfact')
def cat_fact(bot, trigger):
    """Fetch a random cat fact."""
    try:
        r = requests.get(url='https://catfact.ninja/fact', timeout=(10.0, 4.0))
    except requests.exceptions.ConnectTimeout:
        bot.say("Connection timed out.")
        return
    except requests.exceptions.ConnectionError:
        bot.say("Couldn't connect to server.")
        return
    except requests.exceptions.ReadTimeout:
        bot.say("Server took too long to send data.")
        return
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        bot.say("HTTP error: " + e.message)
        return
    try:
        data = r.json()
    except ValueError:
        bot.say("Couldn't decode API response: " + r.content)
        return
    bot.say(data['fact'])