'''
Modulo 3 Sesion 9 - Rebound
Crear una función que acepte dos parámetros (base y altura) y calcule 
el área de un rectángulo. Validar que ambos sean números positivos.
'''

def area(b,a):
    if(a>0) and (b>0): return(a*b) 
    else: return(0)