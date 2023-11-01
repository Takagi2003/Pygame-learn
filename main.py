import pygame   # 导入pygame模块

# 设置需要的模块大小
HIGHT = 400
WIGHT = 300
# 初始化，一定不能忘记
pygame.init()
# 创建一个window对象
window = pygame.display.set_mode((WIGHT, HIGHT))
# 该程序框显示的名字
pygame.display.set_caption("这是一个pygame程序")
# 对window对象进行颜色的填充，格式是R G B，现在是进行白色的填充
window.fill((255, 255, 255))
# 进行刷新，不然不会显示，第一次进行刷新使用这个，后面的都使用pygame.display.update()
pygame.display.flip()


while True:
    # 对输入或者操作的任何一个事件进行循环
    for event in pygame.event.get():
        # 如果检测到按下左上角叉，这结束此程序，exit()只会退出一个线程，如后面添加更过模块exit()可能会导致无法退出
        if event.type ==pygame.QUIT:
            exit()
    # 进行刷新
    pygame.display.update()