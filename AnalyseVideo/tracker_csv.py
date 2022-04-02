import sys

f = open(sys.argv[1], "r")
out = open(sys.argv[2], "w")

linenumber = 0

for line in f:
  if(linenumber != 0):
    out.write(line.replace(",",".").replace(";",",").replace("{","").replace("}",""))
  linenumber += 1

out.close()
f.close()
