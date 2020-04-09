import tkinter as tk
from PIL import Image, ImageTk
from time import time, sleep
from random import choice, uniform, randint
from math import sin, cos, radians

# 模拟重力
GRAVITY = 0.05
# 颜色选项（随机或者按顺序）
colors = ['red', 'blue', 'yellow', 'white', 'green', 'orange', 'purple', 'seagreen', 'indigo', 'cornflowerblue']

'''
particles 类

粒子在空中随机生成随机，变成一个圈、下坠、消失

属性:
    - id: 粒子的id
    - x, y: 粒子的坐标
    - vx, vy: 在坐标的变化速度
    - total: 总数
    - age: 粒子存在的时长
    - color: 颜色
    - cv: 画布
    - lifespan: 最高存在时长

'''
# coding:utf-8
import turtle as t
import time
# 皮卡丘
# 基础设置
t.screensize(800, 600)
t.pensize(2)  # 设置画笔的大小
t.speed(10)  # 设置画笔速度为10
# 画左偏曲线函数
def radian_left(ang, dis, step, n):
    for i in range(n):
        dis += step  # dis增大step
        t.lt(ang)  # 向左转ang度
        t.fd(dis)  # 向前走dis的步长
def radian_right(ang, dis, step, n):
    for i in range(n):
        dis += step
        t.rt(ang)  # 向左转ang度
        t.fd(dis)  # 向前走dis的步长
# 画耳朵
def InitEars():
    t.color("black", "yellow")
    # 左耳朵曲线
    t.pu()  # 提笔
    t.goto(-50, 100)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(110)  # 画笔角度
    t.begin_fill()
    radian_left(1.2, 0.4, 0.1, 40)
    t.setheading(270)  # 画笔角度
    radian_left(1.2, 0.4, 0.1, 40)
    t.setheading(44)  # 画笔角度
    t.forward(32)
    t.end_fill()
    # 右耳朵曲线
    t.pu()  # 提笔
    t.goto(50, 100)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(70)  # 画笔角度
    t.begin_fill()
    radian_right(1.2, 0.4, 0.1, 40)
    t.setheading(270)  # 画笔角度
    radian_right(1.2, 0.4, 0.1, 40)
    t.setheading(136)  # 画笔角度
    t.forward(32)
    t.end_fill()
    # 耳朵黑
    t.begin_fill()
    t.fillcolor("black")
    t.pu()  # 提笔
    t.goto(88, 141)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(35)  # 画笔角度
    radian_right(1.2, 1.6, 0.1, 16)
    t.setheading(270)  # 画笔角度
    radian_right(1.2, 0.4, 0.1, 25)
    t.setheading(132)  # 画笔角度
    t.forward(31)
    t.end_fill()
    t.begin_fill()
    t.fillcolor("black")
    t.pu()  # 提笔
    t.goto(-88, 141)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(145)  # 画笔角度
    radian_left(1.2, 1.6, 0.1, 16)
    t.setheading(270)  # 画笔角度
    radian_left(1.2, 0.4, 0.1, 25)
    t.setheading(48)  # 画笔角度
    t.forward(31)
    t.end_fill()
# 画尾巴
def InitTail():
    # 尾巴
    t.begin_fill()
    t.fillcolor("yellow")
    t.pu()  # 提笔
    t.goto(64, -140)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(10)  # 画笔角度
    t.forward(20)
    t.setheading(90)  # 画笔角度
    t.forward(20)
    t.setheading(10)  # 画笔角度
    t.forward(10)
    t.setheading(80)  # 画笔角度
    t.forward(100)
    t.setheading(35)  # 画笔角度
    t.forward(80)
    t.setheading(260)  # 画笔角度
    t.forward(100)
    t.setheading(205)  # 画笔角度
    t.forward(40)
    t.setheading(260)  # 画笔角度
    t.forward(37)
    t.setheading(205)  # 画笔角度
    t.forward(20)
    t.setheading(260)  # 画笔角度
    t.forward(25)
    t.setheading(175)  # 画笔角度
    t.forward(30)
    t.setheading(100)  # 画笔角度
    t.forward(13)
    t.end_fill()
# 画脚
def InitFoots():
    # 脚
    t.begin_fill()
    t.fillcolor("yellow")
    t.pensize(2)
    t.pu()  # 提笔
    t.goto(-70, -200)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(225)  # 画笔角度
    radian_left(0.5, 1.2, 0, 12)
    radian_left(35, 0.6, 0, 4)
    radian_left(1, 1.2, 0, 18)
    t.setheading(160)  # 画笔角度
    t.forward(13)
    t.end_fill()
    t.begin_fill()
    t.fillcolor("yellow")
    t.pensize(2)
    t.pu()  # 提笔
    t.goto(70, -200)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(315)  # 画笔角度
    radian_right(0.5, 1.2, 0, 12)
    radian_right(35, 0.6, 0, 4)
    radian_right(1, 1.2, 0, 18)
    t.setheading(20)  # 画笔角度
    t.forward(13)
    t.end_fill()
# 画身体
def InitBody():
    # 外形轮廓
    t.begin_fill()
    t.pu()  # 提笔
    t.goto(112, 0)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(90)  # 画笔角度
    t.circle(112, 180)
    t.setheading(250)  # 画笔角度
    radian_left(1.6, 1.3, 0, 50)
    radian_left(0.8, 1.5, 0, 25)
    t.setheading(255)  # 画笔角度
    radian_left(0.4, 1.6, 0.2, 27)
    radian_left(2.8, 1, 0, 45)
    radian_right(0.9, 1.4, 0, 31)
    t.setheading(355)  # 画笔角度
    radian_right(0.9, 1.4, 0, 31)
    radian_left(2.8, 1, 0, 45)
    radian_left(0.4, 7.2, -0.2, 27)
    t.setheading(10)  # 画笔角度
    radian_left(0.8, 1.5, 0, 25)
    radian_left(1.6, 1.3, 0, 50)
    t.end_fill()
def InitEyes():
    # 左眼睛
    t.begin_fill()
    t.fillcolor("black")
    t.pu()  # 提笔
    t.goto(-46, 10)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(90)  # 画笔角度
    t.circle(5, 360)
    t.end_fill()
    # 右眼睛
    t.begin_fill()
    t.fillcolor("black")
    t.pu()  # 提笔
    t.goto(46, 10)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(-90)  # 画笔角度
    t.circle(5, 360)
    t.end_fill()
# 画脸
def InitFace():
    # 脸蛋
    t.begin_fill()
    t.fillcolor("red")
    t.pu()  # 提笔
    t.goto(-63, -10)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(90)  # 画笔角度
    t.circle(10, 360)
    t.end_fill()
    t.begin_fill()
    t.fillcolor("red")
    t.pu()  # 提笔
    t.goto(63, -10)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(-90)  # 画笔角度
    t.circle(10, 360)
    t.end_fill()
    # 嘴巴
    t.pensize(2.2)
    t.pu()  # 提笔
    t.goto(0, 0)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(235)  # 画笔角度
    radian_right(5, 0.8, 0, 30)
    t.pu()  # 提笔
    t.goto(0, 0)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(305)  # 画笔角度
    radian_left(5, 0.8, 0, 30)
# 画手
def InitHands():
    # 左手
    t.pensize(2)
    t.pu()  # 提笔
    t.goto(-46, -100)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(285)  # 画笔角度
    radian_right(0.4, 1.2, 0, 26)
    radian_right(5, 0.35, 0, 26)
    radian_right(0.3, 1.2, 0, 15)
    # 右手
    t.pu()  # 提笔
    t.goto(46, -100)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(255)  # 画笔角度
    radian_left(0.4, 1.2, 0, 26)
    radian_left(5, 0.35, 0, 26)
    radian_left(0.3, 1.2, 0, 15)
def CloseEyes():
    # 左眼睛
    t.pu()  # 提笔
    t.goto(-46, 12)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(180)  # 画笔角度
    t.forward(10)
    # 右眼睛
    t.pu()  # 提笔
    t.goto(46, 12)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(0)  # 画笔角度
    t.forward(10)
# 初始化
def Init():
    InitEars()
    InitTail()
    InitFoots()
    InitBody()
    InitFace()
    InitHands()
    InitEyes()
# 眨眼睛
def Upgarde():
    InitEars()
    InitTail()
    InitFoots()
    InitBody()
    InitFace()
    InitHands()
    CloseEyes()
def Upgarde_Init():
    InitEars()
    InitTail()
    InitFoots()
    InitBody()
    InitFace()
    InitHands()
    InitEyes()
def main():
    Init()
    t.tracer(False)
    # 眨眼睛动画
    for i in range(30):
        if i % 2 == 0:
            t.reset()
            t.hideturtle()
            Upgarde()
            t.update()
            time.sleep(0.3)
        else:
            t.reset()
            t.hideturtle()
            Upgarde_Init()
            t.update()
            time.sleep(1)
main()
# 结束画笔



class Particle:

    def __init__(self, cv, idx, total, explosion_speed, x=0., y=0., vx=0., vy=0., size=2., color='red', lifespan=2,
                 **kwargs):
        self.id = idx
        self.x = x
        self.y = y
        self.initial_speed = explosion_speed
        self.vx = vx
        self.vy = vy
        self.total = total
        self.age = 0
        self.color = color
        self.cv = cv
        self.cid = self.cv.create_oval(
            x - size, y - size, x + size,
            y + size, fill=self.color)
        self.lifespan = lifespan

    def update(self, dt):
        self.age += dt

        # 粒子范围扩大
        if self.alive() and self.expand():
            move_x = cos(radians(self.id * 360 / self.total)) * self.initial_speed
            move_y = sin(radians(self.id * 360 / self.total)) * self.initial_speed
            self.cv.move(self.cid, move_x, move_y)
            self.vx = move_x / (float(dt) * 1000)

        # 以自由落体坠落
        elif self.alive():
            move_x = cos(radians(self.id * 360 / self.total))
            # we technically don't need to update x, y because move will do the job
            self.cv.move(self.cid, self.vx + move_x, self.vy + GRAVITY * dt)
            self.vy += GRAVITY * dt

        # 移除超过最高时长的粒子
        elif self.cid is not None:
            cv.delete(self.cid)
            self.cid = None

    # 扩大的时间
    def expand (self):
        return self.age <= 1.2

    # 粒子是否在最高存在时长内
    def alive(self):
        return self.age <= self.lifespan

'''
循环调用保持不停
'''
def simulate(cv):
    t = time()
    explode_points = []
    wait_time = randint(10, 100)
    numb_explode = randint(6, 10)
    # 创建一个所有粒子同时扩大的二维列表
    for point in range(numb_explode):
        objects = []
        x_cordi = randint(50, 550)
        y_cordi = randint(50, 150)
        speed = uniform(0.5, 1.5)
        size = uniform(1, 3)
        color = choice(colors)
        explosion_speed = uniform(0.2, 1)
        total_particles = randint(10, 50)
        for i in range(1, total_particles):
            r = Particle(cv, idx=i, total=total_particles, explosion_speed=explosion_speed, x=x_cordi, y=y_cordi,
                         vx=speed, vy=speed, color=color, size=size, lifespan=uniform(0.6, 1.75))
            objects.append(r)
        explode_points.append(objects)

    total_time = .0
    # 1.8s内一直扩大
    while total_time < 1.8:
        sleep(0.01)
        tnew = time()
        t, dt = tnew, tnew - t
        for point in explode_points:
            for item in point:
                item.update(dt)
        cv.update()
        total_time += dt
    # 循环调用
    root.after(wait_time, simulate, cv)


def close(*ignore):
    """退出程序、关闭窗口"""
    global root
    root.quit()


if __name__ == '__main__':
    root = tk.Tk()
    cv = tk.Canvas(root, height=400, width=600)
    # 绘制一个黑色背景
    cv.create_rectangle(0, 0, 600, 400, fill='black')

    # cv = tk.Canvas(root, height=400, width=600)
    # # 选一个好看的背景会让效果更惊艳！
    # image = Image.open("./image.jpg")
    # photo = ImageTk.PhotoImage(image)
    #
    # cv.create_image(0, 0, image=photo, anchor='nw')
    cv.pack()

    root.protocol("WM_DELETE_WINDOW", close)
    root.after(100, simulate, cv)
    root.mainloop()
