#-------------------------------------------------------------------------------
# Name:        Modulo 4 - Estadística Descriptiva - MiriadaX.net
#
# Copyright:   (c) David Trillo Montero 2014
#-------------------------------------------------------------------------------

version = "0.3.0 - 20140310"
miVersion = "Regresion Lineal - version " + version
nl =  "\n"

from math import sqrt

class variable():
    def __init__(self, X, name):
        self.name = name
        self.x = X
        self.n = float(len(self.x))
        self.Sx = sum(self.x)
        self.Sxx = sum(map(lambda x: x*x, self.x))
        # Media, Varianza y DesvTipica
        self.avg = self.Sx / self.n
        self.vari = (self.Sxx / self.n) - (self.avg * self.avg)
        self.dt = sqrt(self.vari)

    def __str__(self):
        tmp = self.name + " --> N: %s - Suma: %s - Suma^2: %s" % (self.n, self.Sx, self.Sxx)
        tmp += nl + "      Media: %g - var: %g - dt: %g" % (self.avg, self.vari, self.dt)
        return tmp

class modelolineal():
    """  Linear regression of y = ax + b """
    def __init__(self, X, Y):
        self.vx = variable(X, "x")
        self.vy = variable(Y, "y")

        if self.vx.n != self.vy.n:  raise ValueError, 'unequal length'

        self.n = self.vx.n
        self.Sxy = sum(map(lambda x,y: x*y, self.vx.x, self.vy.x))

        # Covarianza y Correlacion
        self.covxy = (self.Sxy / self.n) - (self.vx.avg * self.vy.avg)
        self.corr = self.covxy / (self.vx.dt * self.vy.dt)

        # resolucion a y b
        det = (self.vx.Sxx * self.n) - self.vx.Sx * self.vx.Sx
        print "det: %s" % (det)
        self.a, self.b = (self.Sxy * self.n - self.vy.Sx * self.vx.Sx)/det, (self.vx.Sxx * self.vy.Sx - self.vx.Sx * self.Sxy)/det

        # Errores y Residuos
        self.avgerror = self.residual = 0.0
        for zx, zy in map(None, X, Y):
            self.avgerror += (zy - self.vy.Sx/self.n)**2
            self.residual += (zy - self.a * zx - self.b)**2
        self.RR = 1 - self.residual/self.avgerror
        ss = self.residual / (self.n-2)
        self.Var_a, self.Var_b = ss * self.n / det, ss * self.vx.Sxx / det


    def resumen(self):
        print str(self.vx) + nl + str(self.vy)
        print "Cov XY: %s" % (self.covxy)
        print "y = %s·x + %s " % (self.a,self.b)
        print "Corr: %s" % (self.corr)
        print "R^2= %g" % self.RR
        print "var_a: %s -  var b: %s" % (self.Var_a, self.Var_b)

    def calcula_y(self, valorx):
        pronos_y = self.vy.avg + ( self.covxy / self.vx.vari ) * (valorx - self.vx.avg)
        print "Para X = %s --- > Y = %s" % (valorx , pronos_y)
    def calcula_x(self, valory):
        pronos_x = self.vx.avg + ( self.covxy / self.vy.vari ) * (valory - self.vy.avg)
        print "Para Y = %s --- > X = %s" % (valory , pronos_x)

    def pronostico(self, valorx):
        """ devuelve y = a·x + b """
        return self.a * valorx + self.b


if __name__ == '__main__':
    x = [0,0,1,5,2,10,1,5,3,1]
    y = [8,10,8,5,6,0,10,2,9,4]
    ml = modelolineal(x,y)
    ml.resumen()
    ml.calcula_y(6)
    ml.calcula_x(7)
