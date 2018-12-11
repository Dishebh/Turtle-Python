from turtle import *

screen = Screen()
screen.setup(400,400)

screen.bgcolor('#A7E30E')

penup()
goto(0,100)
color('#FA057F')
style=('Arial' ,40, 'bold')
write('HELLO', font=style, align='center')
right(90)
forward(60)
color('#3FE0B0')
write('WORLD',font=style,align='center')
hideturtle()

screen.reset()
screen.bgcolor('#000806')
hideturtle()
goto(0,0)
color('#0EFBCB')
dot(350)

color('#FA057F')
style=('Arial' ,10, 'bold')
write('A TYPICAL', font=style, align='center')
penup()
right(90)
forward(50)
pendown()
color('#EDFB0E')
write('SMARTPHONE HAS VERY LARGE',font=style,align='center')
penup()


forward(50)
pendown()
color('#330405')
write('COMPUTING POWER',font=style,align='center')



