inp = open(input(),"r").read().split("\n")[2:]
district = 2
print("""The Hunger Games
https://brantsteele.com/extras/hungergames/01/logo.png
""")
for line in inp:
    line = line.split(",")
    if district % 2 == 0:
        print("""\nDistrict %s
#FFFFFF 0 0\n""" % (district//2))
    district += 1
    print(line[2] + "\n" + line[2])
    match line[3]:
        case "he/him":
            print("0")
        case "she/her":
            print("1")
        case "they/them":
            print("4")
    print("T\nT\n")
