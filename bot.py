#!/usr/bin/env python

import os
import telebot

hostname = "google.co"
channel = '@irgping'
token = '688285869:AAE4lVtVdfeQcRAxQ2H5zxYM724IOxRpsL8'

response = os.system('ping ' + hostname)
bot = telebot.TeleBot(token)


if response == 0:
  print(hostname + ' is up!')
else:
  print(hostname + ' is down!')
  bot.send_message(channel, hostname + ' is down!')
© 2019 GitHub, Inc.
