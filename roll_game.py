import random
print('<<<<< GAME START! >>>>>')
choice=input('Big or Small:')
point1=random.randrange(1,7)
point2=random.randrange(1,7)
point3=random.randrange(1,7)
x=point1+point2+point3
print('<<<<< ROLE THE DICE!>>>>>')
y=None
if (x>=11 and x<=18) :
	y='Big'
else:
	y='Small'
if choice==y:
	print('The points are [{},{},{}] You Win!'.format(point1,point2,point3))
else:
	print('The points are [{},{},{}] You Lose!'.format(point1,point2,point3))