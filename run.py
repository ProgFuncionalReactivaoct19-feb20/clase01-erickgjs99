"""
	autor: @erickgjs99
	file:  run.py
"""
def metodoUno(n):
	return n**2

def metodoDos(m):
	return m + 1 

def metodoTres(x):
	return x + 100

def metodoCuatro(y):
	return y * 3


print(metodoUno(3))

print(metodoDos(metodoUno(4)))

print(metodoTres(metodoDos(metodoTres(5))))

print(metodoCuatro(metodoTres(metodoDos(metodoUno(2)))))