#comillas simples 
cads = 'texto en comillas simples'
cadd = "texto en comillas dobles"
#respeta los saltos de linea
cadc = """texto 
linea 2
linea 3
linea 4
       """

#repeticion y concatenacion
cad = "Cadena " * 3

ca1 = "cadena 1 " 
ca2 = "cadena 2"

#operadores logicos y bool
bT = True
bF = False

bAnd = True and False
bOr  = True or  False
bNot = not False

print bAnd,bOr,bNot


print "comillas triples\n",cadc
print "\n"
print cads,type(cads)
print cadd,type(cadd)
print "\n\n"
print cad
print "\n"
print ca1+ca2
