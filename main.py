#A DIFERENCIA DE JAVA, EN PYTHON NO HAY UN MÉTODO PARA HACER UNA RAÍZ CUADRADA,
#HAREMOS UNO NOSOTROS MISMOS.

def sqrt (n):       #CREA MÉTODO RAÍZ CUADRADA
    return n**(1/2)     #RAÍZ DE N = N ELEVADO A 1/2

print ("La ecuación es del tipo: ax^2 + bx + c = 0")        #GUÍA PARA USUARIO
a = float (input ("Introduzca el valor de a: "))        #SOLICITA VALOR A
b = float (input ("Introduzca el valor de b: "))        #SOLICITA VALOR B
c = float (input ("Introduzca el valor de c: "))        #SOLICITA VALOR C

#EN LAS SIGUIENTES OPERACIONES APLICAREMOS EL MÉTODO SQRT(N) PARA HALLAR RAÍCES CUADRADAS
x1 = (-b+sqrt(b**2-4*a*c)/2*a)      #CALCULA RESULTADO SUMANDO RAÍZ
x2 = (-b-sqrt(b**2-4*a*c)/2*a)      #CALCULA RESULTADO RESTANDO RAÍZ

print ("Las soluciones del polinomio son:",x1,x2)       #OUTPUT