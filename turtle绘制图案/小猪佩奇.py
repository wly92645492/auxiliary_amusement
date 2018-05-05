import turtle as t

'''
2.3 绘图命令

         操纵海龟绘图有着许多的命令，这些命令可以划分为3种：一种为运动命令，一种为画笔控制命令，还有一种是全局控制命令。

(1)    画笔运动命令

命令

说明

turtle.forward(distance)

向当前画笔方向移动distance像素长度

turtle.backward(distance)

向当前画笔相反方向移动distance像素长度

turtle.right(degree)

顺时针移动degree°

turtle.left(degree)

逆时针移动degree°

turtle.pendown()

移动时绘制图形，缺省时也为绘制

turtle.goto(x,y)

将画笔移动到坐标为x,y的位置

turtle.penup()

提起笔移动，不绘制图形，用于另起一个地方绘制

turtle.circle()

画圆，半径为正(负)，表示圆心在画笔的左边(右边)画圆

setx( )

将当前x轴移动到指定位置

sety( )

将当前y轴移动到指定位置

setheading(angle)

设置当前朝向为angle角度

home()

设置当前画笔位置为原点，朝向东。

dot(r)

绘制一个指定直径和颜色的圆点



(2)     画笔控制命令

命令

说明

turtle.fillcolor(colorstring)

绘制图形的填充颜色

turtle.color(color1, color2)

同时设置pencolor=color1, fillcolor=color2

turtle.filling()

返回当前是否在填充状态

turtle.begin_fill()

准备开始填充图形

turtle.end_fill()

填充完成

turtle.hideturtle()

隐藏画笔的turtle形状

turtle.showturtle()

显示画笔的turtle形状



(3)    全局控制命令

命令

说明

turtle.clear()

清空turtle窗口，但是turtle的位置和状态不会改变

turtle.reset()

清空窗口，重置turtle状态为起始状态

turtle.undo()

撤销上一个turtle动作

turtle.isvisible()

返回当前turtle是否可见

stamp()

复制当前图形

turtle.write(s [,font=("font-name",font_size,"font_type")])

写文本，s为文本内容，font是字体的参数，分别为字体名称，大小和类型；font为可选项，font参数也是可选项



(4)    其他命令

命令

说明

turtle.mainloop()或turtle.done()

启动事件循环 -调用Tkinter的mainloop函数。

必须是乌龟图形程序中的最后一个语句。

turtle.mode(mode=None)

设置乌龟模式（“standard”，“logo”或“world”）并执行重置。如果没有给出模式，则返回当前模式。

模式

初始龟标题

正角度

standard

向右（东）

逆时针

logo

向上（北）

顺时针

turtle.delay(delay=None)

设置或返回以毫秒为单位的绘图延迟。

turtle.begin_poly()

开始记录多边形的顶点。当前的乌龟位置是多边形的第一个顶点。

turtle.end_poly()

停止记录多边形的顶点。当前的乌龟位置是多边形的最后一个顶点。将与第一个顶点相连。

turtle.get_poly()

返回最后记录的多边形。

'''

# 设置画笔的宽度
t.pensize(4)

# 隐藏画笔的turtle形状
t.hideturtle()

t.colormode(255)
t.color((255, 155, 192), "pink")
t.setup(840, 500)
# 设置画笔移动速度，画笔绘制的速度范围[0,10]整数，数字越大越快
t.speed(10)




# 尾巴
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
