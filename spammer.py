# This is spammer.py. You can spam the whole text.txt file with it, in just a few lines of python.
# Fill in the text.txt file with the things that you want to spam, set the time between the
# individual paragraphs by editing the "time.sleep(YOUR_TIME)" element (I have it set to 3 seconds
# right now). Then press start and quickly head over to the place, you want to spam in.


import pyautogui, time

print("Starting...")
time.sleep(3)
f = open("text", 'r')
for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")

