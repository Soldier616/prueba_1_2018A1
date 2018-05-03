def creartxt():
    ar1=open("1.txt","w")
    ar1.close()

def grabar1():
    ar1=open("1.txt","a")
    ar1.write("\t**Calculadora de numero binario**\n")
    ar1.write("Diego ")
    ar1.write("Pilamunga\n")

    def calcu():
        def leerdatos():
            bin=open("binario.txt","r")
            linea=bin.readlines()
            lista=linea
            suma = ((2 ** 5) * int(lista[0])) + ((2 ** 4) * int(lista[1])) + ((2 ** 3) * int(lista[2])) + ((2 ** 2) * int(lista[3])) + ( (2 ** 1) * int(lista[4])) + ((2 ** 0) * int(lista[3]))
            ar1.write("\nNumero binario: " + str(lista))
            ar1.write("\nnumero decimal: " + str(suma))
            bin.close()
            print(suma)

        leerdatos()
    calcu()
    ar1.close()
creartxt()
grabar1()


