from lifx import get_lifx_bulb
import time
from tqdm import tqdm
from main import convert_to_hsv

colors = {
    "RED": [65535, 65535, 65535, 3500],
    "ORANGE": [6500, 65535, 65535, 3500],
    "YELLOW": [9000, 65535, 65535, 3500],
    "GREEN": [16173, 65535, 65535, 3500],
    "CYAN": [29814, 65535, 65535, 3500],
    "BLUE": [43634, 65535, 65535, 3500],
    "PURPLE": [50486, 65535, 65535, 3500],
    "PINK": [58275, 65535, 47142, 3500],
    # "WHITE": [58275, 0, 65535, 5500],
    # "COLD_WHITE": [58275, 0, 65535, 9000],
    # "WARM_WHITE": [58275, 0, 65535, 3200],
    # "GOLD": [58275, 0, 65535, 2500]
}

bulb = get_lifx_bulb()

for name, color in colors.items():
    print("Setting {}".format(name))
    bulb.set_color(color, 100)
    time.sleep(1)
    # break

# for i in tqdm(range(0, 65536, 100)):
#     bulb.set_color([65535, 65535, i, 3500], 10)
#     time.sleep(0.01)

# for i in range(256):
#     # [b,g,r]
rgb_color = [0, 51, 0, 0]
color = convert_to_hsv(rgb_color)
print(rgb_color, color)
bulb.set_color(color, 10)
time.sleep(0.01)

# TODO: Fix 'good' colours list and use it for KNN for average colour
