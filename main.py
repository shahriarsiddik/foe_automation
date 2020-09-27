import pyautogui
import time
import webbrowser
import keyboard

new = 2 # open in a new tab, if possible

resource_coords = [(2762, 670), (2805, 649), (2827, 603),
                   (2761, 630), (2713, 650), (2677, 644),
                   (2642, 616), (2576, 594), (2616, 567),
                   (2610, 486), (2529, 466), (2474, 493),
                   (2428, 519), (2418, 469), (2772, 583),
                   (2737, 556), (2717, 612), (2687, 593),
                   (2810, 652), (2566, 599), (2508, 610),
                   (2656, 508), (2460, 503), (2429, 517),
                   (2681, 593), (2775, 579), (2847, 685),
                   (2682, 532), (2540, 534), (2490, 567),
                   (2327, 532), (2482, 432), (2490, 432)]


def open_game():
    url = "https://en4.forgeofempires.com/game/index?"
    new = 2
    webbrowser.get(using='google-chrome').open(url,new=new)




def fake_click():
    pyautogui.click(2590, 853)

def click_to_discard_popup():
    pyautogui.click(2586, 850)


def click_to_collect(x, y):
    pyautogui.click(x, y)

def collect_resources(res_coord):
    for i in range(len(res_coord)):
        click_to_collect(res_coord[i][0], res_coord[i][1])
        print("---resource--collected----")
        time.sleep(0.3)
        fake_click()
        print("---fake--click---")

for timer in range(10000):
    open_game()
    time.sleep(7)
    fake_click()
    collect_resources(resource_coords)
    print("last collection time " + str(time.time()))
    time.sleep(120)
    # keyboard.press_and_release('ctrl+w')

