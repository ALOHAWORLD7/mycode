#!/usr/bin/env python3

switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

print( switch["hostname"] )
print( switch["ip"] )


print("first test")

print(switch.get("lynx"))

print("Second")
print(switch.get("lynx", "THIS IS HE WAY"))

print('third')
print(switch.get("third"))


print("4th TEst")
print(switch.keys())

print('5th Test')
print(switch.values())

print( "Sixth test - .pop()" )
switch.pop("version") # removes this key (and value) pair
print( switch.keys() )   # notice the value of version is gone
print( switch.values() ) # notice the value 1.2

print( "Seventh test - ADD a new value" )
switch["adminlogin"] = "karl08"
print( switch.keys() )
print( switch.values() )

print( "Eighth test - ADD a new value" )
switch["password"] = "qwerty"
print( switch.keys() )
print( switch.values() )

