import pyautogui

position = pyautogui.position()
print(position)

# # ##################################
# # moveTo: Move to absolute position
# # move: Move to relative position
# # pyautogui.click(clicks=2) => Double click
# pyautogui.moveTo(171, 275, duration=1)
# pyautogui.click()

# pyautogui.moveTo(148, 230, duration=2)
# pyautogui.click()

# pyautogui.moveTo(2451, 48, duration=1)
# pyautogui.click()


# ####################################
# Right-click on window
# We can give location params with click function
pyautogui.click(171, 275, button='right')
