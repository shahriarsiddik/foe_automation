from pynput.mouse import Listener
import csv

def on_click(x, y, button, pressed):
    if str(button) == 'Button.left':
        row_contents = [x,y]
        with open('resources.csv', 'a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row_contents)

with Listener(on_click=on_click) as listener:
    listener.join()
