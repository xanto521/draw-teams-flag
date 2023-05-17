# 导入turtle库
import turtle
 
# 设置窗口大小及初始位置
turtle.setup(1200, 800,)
# 设置画笔粗细
turtle.pensize(2)
# 设置画笔颜色
# turtle.pencolor("red")
# 画笔向右旋转90°
turtle.right(90)
# 提起画笔
turtle.penup()
# 画笔退后20px
# turtle.fd(-20)

# 移动到初始位置
turtle.seth(-135)
turtle.goto(-300,-300)

### 绘制外框
# 画笔落下
turtle.pendown()
turtle.seth(0)
turtle.pencolor("black")
turtle.fillcolor("red")
turtle.begin_fill()
turtle.fd(800)
turtle.seth(124)
turtle.goto(300,0)
turtle.seth(56)
turtle.goto(500,300)
turtle.seth(180)
turtle.goto(-300,300)
turtle.seth(270)
turtle.goto(-300,-300)
turtle.end_fill()
# 抬起画笔
turtle.penup()
### 外框绘制结束

### 绘制五角星
turtle.seth(56.35)
# 初始位置
turtle.goto(-78.66,32.48)
turtle.seth(0)
turtle.pencolor("yellow")
turtle.fillcolor("yellow")
turtle.pendown()
turtle.begin_fill()
turtle.fd(60)
turtle.left(72)
turtle.fd(60)
turtle.right(144)
turtle.fd(60)
turtle.left(72)
turtle.fd(60)
turtle.right(144)
turtle.fd(60)
turtle.left(72)
turtle.fd(60)
turtle.right(144)
turtle.fd(60)
turtle.left(72)
turtle.fd(60)
turtle.right(144)
turtle.fd(60)
turtle.left(72)
turtle.fd(60)
turtle.end_fill()
turtle.penup()
### 绘制五角星结束

### 绘制火炬
# 移动到初始位置
turtle.seth(36)
turtle.goto(-55.56,46.28)
turtle.seth(27.71)
turtle.pendown()
# 开始绘制
turtle.goto(-16.35,66.88)
turtle.seth(-135.30)
turtle.circle(21.75,68.37)
print(turtle.pos())
turtle.goto(-21.06,42.89)
turtle.seth(-66.95)
turtle.goto(28.48,-73.52)
turtle.seth(-72.83)
turtle.circle(-5,158.93)
print(turtle.pos())
turtle.goto(-47.95,28.77)
turtle.circle(21.75,68.32)
print(turtle.pos())
turtle.goto(-55.56,46.28)
# 绘制手柄结束
turtle.seth(168.92)
turtle.circle(-30.32,149.11)
turtle.seth(14.08)
turtle.circle(60.64,72.80)
turtle.seth(-73.60)
turtle.circle(-70.52,32.95)
turtle.seth(0.7)
turtle.circle(60.33,69.62)
turtle.seth(-91.39)
turtle.circle(-74.67,49.84)
turtle.seth(-22.67)
turtle.circle(73.4,8.37)
turtle.seth(-155.92)
turtle.circle(-121.92,17.19)
turtle.seth(-163.59)
turtle.circle(21.74,93.71)
turtle.penup()
turtle.goto(0,0)
### 火炬绘制结束

# 程序结束 保持界面不关闭
turtle.done()
