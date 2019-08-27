"""
绘制小猪佩奇
参考turtle绘图介绍
https://docs.python.org/3.6/library/turtle.html?highlight=turtle#turtle.penup
"""
# -*- coding: utf-8 -*-
import turtle as t


def draw_nose():

    t.up()  # 提起笔
    t.goto(-100, 100)  # 定位
    t.down()
    t.seth(-30)  # 设置当前朝向的角度
    t.begin_fill()  # 准备开始填充图形
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a += 0.08
            t.left(3)  # 向左转角度
            t.forward(a)  # 向当前方向移动a的长度
        else:
            a -= 0.08
            t.left(3)  # 向左转角度
            t.forward(a)  # 向当前方向移动a的长度
    t.end_fill()  # 填充完成
    t.up()
    t.seth(90)
    t.forward(25)
    t.seth(0)
    t.fd(10)
    t.pd()
    t.seth(10)
    t.begin_fill()
    t.circle(5)
    t.fillcolor(160, 82, 45)  # 棕色，设置填充颜色
    t.end_fill()
    t.pu()
    t.seth(0)
    t.fd(20)
    t.pd()
    t.seth(10)
    t.begin_fill()
    t.circle(5)
    t.end_fill()


def draw_head():
    t.color((255, 155, 192), "pink")
    t.pu()
    t.seth(90)
    t.fd(41)
    t.seth(0)
    t.pd()
    t.begin_fill()
    t.seth(180)
    t.circle(300, -30)
    t.circle(100, -60)
    t.circle(80, -100)
    t.circle(150, -20)
    t.circle(60, -95)
    t.seth(161)
    t.circle(-300, 15)
    t.pu()
    t.goto(-100, 100)
    t.pd()
    t.seth(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a += 0.08
            t.lt(3)
            t.fd(a)
        else:
            a -= 0.08
            t.lt(3)
            t.fd(a)
    t.end_fill()


def drawl_ears():
    t.pu()
    t.seth(90)
    t.fd(-7)
    t.seth(0)
    t.fd(70)
    t.begin_fill()
    t.pd()
    t.seth(100)
    t.circle(-50, 50)
    t.circle(-10, 120)
    t.circle(-50, 54)
    t.end_fill()
    t.pu()
    t.seth(-90)
    t.fd(12)
    t.seth(0)
    t.fd(30)
    t.pd()
    t.begin_fill()
    t.seth(100)
    t.circle(-50, 50)
    t.circle(-10, 120)
    t.circle(-50, 56)
    t.end_fill()


def draw_eyes():

    # 画第一只眼睛

    t.color((255, 155, 192), "white")
    t.pu()
    t.seth(90)
    t.fd(-20)
    t.seth(0)
    t.fd(-95)
    t.pd()
    t.begin_fill()
    t.circle(15, 360)
    t.end_fill()
    t.color("black")
    t.pu()
    t.seth(90)
    t.fd(12)
    t.seth(0)
    t.fd(-3)
    t.pd()
    t.begin_fill()
    t.circle(3)
    t.end_fill()

    # 画第二只眼睛

    t.color((255, 155, 192), "white")
    t.pu()
    t.seth(90)
    t.fd(-25)
    t.seth(0)
    t.fd(40)
    t.pd()
    t.begin_fill()
    t.circle(15, 360)
    t.end_fill()
    t.color("black")
    t.pu()
    t.seth(90)
    t.fd(12)
    t.seth(0)
    t.fd(-3)
    t.pd()
    t.begin_fill()
    t.circle(3)
    t.end_fill()


def draw_cheek():
    t.color(255, 155, 192)
    t.pu()
    t.seth(90)
    t.fd(-100)
    t.seth(0)
    t.fd(60)
    t.pd()
    t.begin_fill()
    t.circle(30)
    t.end_fill()


def draw_mouse():
    t.pencolor((239, 64, 64))
    t.pu()
    t.seth(90)
    t.fd(15)
    t.seth(0)
    t.fd(-100)
    t.pd()
    t.seth(-80)
    t.circle(30, 40)
    t.circle(40, 80)


def draw_body():
    t.color((255, 99, 71), "red")
    t.pu()
    t.seth(90)
    t.fd(-20)
    t.seth(0)
    t.fd(-71)
    t.pd()
    t.begin_fill()
    t.seth(-130)
    t.circle(100, 10)
    t.circle(300, 29)
    t.seth(0)
    t.fd(230)
    t.seth(90)
    t.circle(300, 30)
    t.circle(100, 5)
    t.color((255, 155, 192), (255, 100, 100))
    t.seth(-135)
    t.circle(-80, 58)
    t.circle(-180, 21)
    t.end_fill()


def drawl_hands():
    # 左手
    t.color((255, 155, 192))
    t.pu()
    t.seth(90)
    t.fd(-45)
    t.seth(0)
    t.fd(-25)
    t.pd()
    t.seth(-160)
    t.circle(300, 15)
    t.pu()
    t.seth(90)
    t.fd(15)
    t.pd()
    t.seth(-10)
    t.circle(-20, 90)

    # 右手
    t.pu()
    t.seth(90)
    t.fd(30)
    t.seth(0)
    t.fd(240)
    t.pd()
    t.seth(-20)
    t.circle(-300, 15)
    t.pu()
    t.seth(90)
    t.fd(20)
    t.pd()
    t.seth(-170)
    t.circle(20, 90)


def draw_legs():

    # 画左腿

    t.pensize(10)
    t.color((255, 110, 147))
    t.pu()
    t.seth(90)
    t.fd(-68)
    t.seth(0)
    t.fd(-180)
    t.pd()
    t.seth(-90)
    t.fd(40)
    t.seth(-180)
    t.color("black")
    t.pensize(15)
    t.fd(20)

    # 画右腿

    t.pensize(10)
    t.color((255, 110, 147))
    t.pu()
    t.seth(90)
    t.fd(40)
    t.seth(0)
    t.fd(90)
    t.pd()
    t.seth(-90)
    t.fd(40)
    t.seth(-180)
    t.color("black")
    t.pensize(15)
    t.fd(20)


def draw_tail():
    t.pensize(4)
    t.color((255, 155, 192))
    t.pu()
    t.seth(90)
    t.fd(70)
    t.seth(0)
    t.fd(95)
    t.pd()
    t.seth(0)
    t.circle(70, 20)
    t.circle(10, 330)
    t.circle(70, 30)


def main():
    """
    主函数
    """
    t.pensize(4)
    t.colormode(255)
    t.color((255, 155, 192), "pink")
    t.setup(840, 800)
    t.speed(50)

    draw_nose()
    draw_head()
    drawl_ears()
    draw_eyes()
    draw_cheek()
    draw_mouse()
    draw_body()
    drawl_hands()
    draw_legs()
    draw_tail()

    t.exitonclick()


if __name__ == '__main__':
    main()
