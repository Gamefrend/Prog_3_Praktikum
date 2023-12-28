def h(a,b,c=1000,*d,**e):
    print(a,b,c,d,e)

tup = ("ene","mene","mu")
kw = { "x":"iks", "b":"beh", "lst":[17,17,17] }
h(17,21)
h(10,20,30)
h(1,2,3,4,5,6,x=7, y=22)
#h(1,2,3,4,5,6,c=7)
h(*tup), h(1,2,*tup,3)
h(10, **kw)
h(10,20,*tup, **kw)