# ItsJarik

import blynklib

BLYNK_AUTH = '3cQIWyxYKPUK6j4U1u2U5NIvjyYG5g9X'

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH, server='192.168.2.6', port=8080)

WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"


# register handler for virtual pin V4 write event
@blynk.handle_event('write V0')
def write_virtual_pin_handler(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))

# register handler for virtual pin V4 write event
@blynk.handle_event('write V4')
def write_virtual_pin_handler(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))


###########################################################
# infinite loop that waits for event
###########################################################
while True:
    blynk.run()
