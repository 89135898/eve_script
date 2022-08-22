import time

import win32gui

from logistics_tasks.logistics import Logistics

if __name__ == "__main__":
    image_name = "test.png"

    time.sleep(5)
    hwnd = win32gui.FindWindow(None, "星战前夜：晨曦 - 我变强了")

    while True:
        # 离站
        Logistics.leave_the_station(hwnd, image_name)

        # 打开星际代理人面板
        Logistics.open_logistics_agent(hwnd, image_name)

        # 赶路
        Logistics.go_to_the_road(hwnd, image_name)

        # 接任务
        Logistics.accept_task(hwnd, image_name)

        # 打开背包
        Logistics.open_bag(hwnd, image_name)

        # 移动任务道具至背包
        Logistics.move_task_prop_to_bag(hwnd, image_name)

        # 离站
        Logistics.leave_the_station(hwnd, image_name)

        # 关闭背包面板
        Logistics.close_bag(hwnd, image_name)

        # 赶路
        Logistics.go_to_the_road(hwnd, image_name)

        # 关闭背包
        Logistics.close_bag(hwnd, image_name)

        # 关闭代理人面板
        Logistics.close_logistics_agent(hwnd, image_name)

        # 交任务
        Logistics.complete_task(hwnd, image_name)
