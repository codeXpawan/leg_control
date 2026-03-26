import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/hari-prasad-gajurel/Our_control/leg_control/install/osl_motor'
