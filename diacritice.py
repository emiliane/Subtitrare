import sys

fisier = sys.argv[1] # "1.srt"

codare1 = "utf-8"
codare2 = "iso-8859-1"

def citesteFisier(fname, codare):
  f = open(fname, "r", encoding=codare)
  return f    

try:
  f = citesteFisier(fisier, codare1)
  s = f.read()
except:
  f = citesteFisier(fisier, codare2)
  s = f.read()

print("Citit fișier subtitrare: " + fisier)

s = s.replace("ã", "ă")
s = s.replace("Ã", "Ă")
s = s.replace("º", "ș")
s = s.replace("ª", "Ș")
s = s.replace("þ", "ț")
s = s.replace("Þ", "Ț")

s = s.replace("\u00e3", "\u0103") #ă
s = s.replace("\u00c3", "\u0102") #Ă
s = s.replace("\u015f", "\u0219") #ș
s = s.replace("\u015e", "\u0218") #Ș
s = s.replace("\u0163", "\u021b") #ț
s = s.replace("\u0162", "\u021a") #Ț

punct = "."
fisier2 = fisier.rsplit(punct, 1)

try:  
  fisierNou = fisier2[0] + "-corectat" + punct + fisier2[1]
except:
  print("Fișier fără extensie")
  fisierNou = fisier2[0] + "-corectat"


f = open(fisierNou, "w")
f.write(s)
f.close()

print("Scris fișier subtitrare corectat: " + fisierNou)
