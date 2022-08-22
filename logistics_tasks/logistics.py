import time

from logistics_tasks.helper import Helper


class Logistics:
    def __init__(self):
        pass

    # 离站
    @staticmethod
    def leave_the_station(hwnd, image_name):
        # 离站
        while True:
            Helper.move_to_00()
            Helper.screen_shot(hwnd, image_name)
            rectangle = Helper.find_image_position("target/leave_station.png", image_name, hwnd)
            if rectangle is None:
                break
            else:
                Helper.mouse_left_click(rectangle)
                print("离站中...")
                time.sleep(15)
        # 离站完成标志
        time.sleep(2)
        while True:
            Helper.screen_shot(hwnd, image_name)
            rectangle = Helper.find_image_position("target/departure_completed_flag.png", image_name, hwnd)
            if rectangle is not None:
                break
            else:
                time.sleep(2)
                print("等待...")
        time.sleep(2)
        print("离站完成")

    # 赶路
    @staticmethod
    def go_to_the_road(hwnd, image_name):
        Helper.move_to_00()
        Helper.screen_shot(hwnd, image_name)
        rectangle = Helper.find_image_position("target/task_end_point.png", image_name, hwnd)
        if rectangle is None:
            time.sleep(1)
            Helper.screen_shot(hwnd, image_name)
            rectangle = Helper.find_image_position("target/dock.png", image_name, hwnd)
            time.sleep(1)
            Helper.mouse_left_click(rectangle)
            time.sleep(1)

            print("当前星系直接停靠...")
        else:
            # 设为终点
            Logistics.set_end_point(hwnd, image_name)
            while True:
                Helper.screen_shot(hwnd, image_name)
                print("开始赶路...")
                # 开启自动导航
                if Helper.find_image_position("target/departure_completed_flag.png", image_name, hwnd) is not None:
                    Helper.keyboard_input_combination(17, 83)
                    break
        while True:
            Helper.screen_shot(hwnd, image_name)
            rectangle = Helper.find_image_position("target/leave_station.png", image_name, hwnd)
            if rectangle is None:
                time.sleep(5)
                print('赶路中...')
            else:
                print('到站...')
                return
        time.sleep(1)

    # 打开物流代理人界面
    @staticmethod
    def open_logistics_agent(hwnd, image_name):
        Helper.move_to_00()
        Helper.screen_shot(hwnd, image_name)
        rectangle = Helper.find_image_position("target/task_title.png", image_name, hwnd)
        if rectangle is None:
            Helper.keyboard_input_combination(18, 77)
            time.sleep(5)

        Helper.screen_shot(hwnd, image_name)
        rectangle = Helper.find_image_position("target/task_first.png", image_name, hwnd)
        if rectangle is not None:
            Helper.mouse_left_click(rectangle)
            while True:
                Helper.screen_shot(hwnd, image_name)
                if Helper.find_image_position("target/task_first.png", image_name, hwnd) is None:
                    break
                else:
                    print("接任务中...")
                    time.sleep(1)

        time.sleep(1)
        Helper.screen_shot(hwnd, image_name)
        rectangle = Helper.find_image_position('target/task_second.png', image_name, hwnd)
        if rectangle is not None:
            Helper.mouse_left_click(rectangle)
            while True:
                Helper.screen_shot(hwnd, image_name)
                if Helper.find_image_position('target/task_second.png', image_name, hwnd) is None:
                    break
                else:
                    print("接任务中...")
                    time.sleep(1)

        time.sleep(1)
        Helper.screen_shot(hwnd, image_name)
        rectangle = Helper.find_image_position('target/task_third.png', image_name, hwnd)
        if rectangle is not None:
            Helper.mouse_left_click(rectangle)
            while True:
                Helper.screen_shot(hwnd, image_name)
                if Helper.find_image_position('target/task_third', image_name, hwnd) is None:
                    break
                else:
                    print("接任务中...")
                    time.sleep(1)
    # 关闭代理人面板
    @staticmethod
    def close_logistics_agent(hwnd, image_name):
        Helper.move_to_00()
        count = 0
        time.sleep(1)
        while count > 5:
            Helper.screen_shot(hwnd, image_name)
            rectangle = Helper.find_image_position("target/task_title.png", image_name, hwnd)
            if rectangle is not None:
                time.sleep(1)
                Helper.keyboard_input_combination(18, 77)
                print("关闭代理人面板...")
                break
            else:
                count = count + 1
                time.sleep(1)

    # 接任务
    @staticmethod
    def accept_task(hwnd, image_name):
        Helper.move_to_00()
        # 等待界面绘制完成
        while True:
            Helper.screen_shot(hwnd, image_name)
            time.sleep(1)
            if Helper.find_image_position("target/open_task.png", image_name, hwnd) is not None:
                break
            elif Helper.find_image_position("target/task_target.png", image_name, hwnd) is not None:
                break

        # 点击任务NPC
        Helper.screen_shot(hwnd, image_name)
        rectangle = Helper.find_image_position("target/task_target.png", image_name, hwnd)
        Helper.mouse_left_click(rectangle)
        time.sleep(1)

        Helper.screen_shot(hwnd, image_name)
        rectangle = Helper.find_image_position("target/open_task.png", image_name, hwnd)
        time.sleep(1)
        Helper.mouse_left_click(rectangle)
        print('开始对话...')
        time.sleep(3)

        Helper.screen_shot(hwnd, image_name)
        rectangle = Helper.find_image_position("target/accept_task.png", image_name, hwnd)
        if rectangle is not None:
            time.sleep(1)
            Helper.mouse_left_click(rectangle)
            print('接任务...')
        time.sleep(2)

        # 获取任务道具图片
        Logistics.get_goods_image(hwnd, image_name)

        time.sleep(2)
        Helper.screen_shot(hwnd, image_name)
        rectangle = Helper.find_image_position("target/close_task.png", image_name, hwnd)
        Helper.mouse_left_click(rectangle)
        print('关闭对话...')

    # 移动任务道具到背包
    @staticmethod
    def move_task_prop_to_bag(hwnd, image_name):
        while True:
            Helper.move_to_00()
            # 点击物品机库
            time.sleep(5)
            Helper.screen_shot(hwnd, image_name)
            rectangle = Helper.find_image_position("target/item_hangar.png", image_name, hwnd)
            Helper.mouse_left_click(rectangle)
            print("点击机库...")
            time.sleep(1)
            # 点击任务道具
            Helper.screen_shot(hwnd, image_name)
            rectangle = Helper.find_image_position("target/task_props.png", image_name, hwnd)
            if rectangle is None:
                break
            Helper.mouse_left_click(rectangle)
            time.sleep(1)
            print("点击任务道具...")
            Helper.move_to_00()
            time.sleep(1)
            # 移动到船舱
            Helper.screen_shot(hwnd, image_name)
            rectangle = Helper.find_image_position("target/task_props.png", image_name, hwnd)
            moveToRectangle = Helper.find_image_position("target/hangar.png", image_name, hwnd)
            moveToRectangle[2] = moveToRectangle[2] + 40
            Helper.mouse_left_drag(rectangle, moveToRectangle)
            time.sleep(1)
            print("移动任务道具到船舱...")

    # 交任务
    @staticmethod
    def complete_task(hwnd, image_name):
        Helper.move_to_00()
        # 等待界面绘制完成
        while True:
            Helper.screen_shot(hwnd, image_name)
            time.sleep(1)
            if Helper.find_image_position("target/open_task.png", image_name, hwnd) is not None:
                break
            elif Helper.find_image_position("target/task_target.png", image_name, hwnd) is not None:
                break

        # 点击任务NPC
        Helper.screen_shot(hwnd, image_name)
        rectangle = Helper.find_image_position("target/task_target.png", image_name, hwnd)
        if rectangle is not None:
            Helper.mouse_left_click(rectangle)
            time.sleep(2)
        # 开始对话
        Helper.screen_shot(hwnd, image_name)
        rectangle = Helper.find_image_position("target/open_task.png", image_name, hwnd)
        Helper.mouse_left_click(rectangle)
        print("开始对话...")
        time.sleep(2)
        # 完成任务
        Helper.screen_shot(hwnd, image_name)
        rectangle = Helper.find_image_position("target/complete_task.png", image_name, hwnd)
        Helper.mouse_left_click(rectangle)
        time.sleep(2)
        print("完成任务...")

        time.sleep(2)
        Helper.screen_shot(hwnd, image_name)
        rectangle = Helper.find_image_position("target/close_task.png", image_name, hwnd)
        Helper.mouse_left_click(rectangle)
        print('关闭对话...')

    # 获取货物图片
    @staticmethod
    def get_goods_image(hwnd, image_name):
        Helper.move_to_00()

        # 找到货物
        Helper.screen_shot(hwnd, image_name)
        rectangle = Helper.find_image_position("target/freight.png", image_name, hwnd)

        targetRectangle = [rectangle[0]-30, rectangle[1], rectangle[0] - 15, rectangle[1]+20]
        # 打开货物信息
        Helper.mouse_left_click(targetRectangle)

        time.sleep(5)
        # 获取货物截图
        Helper.screen_shot(hwnd, image_name)
        rectangle = Helper.find_image_position("target/attributes.png", image_name, hwnd)
        # 找到属性按钮，向上截取货物信息
        rectangle = [rectangle[0]-30, rectangle[1]-70, rectangle[0]+5, rectangle[1]-25]
        Helper.screen_shot(hwnd, 'target/task_props.png', rectangle)

        # 关闭货物信息
        Helper.screen_shot(hwnd, image_name)
        rectangle = Helper.find_image_position("target/task_props.png", image_name, hwnd)
        rectangle[0] = rectangle[2] + 20
        rectangle[2] = rectangle[2] + 60
        Helper.mouse_right_click(rectangle)
        time.sleep(1)
        Helper.screen_shot(hwnd, image_name)
        rectangle = Helper.find_image_position("target/close_window.png", image_name, hwnd)
        Helper.mouse_left_click(rectangle)
        time.sleep(2)

    # 设置终点
    @staticmethod
    def set_end_point(hwnd, image_name):
        Helper.move_to_00()

        # 点击任务NPC
        time.sleep(1)
        Helper.screen_shot(hwnd, image_name)
        rectangle = Helper.find_image_position("target/task_target.png", image_name, hwnd)
        if rectangle is not None:
            Helper.mouse_left_click(rectangle)

        count = 0
        while count < 5:
            Helper.screen_shot(hwnd, image_name)
            rectangle = Helper.find_image_position("target/task_end_point.png", image_name, hwnd)
            if rectangle is not None:
                Helper.mouse_left_click(rectangle)
                break
            else:
                count = count + 1
                time.sleep(2)

    # 关闭背包
    @staticmethod
    def close_bag(hwnd, image_name):
        cont = 0
        Helper.move_to_00()
        while cont < 5:
            Helper.screen_shot(hwnd, image_name)
            rectangle = Helper.find_image_position("target/bag.png", image_name, hwnd)
            if rectangle is not None:
                Helper.keyboard_input_combination(18, 67)
                break
            else:
                cont = cont + 1
                time.sleep(1)
        time.sleep(1)

    # 打开背包
    @staticmethod
    def open_bag(hwnd, image_name):
        cont = 0
        Helper.move_to_00()
        while cont < 5:
            Helper.screen_shot(hwnd, image_name)
            rectangle = Helper.find_image_position("target/bag.png", image_name, hwnd)
            if rectangle is None:
                Helper.keyboard_input_combination(18, 67)
                break
            else:
                cont = cont + 1
                time.sleep(1)