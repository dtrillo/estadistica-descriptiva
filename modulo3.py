#-------------------------------------------------------------------------------
# Name:        Modulo 4 - Estadística Descriptiva - MiriadaX.net
#
# Copyright:   (c) David Trillo Montero 2014
#-------------------------------------------------------------------------------

version = "0.1.0"
miVersion = "Estadistica Descriptiva - version", version
nl =  "\n"


x = [25, 75, 125, 175, 225, 275]
f = [2 , 10 , 20 , 10 , 5 , 3]
x = [24, 36, 48, 60]
f = [10, 12, 8, 6]
xf = map(lambda x,y: x*y, x,f) # x*f
casos = sum(f)
xmedia = sum(xf) / casos
print("Media: " + str(xmedia))
xx = [ abs(i - xmedia) for i in x]  # Xi - Xmedia
xxf = map(lambda x,y: x*y, xx,f)    # (Xi - Xmedia) * f

dm = sum(xxf) / casos
print "DM: ", dm

x2f = map(lambda x,y: x*x*y, x,f) # x2*f
vari = (sum(x2f) / casos) - (xmedia * xmedia)
print "Varianza: " + str(vari)
