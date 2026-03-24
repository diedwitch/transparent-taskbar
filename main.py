import win32gui
import win32con

taskbar = win32gui.FindWindow("Shell_TrayWnd", None)

style = win32gui.GetWindowLong(taskbar, win32con.GWL_EXSTYLE)
win32gui.SetWindowLong(taskbar, win32con.GWL_EXSTYLE, style | win32con.WS_EX_LAYERED)

# 0 = fully transparent, 255 = solid
win32gui.SetLayeredWindowAttributes(taskbar, 0, 0, win32con.LWA_ALPHA)
