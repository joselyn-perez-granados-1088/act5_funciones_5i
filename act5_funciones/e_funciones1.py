print("manejo de funciones v1")
def hola_mundo():
    print("hola soy josytodia, dentro de la funcion")
def mensaje(msg):
    print(msg)
def escribirnc(nombre,apellido):
    print(nombre,apellido)
    print(f"mi nombre compelto es{nombre} {apellido}")
def sumadosnumeroos(n1,n2):
        s=n1+n2
        return f"la suma de {n1} y de {n2} es de:",s 
        print(f"la suma de m1+n2 es {s} ")
    #LLAMANDO A LAS FUNCIONES ♥
hola_mundo()
mensaje("ayo wasap") # llama a mensaje con 1 parametro
mensaje("el profe me sorprendio mandando mensas") # llama a mensaje con un parametro
escribirnc("josy","teodia")
print (sumadosnumeroos(7,3))
print (sumadosnumeroos(15,45))