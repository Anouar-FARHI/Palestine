from turtle import *

# Configurer la taille de la fenêtre pour afficher tout le drapeau
setup(width=1000, height=800)

#red triangle
color('red')
begin_fill()
lt(90)
fd(200)
rt(135)
fd(150)
rt(90)
fd(150)
end_fill()

#black triangle
penup()
rt(135)
fd(210)
pendown()
rt(90)
color('black')
begin_fill()
fd(300)
rt(90)
fd(70)
rt(90)
fd(227)
rt(45)
fd(100)
end_fill()

#white triangle
penup()
lt(180)
fd(100)
pendown()
color('white')
lt(45)
fd(227)
rt(90)
fd(70)

#green rectangle
color('green')
begin_fill()
rt(90)
fd(229)
lt(45)
fd(100)
lt(135)
fd(300)
lt(90)
fd(70)
end_fill()


color('red')

write("#Save_Palestine", font=('verdina', 15, 'bold'))

mainloop()
