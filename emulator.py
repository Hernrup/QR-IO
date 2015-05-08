from subprocess import call
from os.path import join, abspath

sdk_path = abspath(join('f', 'dev', 'Android', 'sdk'))
image_name = 'Nexus_5_API_22_x86'

call([abspath(join(sdk_path, 'tools', 'emulator.exe')),
      '-scale', 0.5, '-netdelay', 'none', '-netspeed', 'full', '-avd', image_name])


# $ export AP_PORT=4321  # Use set AP_PORT=9999 on Windows
# $ export AP_HOST=192.168.0.100  # Use set AP_HOST=192.168.0.100 on Windows