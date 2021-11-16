# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 15:02:49 2021

@author: Admin
"""

from periphery import GPIO

gpio_p13 = GPIO("/dev/gpiochip0", 6, "in")
gpio_p18 = GPIO("/dev/gpiochip4", 10, "in")
gpio_p22 = GPIO("/dev/gpiochip4", 12, "in")
gpio_p29 = GPIO("/dev/gpiochip0", 7, "in")
gpio_p31 = GPIO("/dev/gpiochip0", 8, "in")

gpio_p16 = GPIO("/dev/gpiochip2", 9, "out")

led = GPIO("/dev/gpiochip2", 13, "out")  # pin 37
button = GPIO("/dev/gpiochip4", 13, "in")  # pin 36

try:
  while True:
    value = gpio_p13.read()     
    gpio_p16.write(not value)
    led.write(button.read())
    
except KeyboardInterrupt:
    
  led.write(False)
  gpio_p16.write(False)
  
  gpio_p16.close()
  gpio_p13.close()
  led.close()
  button.close()

  gpio_p18.close()
  gpio_p22.close()
  gpio_p29.close()
  gpio_p31.close()