div4 = []
div6 = []
div9 = []
div46 = []
div49 = []
div69 = []
div469 = []

for i in range(1,1000001):
    if i%4 == 0:
        div4.append(i)
        if i%6 == 0:
            div46.append(i)
            if i%9 == 0:
                div469.append(i)
        if i%9 == 0:
            div49.append(i)
    if i%6 == 0:
        div6.append(i)
        if i%9 == 0:
            div69.append(i)
    if i%9 == 0:
        div9.append(i)

print "div4:", len(div4)
print "div6:", len(div6)
print "div9:", len(div9)
print "div46:", len(div46)
print "div49:", len(div49)
print "div69:", len(div69)
print "div469:", len(div469)
