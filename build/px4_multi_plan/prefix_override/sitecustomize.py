import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/maav/px4_multi_vehicle_offboard/install/px4_multi_plan'
