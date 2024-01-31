import re
import socket

with open(r"C:\Users\eniav\Desktop\Uni Aufgaben\Prog 3\access.log") as file:
    inhalt = file.read()

temp = "00"
getBilder = re.compile(r"GET.*\.(png|jpg|gif)")
alleEintraege = re.compile(r"\n")
print(len(getBilder.findall(inhalt)))
anzahlEintraege = len(alleEintraege.findall(inhalt))
currentRe = re.compile(r".{18}\[\d{2}/\w{3}/\d{4}:00:\d{2}:\d{2}")
counter = 0
for i in range(0, 24):
    if i < 10:
        currentRe = re.compile(r"[^\[]*\[\d{2}/\w{3}/\d{4}:0" + re.escape(str(i)) + r":\d{2}:\d{2}")
    else:
        currentRe = re.compile(r"[^\[]*\[\d{2}/\w{3}/\d{4}:" + re.escape(str(i)) + r":\d{2}:\d{2}")

findIP = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
middleAndTopLvl = {}
ipCach = {}
print(socket.gethostbyaddr("195.72.105.32"))
for ip in findIP.findall(inhalt):
    if ip not in ipCach:
        ipCach.update({ip: 1})
    else:
        ipCach[ip] = ipCach[ip]+1

counter = 0

for ip in ipCach:
    counter = counter + 1
    print(str(round(((counter/len(ipCach)) * 100),2)) + "%")
    try:
        tempDomain = socket.gethostbyaddr(ip)[0].split(".")[-2:]
        tempDomain = tempDomain[0] +"."+ tempDomain[1]
    except:
        pass
    if tempDomain not in middleAndTopLvl:
        middleAndTopLvl.update({tempDomain : ipCach[ip]})
    else:
        middleAndTopLvl.update({tempDomain : middleAndTopLvl[tempDomain]+ipCach[ip]})

print(middleAndTopLvl)
