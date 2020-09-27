import Xlib
import Xlib.display
import time

# def main():
#     display = Xlib.display.Display(':0')
#     root = display.screen().root
#     root.change_attributes(event_mask=
#         Xlib.X.ButtonPressMask | Xlib.X.ButtonReleaseMask)
#
#     while True:
#         print("this is it")
#         event = root.display.next_event()
#         print(event)
#
# if __name__ == "__main__":
#     main()


# for i in range(1000):
#     time.sleep(1)
#     data = display.Display().screen().root.query_pointer()._data
#     print((data["root_x"], data["root_y"]))

# from Xlib import X
# from Xlib.display import Display
# from Xlib.ext.xtest import fake_input
# d = Display()
# fake_input(d, X.ButtonPress, 1)
# d.sync()
# fake_input(d, X.ButtonRelease, 1)
# d.sync()

from pynput.mouse import Controller

mouse = Controller()





















