
## EVE 自动物流任务

### 注意事项

> 本软件仅供学习使用，请勿用于商业用途。

### 用到的插件

> pywin32 模拟键鼠操作，窗口绑定

> pyautogui 屏幕截图

> opencv 图像处理和目标识别 

### 使用说明

1. 确保eve游戏窗口可见，并且是可操作能进行快捷键操作
2. 设置eve游戏分辨率为1080*1920 窗口模式
3. 将游戏特效开到最低，确保target中所有图片一致，不然目标图片识别不到。若目标图片识别不到，需要自行截图，截图尽量精确

### target目录下图片说明

1. accept_task.png: 接受任务按钮目标图片
2. attributes.png : 属性-用于找到任务目标图片
3. bag.png 识别背包窗口是否开启
4. close_task.png 关闭任务窗口
5. close_window.png 关闭任务道具属性窗口
6. complete_task.png 完成任务按钮目标图片
7. departure_completed_flag.png 是否在太空中目标图片
8. dock.png 停靠进站按钮
9. freight.png 任务面板货物图片，用于偏移找到任务目标图片，后续单击打开任务目标属性面板，获取任务目标截图
10. hangar.png 舰船库目标图片，用于将背包中任务道具拖到舰船库中
11. item_hangar.png 物品机库目标图片，用于打开物品机库，定位任务道具坐标
12. leave_station.png 离站按钮，用于离站和是否在空间站中标志
13. open_task.png 打开任务窗口目标图片
14. task_end_point.png 设为终点
15. task_first.png 任务面板第一页
16. task_second.png 任务面板第二页
17. task_third.png 任务面板第三页
18. task_props.png 任务道具截图，打开任务道具属性面板后自动截取
19. task_target.png 任务接受npc目标图片,从哪个npc处接任务
20. task_title.png 用于判断是否打开任务面板
