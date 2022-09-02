import ctypes
import time
import ctypes.wintypes

import numpy as np
import pyautogui
import win32con
import win32gui
import win32ui
import win32api
import cv2


class Helper:

    def __init__(self):
        pass

    # 窗口截屏
    @staticmethod
    def screen_shot(hwnd, image_name, rectangle=None):
        if rectangle is None:
            left, top, right, bottom = win32gui.GetWindowRect(hwnd)
            # 获取句柄窗口大小
            width = right - left
            height = bottom - top
        else :
            left, top, right, bottom = rectangle
            width = right - left
            height = bottom - top
        img = pyautogui.screenshot(region=(left, top, width, height))
        img.save(image_name)

        # 返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
        # hWnDc = win32gui.GetWindowDC(hwnd)
        # # 创建设备描述表
        # mfcDC = win32ui.CreateDCFromHandle(hWnDc)
        # # 创建内存设备描述表
        # saveDC = mfcDC.CreateCompatibleDC()
        # # 创建位图对象
        # saveBitMap = win32ui.CreateBitmap()
        # # 获取客户端窗口大小
        # # windowWidth, windowHeight = win32gui.GetClientRect(hwnd)[2:]
        # # 创建与设备描述表兼容的位图对象
        # saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
        # # 将截图保存到saveBitMap中
        # saveDC.SelectObject(saveBitMap)
        # # 截取从左上角（0，0）长宽为（w，h）的图片
        # saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)
        # saveBitMap.SaveBitmapFile(saveDC, 'test.png')
        # # signed_ints_array = saveBitMap.GetBitmapBits(True)
        # # Free Resources
        # # 释放资源
        # saveDC.DeleteDC()
        # mfcDC.DeleteDC()
        # win32gui.ReleaseDC(hwnd, hWnDc)
        # win32gui.DeleteObject(saveBitMap.GetHandle())

    # 获取所有窗口信息
    @staticmethod
    def find_all_window():
        hWnd_list = []
        win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWnd_list)
        for cwnd in hWnd_list:
            if win32gui.IsWindowVisible(cwnd):
                print(win32gui.GetWindowText(cwnd))
                print(win32gui.GetClassName(cwnd))
                print(win32gui.GetWindowRect(cwnd))
                print('\n')

    # 获取目标随机坐标
    @staticmethod
    def get_random_position(rectangle):
        # 缩小范围
        scaleX = (rectangle[2] - rectangle[0]) * 0.1
        scaleY = (rectangle[3] - rectangle[1]) * 0.1
        x = np.random.randint(rectangle[0]+scaleX, rectangle[2]-scaleX)
        y = np.random.randint(rectangle[1]+scaleY, rectangle[3]-scaleY)
        return x-9, y-9

    # 鼠标左击
    @staticmethod
    def mouse_left_click(rectangle):
        x, y = Helper.get_random_position(rectangle)

        win32api.SetCursorPos((x, y))
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        # 随机休眠
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    # 鼠标右击
    @staticmethod
    def mouse_right_click(rectangle):
        x, y = Helper.get_random_position(rectangle)
        win32api.SetCursorPos((x, y))
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
        # 随机休眠
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

    # 左键拖拽
    @staticmethod
    def mouse_left_drag(rectangle, moveToRectangle):
        x, y = Helper.get_random_position(rectangle)
        move_to_x, move_to_y = Helper.get_random_position(moveToRectangle)

        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.2)
        win32api.SetCursorPos((move_to_x, move_to_y))
        time.sleep(0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    # 右键拖拽
    @staticmethod
    def mouse_right_drag(rectangle, moveToRectangle):
        x, y = Helper.get_random_position(rectangle)
        move_to_x, move_to_y = Helper.get_random_position(moveToRectangle)
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
        # 随机休眠
        time.sleep(np.random.rand() * 0.5)
        win32api.SetCursorPos((move_to_x, move_to_y))
        # 随机休眠
        time.sleep(np.random.rand() * 0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

    # 左键双击
    @staticmethod
    def mouse_left_double_click(rectangle):
        x, y = Helper.get_random_position(rectangle)
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        # 随机休眠
        time.sleep(np.random.rand() * 0.25)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        # 随机休眠
        time.sleep(np.random.rand() * 0.25)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        # 随机休眠
        time.sleep(np.random.rand() * 0.25)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

    # 右键双击
    @staticmethod
    def mouse_right_double_click(rectangle):
        x, y = Helper.get_random_position(rectangle)
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
        # 随机休眠
        time.sleep(np.random.rand() * 0.25)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)
        # 随机休眠
        time.sleep(np.random.rand() * 0.25)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
        # 随机休眠
        time.sleep(np.random.rand() * 0.25)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)

    # 键盘输入
    @staticmethod
    def keyboard_input(key):
        win32api.keybd_event(key, 0, 0, 0)
        # 随机休眠
        time.sleep(np.random.rand() * 0.25)
        win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)

    # 键盘输入组合键
    @staticmethod
    def keyboard_input_combination(key1, key2):
        time.sleep(1)
        win32api.keybd_event(key1, 0, 0, 0)
        time.sleep(0.1)
        win32api.keybd_event(key2, 0, 0, 0)
        time.sleep(0.1)
        win32api.keybd_event(key2, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.5)
        win32api.keybd_event(key1, 0, win32con.KEYEVENTF_KEYUP, 0)

    # 找到目标图片坐标
    @staticmethod
    def find_image_position(image, target_image, hwnd):
        # 图像类型转换
        img_target = cv2.imread(target_image)
        img = cv2.imread(image)
        # 图像模板匹配
        result = cv2.matchTemplate(img, img_target, cv2.TM_CCOEFF_NORMED)
        # 匹配结果转换为二维数组
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        # 获取匹配结果中最大的坐标
        print(image, max_val)
        if max_val > 0.8:
            startX, startY = max_loc
            endX, endY = (startX + img.shape[1], startY + img.shape[0])
            if False:
                # rectangle = [startX, startY, endX, endY]
                # rectangle = [rectangle[0] - 5, rectangle[1] - 70, rectangle[2] - 5, rectangle[1] - 10]
                # rectangle = [rectangle[0], rectangle[1]-65, rectangle[2]-10, rectangle[1]-15]
                # rectangle = [rectangle[0]+5, rectangle[1]-60, rectangle[2]-15, rectangle[1]-20]
                # rectangle = [rectangle[0]+10, rectangle[1] - 55, rectangle[2] - 20, rectangle[1] - 25]
                # cv2.rectangle(img_target, (rectangle[0], rectangle[1]), (rectangle[2], rectangle[3]), (0, 0, 255), 2)

                cv2.rectangle(img_target, (startX, startY), (endX, endY), (0, 255, 255),
                              2)
                cv2.imshow('result', img_target)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

            return Helper.convert_position([startX, startY, endX, endY], hwnd)
        else:
            return None

    # 转换坐标
    @staticmethod
    def convert_position(targetRect, hwnd):
        try:
            f = ctypes.windll.dwmapi.DwmGetWindowAttribute
        except WindowsError:
            f = None
        if f:
            rect = ctypes.wintypes.RECT()
            DWMWA_EXTENDED_FRAME_BOUNDS = 9
            f(ctypes.wintypes.HWND(hwnd),
              ctypes.wintypes.DWORD(DWMWA_EXTENDED_FRAME_BOUNDS),
              ctypes.byref(rect),
              ctypes.sizeof(rect)
              )

            return [targetRect[0] + rect.left, targetRect[1] + rect.top, targetRect[2] + rect.left,
                    targetRect[3] + rect.top]
        else:
            return targetRect

    # 鼠标移动
    @staticmethod
    def mouse_move(x, y):
        win32api.SetCursorPos((x, y))
        time.sleep(0.5)

    # 鼠标移动到00点
    @staticmethod
    def move_to_00():
        time.sleep(1)
        win32api.SetCursorPos((0, 0))
        time.sleep(0.5)
