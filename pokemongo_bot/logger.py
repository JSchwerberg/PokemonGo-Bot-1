from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
import six
import time

try:
    from . import lcd
    lcd = lcd.lcd()
    # Change this to your i2c address
    lcd.set_addr(0x23)
except Exception:
    lcd = False


def log(string, color='white'):
    color_hex = {
        'red': '91m',
        'green': '92m',
        'yellow': '93m',
        'blue': '94m',
        'cyan': '96m'
    }
    if color not in color_hex:
        print('[{time}] {string}'.format(
            time=time.strftime("%H:%M:%S"),
            string=string.decode('utf-8') if six.PY2 \
                   else string
        ))
    else:
        print(
            '[{time}] \033[{color} {string} \033[0m'.format(
                time=time.strftime("%H:%M:%S"),
                color=color_hex[color],
                string=string.decode('utf-8') if six.PY2 \
                       else string
            )
        )
    if lcd:
        if string:
            lcd.message(string)
