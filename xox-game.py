from graphics import *
import random
lis = []
win = GraphWin("19290340",300, 350)
win.setBackground("Lightgray")
a = Rectangle(Point(0, 0), Point(100, 100))
al =Text(a.getCenter(), '')
lis.append(al)
a.draw(win)
al.draw(win)
b = Rectangle(Point(100,0), Point(200, 100))
be = Text(b.getCenter(), '')
lis.append(be)
b.draw(win)
be.draw(win)
c = Rectangle(Point(200, 0), Point(300, 100))
ce =Text(c.getCenter(), '')
lis.append(ce)
c.draw(win)
ce.draw(win)
d = Rectangle(Point(0,100), Point(100, 200))
de =Text(d.getCenter(), '')
lis.append(de)
d.draw(win)
de.draw(win)
e = Rectangle(Point(100, 100), Point(200, 200))
el = Text(e.getCenter(), '')
lis.append(el)
e.draw(win)
el.draw(win)
f = Rectangle(Point(200, 100), Point(300, 200))
fe =Text(f.getCenter(), '')
lis.append(fe)
f.draw(win)
fe.draw(win)
g = Rectangle(Point(0,200), Point(100, 300))
ge =Text(g.getCenter(), '')
lis.append(ge)
g.draw(win)
ge.draw(win)
h = Rectangle(Point(100, 200), Point(200, 300))
he =Text(h.getCenter(), '')
lis.append(he)
h.draw(win)
he.draw(win)
j = Rectangle(Point(200, 200), Point(300, 300))
je =Text(j.getCenter(), '')
lis.append(je)
j.draw(win)
je.draw(win)
k = Rectangle(Point(0, 300), Point(300, 350))
ke =Text(k.getCenter(), '')
k.draw(win)
ke.draw(win)
while True:
    try:
        w = win.getMouse()
    except GraphicsError:
        win.close()
        break
    if 0<w.getX()<100 and 0<w.getY()<100:
        if al.getText() == '':
            ke.setText('')
            al.setText("X")
            if al.getText()!='' and be.getText()!='' and ce.getText()!='' and de.getText()!='' and el.getText()!='' and fe.getText()!='' and ge.getText()!='' and he.getText()!='' and je.getText()!='':
                ke.setText("Draw!")
                if al.getText() == de.getText() == ge.getText() or al.getText() == el.getText() == je.getText() or al.getText() == be.getText() == ce.getText():
                    ke.setText(al.getText() + " Wins")
            else:
                if al.getText() == de.getText() == ge.getText() or al.getText() == el.getText() == je.getText() or al.getText() == be.getText() == ce.getText():
                    ke.setText(al.getText() + " Wins")
            if ke.getText()=="Draw!" or ke.getText()=="X Wins" or ke.getText()=="O Wins":
                try:
                    keyString = win.getKey()
                    if keyString == "q":
                        win.close()
                        break
                except:
                    w = win.getMouse()
                    pass
            while True:
                y=random.choice(lis)
                if y==al or y==be or y==ce or y==de or y==el or y==fe or y==ge or y==he or y==je:
                    if y.getText()== '':
                        y.setText("O")
                        if al.getText() != '' and be.getText() != '' and ce.getText() != '' and de.getText() != '' and el.getText() != '' and fe.getText() != '' and ge.getText() != '' and he.getText() != '' and je.getText() != '':
                            ke.setText("Draw!")
                            if al.getText() == de.getText() == ge.getText() or al.getText() == el.getText() == je.getText() or al.getText() == be.getText() == ce.getText():
                                ke.setText(al.getText() + " Wins")
                        else:
                            if al.getText() == de.getText() == ge.getText() or al.getText() == el.getText() == je.getText() or al.getText() == be.getText() == ce.getText():
                                ke.setText(al.getText() + " Wins")
                        if ke.getText() == "Draw!" or ke.getText() == "X Wins" or ke.getText() == "O Wins":
                            try:
                                keyString = win.getKey()
                                if keyString == "q":
                                    win.close()
                                    break
                            except:
                                w = win.getMouse()
                                pass
                        break
                    else:
                        continue
        else:
            ke.setText("You cannot click the filled squares!")
            continue
    if 100< w.getX()<200 and 0<w.getY()<100:
        if be.getText() == '':
            ke.setText('')
            be.setText("X")
            if al.getText()!='' and be.getText()!='' and ce.getText()!='' and de.getText()!='' and el.getText()!='' and fe.getText()!='' and ge.getText()!='' and he.getText()!='' and je.getText()!='':
                ke.setText("Draw!")
                if be.getText() == al.getText() == ce.getText() or be.getText() == el.getText() == he.getText():
                    ke.setText(be.getText() + " Wins")
            else:
                if be.getText() == al.getText() == ce.getText() or be.getText() == el.getText() == he.getText():
                    ke.setText(be.getText() + " Wins")
            if ke.getText()=="Draw!" or ke.getText()=="X Wins" or ke.getText()=="O Wins":
                try:
                    keyString = win.getKey()
                    if keyString == "q":
                        win.close()
                        break
                except :
                    w = win.getMouse()
                    pass
            while True:
                y=random.choice(lis)
                if y==al or y==be or y==ce or y==de or y==fe or y==ge or y==he or y==je or y==el:
                    if y.getText()== '':
                        y.setText("O")
                        if al.getText() != '' and be.getText() != '' and ce.getText() != '' and de.getText() != '' and el.getText() != '' and fe.getText() != '' and ge.getText() != '' and he.getText() != '' and je.getText() != '':
                            ke.setText("Draw!")
                            if be.getText() == al.getText() == ce.getText() or be.getText() == el.getText() == he.getText():
                                ke.setText(be.getText() + " Wins")
                        else:
                            if be.getText() == al.getText() == ce.getText() or be.getText() == el.getText() == he.getText():
                                ke.setText(be.getText() + " Wins")
                        if ke.getText() == "Draw!" or ke.getText() == "X Wins" or ke.getText() == "O Wins":
                            try:
                                keyString = win.getKey()
                                if keyString == "q":
                                    win.close()
                                    break
                            except:
                                w = win.getMouse()
                                pass
                        break
                    else:
                        continue
        else:
            ke.setText("You cannot click the filled squares!")
            continue
    if 200< w.getX()<300 and 0<w.getY()<100:
        if ce.getText() == '':
            ke.setText('')
            ce.setText("X")
            if al.getText()!='' and be.getText()!='' and ce.getText()!='' and de.getText()!='' and el.getText()!='' and fe.getText()!='' and ge.getText()!='' and he.getText()!='' and je.getText()!='':
                ke.setText("Draw!")
                if ce.getText() == fe.getText() == je.getText() or ce.getText() == el.getText() == ge.getText() or ce.getText() == be.getText() == al.getText():
                    ke.setText(ce.getText() + " Wins")
            else:
                if ce.getText() == fe.getText() == je.getText() or ce.getText() == el.getText() == ge.getText() or ce.getText() == be.getText() == al.getText():
                    ke.setText(ce.getText() + " Wins")
            if ke.getText()=="Draw!" or ke.getText()=="X Wins" or ke.getText()=="O Wins":
                try:
                    keyString = win.getKey()
                    if keyString == "q":
                        win.close()
                        break
                except:
                    w = win.getMouse()
                    pass
            while True:
                y=random.choice(lis)
                if y==al or y==be or y==ce or y==de or y==fe or y==ge or y==he or y==je or y==el:
                    if y.getText()== '':
                        y.setText("O")
                        if al.getText() != '' and be.getText() != '' and ce.getText() != '' and de.getText() != '' and el.getText() != '' and fe.getText() != '' and ge.getText() != '' and he.getText() != '' and je.getText() != '':
                            ke.setText("Draw!")
                            if ce.getText() == fe.getText() == je.getText() or ce.getText() == el.getText() == ge.getText() or ce.getText() == be.getText() == al.getText():
                                ke.setText(ce.getText() + " Wins")
                        else:
                            if ce.getText() == fe.getText() == je.getText() or ce.getText() == el.getText() == ge.getText() or ce.getText() == be.getText() == al.getText():
                                ke.setText(ce.getText() + " Wins")
                        if ke.getText() == "Draw!" or ke.getText() == "X Wins" or ke.getText() == "O Wins":
                            try:
                                keyString = win.getKey()
                                if keyString == "q":
                                    win.close()
                                    break
                            except:
                                w = win.getMouse()
                                pass
                        break
                    else:
                        continue
        else:
            ke.setText("You cannot click the filled squares!")
            continue
    if 0< w.getX()<100 and 100<w.getY()<200:
        if de.getText() == '':
            ke.setText('')
            de.setText("X")
            if al.getText()!='' and be.getText()!='' and ce.getText()!='' and de.getText()!='' and el.getText()!='' and fe.getText()!='' and ge.getText()!='' and he.getText()!='' and je.getText()!='':
                ke.setText("Draw!")
                if de.getText() == al.getText() == ge.getText() or de.getText() == el.getText() == fe.getText():
                    ke.setText(de.getText() + " Wins")
            else:
                if de.getText() == al.getText() == ge.getText() or de.getText() == el.getText() == fe.getText():
                    ke.setText(de.getText() + " Wins")
            if ke.getText()=="Draw!" or ke.getText()=="X Wins" or ke.getText()=="O Wins":
                try:
                    keyString = win.getKey()
                    if keyString == "q":
                        win.close()
                        break
                except:
                    w = win.getMouse()
                    pass
            while True:
                y=random.choice(lis)
                if y==al or y==be or y==ce or y==de or y==fe or y==ge or y==he or y==je or y==el:
                    if y.getText()== '':
                        y.setText("O")
                        if al.getText() != '' and be.getText() != '' and ce.getText() != '' and de.getText() != '' and el.getText() != '' and fe.getText() != '' and ge.getText() != '' and he.getText() != '' and je.getText() != '':
                            ke.setText("Draw!")
                            if de.getText() == al.getText() == ge.getText() or de.getText() == el.getText() == fe.getText():
                                ke.setText(de.getText() + " Wins")
                        else:
                            if de.getText() == al.getText() == ge.getText() or de.getText() == el.getText() == fe.getText():
                                ke.setText(de.getText() + " Wins")
                        if ke.getText() == "Draw!" or ke.getText() == "X Wins" or ke.getText() == "O Wins":
                            try:
                                keyString = win.getKey()
                                if keyString == "q":
                                    win.close()
                                    break
                            except:
                                w = win.getMouse()
                                pass
                        break
                    else:
                        continue
        else:
            ke.setText("You cannot click the filled squares!")
            continue
    if 100< w.getX()<200 and 100<w.getY()<200:
        if el.getText() == '':
            ke.setText('')
            el.setText("X")
            if al.getText()!='' and be.getText()!='' and ce.getText()!='' and de.getText()!='' and el.getText()!='' and fe.getText()!='' and ge.getText()!='' and he.getText()!='' and je.getText()!='':
                ke.setText("Draw!")
                if el.getText() == al.getText() == je.getText() or el.getText() == ce.getText() == ge.getText() or el.getText() == be.getText() == he.getText() or el.getText() == de.getText() == fe.getText():
                    ke.setText(el.getText() + " Wins")
            else:
                if el.getText() == al.getText() == je.getText() or el.getText() == ce.getText() == ge.getText() or el.getText() == be.getText() == he.getText() or el.getText() == de.getText() == fe.getText():
                    ke.setText(el.getText() + " Wins")
            if ke.getText()=="Draw!" or ke.getText()=="X Wins" or ke.getText()=="O Wins":
                try:
                    keyString = win.getKey()
                    if keyString == "q":
                        win.close()
                        break
                except:
                    w = win.getMouse()
                    pass
            while True:
                y=random.choice(lis)
                if y==al or y==be or y==ce or y==de or y==fe or y==ge or y==he or y==je or y==el:
                    if y.getText()== '':
                        y.setText("O")
                        if al.getText() != '' and be.getText() != '' and ce.getText() != '' and de.getText() != '' and el.getText() != '' and fe.getText() != '' and ge.getText() != '' and he.getText() != '' and je.getText() != '':
                            ke.setText("Draw!")
                            if el.getText() == al.getText() == je.getText() or el.getText() == ce.getText() == ge.getText() or el.getText() == be.getText() == he.getText() or el.getText() == de.getText() == fe.getText():
                                ke.setText(el.getText() + " Wins")
                        else:
                            if el.getText() == al.getText() == je.getText() or el.getText() == ce.getText() == ge.getText() or el.getText() == be.getText() == he.getText() or el.getText() == de.getText() == fe.getText():
                                ke.setText(el.getText() + " Wins")
                        if ke.getText() == "Draw!" or ke.getText() == "X Wins" or ke.getText() == "O Wins":
                            try:
                                keyString = win.getKey()
                                if keyString == "q":
                                    win.close()
                                    break
                            except:
                                w = win.getMouse()
                                pass
                        break
                    else:
                        continue
        else:
            ke.setText("You cannot click the filled squares!")
            continue
    if 200< w.getX()<300 and 100<w.getY()<200:
        if fe.getText() == '':
            ke.setText('')
            fe.setText("X")
            if al.getText()!='' and be.getText()!='' and ce.getText()!='' and de.getText()!='' and el.getText()!='' and fe.getText()!='' and ge.getText()!='' and he.getText()!='' and je.getText()!='':
                ke.setText("Draw!")
                if fe.getText() == ce.getText() == je.getText() or fe.getText() == el.getText() == de.getText():
                    ke.setText(fe.getText() + " Wins")
            else:
                if fe.getText() == ce.getText() == je.getText() or fe.getText() == el.getText() == de.getText():
                    ke.setText(fe.getText() + " Wins")
            if ke.getText()=="Draw!" or ke.getText()=="X Wins" or ke.getText()=="O Wins":
                try:
                    keyString = win.getKey()
                    if keyString == "q":
                        win.close()
                        break
                except:
                    w = win.getMouse()
                    pass
            while True:
                y=random.choice(lis)
                if y==al or y==be or y==ce or y==de or y==fe or y==ge or y==he or y==je or y==el:
                    if y.getText()== '':
                        y.setText("O")
                        if al.getText() != '' and be.getText() != '' and ce.getText() != '' and de.getText() != '' and el.getText() != '' and fe.getText() != '' and ge.getText() != '' and he.getText() != '' and je.getText() != '':
                            ke.setText("Draw!")
                            if fe.getText() == ce.getText() == je.getText() or fe.getText() == el.getText() == de.getText():
                                ke.setText(fe.getText() + " Wins")
                        else:
                            if fe.getText() == ce.getText() == je.getText() or fe.getText() == el.getText() == de.getText():
                                ke.setText(fe.getText() + " Wins")
                        if ke.getText() == "Draw!" or ke.getText() == "X Wins" or ke.getText() == "O Wins":
                            try:
                                keyString = win.getKey()
                                if keyString == "q":
                                    win.close()
                                    break
                            except:
                                w = win.getMouse()
                                pass
                        break
                    else:
                        continue
        else:
            ke.setText("You cannot click the filled squares!")
            continue
    if 0< w.getX()<100 and 200<w.getY()<300:
        if ge.getText() == '':
            ke.setText('')
            ge.setText("X")
            if al.getText()!='' and be.getText()!='' and ce.getText()!='' and de.getText()!='' and el.getText()!='' and fe.getText()!='' and ge.getText()!='' and he.getText()!='' and je.getText()!='':
                ke.setText("Draw!")
                if ge.getText() == el.getText() == ce.getText() or ge.getText() == de.getText() == al.getText() or ge.getText() == he.getText() == je.getText():
                    ke.setText(ge.getText() + " Wins")
            else:
                if ge.getText() == el.getText() == ce.getText() or ge.getText() == de.getText() == al.getText() or ge.getText() == he.getText() == je.getText():
                    ke.setText(ge.getText() + " Wins")
            if ke.getText()=="Draw!" or ke.getText()=="X Wins" or ke.getText()=="O Wins":
                try:
                    keyString = win.getKey()
                    if keyString == "q":
                        win.close()
                        break
                except:
                    w = win.getMouse()
                    pass
            while True:
                y=random.choice(lis)
                if y==al or y==be or y==ce or y==de or y==fe or y==ge or y==he or y==je or y==el:
                    if y.getText()== '':
                        y.setText("O")
                        if al.getText() != '' and be.getText() != '' and ce.getText() != '' and de.getText() != '' and el.getText() != '' and fe.getText() != '' and ge.getText() != '' and he.getText() != '' and je.getText() != '':
                            ke.setText("Draw!")
                            if ge.getText() == el.getText() == ce.getText() or ge.getText() == de.getText() == al.getText() or ge.getText() == he.getText() == je.getText():
                                ke.setText(ge.getText() + " Wins")
                        else:
                            if ge.getText() == el.getText() == ce.getText() or ge.getText() == de.getText() == al.getText() or ge.getText() == he.getText() == je.getText():
                                ke.setText(ge.getText() + " Wins")
                        if ke.getText() == "Draw!" or ke.getText() == "X Wins" or ke.getText() == "O Wins":
                            try:
                                keyString = win.getKey()
                                if keyString == "q":
                                    win.close()
                                    break
                            except:
                                w = win.getMouse()
                                pass
                        break
                    else:
                        continue
        else:
            ke.setText("You cannot click the filled squares!")
            continue
    if 100< w.getX()<200 and 200<w.getY()<300:
        if he.getText() == '':
            ke.setText('')
            he.setText("X")
            if al.getText()!='' and be.getText()!='' and ce.getText()!='' and de.getText()!='' and el.getText()!='' and fe.getText()!='' and ge.getText()!='' and he.getText()!='' and je.getText()!='':
                ke.setText("Draw!")
                if he.getText() == ge.getText() == je.getText() or he.getText() == el.getText() == be.getText():
                    ke.setText(he.getText() + " Wins")
            else:
                if he.getText() == ge.getText() == je.getText() or he.getText() == el.getText() == be.getText():
                    ke.setText(he.getText() + " Wins")
            if ke.getText()=="Draw!" or ke.getText()=="X Wins" or ke.getText()=="O Wins":
                try:
                    keyString = win.getKey()
                    if keyString == "q":
                        win.close()
                        break
                except:
                    w = win.getMouse()
                    pass
            while True:
                y=random.choice(lis)
                if y==al or y==be or y==ce or y==de or y==fe or y==ge or y==he or y==je or y==el:
                    if y.getText()== '':
                        y.setText("O")
                        if al.getText() != '' and be.getText() != '' and ce.getText() != '' and de.getText() != '' and el.getText() != '' and fe.getText() != '' and ge.getText() != '' and he.getText() != '' and je.getText() != '':
                            ke.setText("Draw!")
                            if he.getText() == ge.getText() == je.getText() or he.getText() == el.getText() == be.getText():
                                ke.setText(he.getText() + " Wins")
                        else:
                            if he.getText() == ge.getText() == je.getText() or he.getText() == el.getText() == be.getText():
                                ke.setText(he.getText() + " Wins")
                        if ke.getText() == "Draw!" or ke.getText() == "X Wins" or ke.getText() == "O Wins":
                            try:
                                keyString = win.getKey()
                                if keyString == "q":
                                    win.close()
                                    break
                            except:
                                w = win.getMouse()
                                pass
                        break
                    else:
                        continue
        else:
            ke.setText("You cannot click the filled squares!")
            continue
    if 200< w.getX()<300 and 200<w.getY()<300:
        if je.getText() == '':
            ke.setText('')
            je.setText("X")
            if al.getText()!='' and be.getText()!='' and ce.getText()!='' and de.getText()!='' and el.getText()!='' and fe.getText()!='' and ge.getText()!='' and he.getText()!='' and je.getText()!='':
                ke.setText("Draw!")
                if je.getText() == fe.getText() == ce.getText() or je.getText() == el.getText() == al.getText() or je.getText() == he.getText() == ge.getText():
                    ke.setText(je.getText() + " Wins")
            else:
                if je.getText() == fe.getText() == ce.getText() or je.getText() == el.getText() == al.getText() or je.getText() == he.getText() == ge.getText():
                    ke.setText(je.getText() + " Wins")
            if ke.getText()=="Draw!" or ke.getText()=="X Wins" or ke.getText()=="O Wins":
                try:
                    keyString = win.getKey()
                    if keyString == "q":
                        win.close()
                        break
                except:
                    w = win.getMouse()
                    pass
            while True:
                y=random.choice(lis)
                if y==al or y==be or y==ce or y==de or y==fe or y==ge or y==he or y==je or y ==el:
                    if y.getText()== '':
                        y.setText("O")
                        if al.getText() != '' and be.getText() != '' and ce.getText() != '' and de.getText() != '' and el.getText() != '' and fe.getText() != '' and ge.getText() != '' and he.getText() != '' and je.getText() != '':
                            ke.setText("Draw!")
                            if je.getText() == fe.getText() == ce.getText() or je.getText() == el.getText() == al.getText() or je.getText() == he.getText() == ge.getText():
                                ke.setText(je.getText() + " Wins")
                        else:
                            if je.getText() == fe.getText() == ce.getText() or je.getText() == el.getText() == al.getText() or je.getText() == he.getText() == ge.getText():
                                ke.setText(je.getText() + " Wins")
                        if ke.getText() == "Draw!" or ke.getText() == "X Wins" or ke.getText() == "O Wins":
                            try:
                                keyString = win.getKey()
                                if keyString == "q":
                                    win.close()
                                    break
                            except:
                                w = win.getMouse()
                                pass
                        break
                    else:
                        continue
        else:
            ke.setText("You cannot click the filled squares!")
            continue
            







