import pyautogui as pg 
import time
import random
#from Path.xyCoor import x_y_Coors
import keyboard as key

#time.sleep(7)
#pos = pg.position()
#print(pos)

pg.leftClick(x=1213,y=6) 
time.sleep(1)
key.press_and_release('delete')
time.sleep(1)
key.write("IG-LPS-BOT")
time.sleep(1)
pg.leftClick(x=954, y=466)


x_y_Coors = {
    1: "x=689, y=230",
    2: "x=793, y=224",
    3: "x=912, y=226",
    4: "x=1021, y=220",
    5: "x=689, y=339",
    6: "x=1136, y=233",
    7: "x=804, y=346",
}
time.sleep(2)
selected_coordinates = []
for i in range(1):
    rand_key = random.choice(list(x_y_Coors.keys()))
    coordinates = x_y_Coors[rand_key].strip()  # Remove leading/trailing spaces
    selected_coordinates.append(coordinates)
    x_y_Coors.pop(rand_key)

for coordinates in selected_coordinates:
    try:
        x, y = [int(coord.split('=')[1]) for coord in coordinates.split(',')]
    except ValueError:
        print(f"Invalid format for coordinates: {coordinates}")
        continue
    time.sleep(2)
    pg.leftClick(x, y)
    time.sleep(2)
    # Drag to the coordinates using the left mouse button with increased duration
    pg.dragTo(x=625, y=434, button='left', duration=1.5)
    time.sleep(2)

