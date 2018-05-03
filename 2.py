
def creartxt():
    ar2=open("2.txt","w")
    ar2.close()

def grabar2():
    ar2=open("2.txt","w")
    ar2.write("\tInvertir texto\n")
    def invertir():
        x = "Diego Pilamunga"
        ar2.write("Cadena de texto: "+str(x)+"\n")
        ar2.write("Cadena de texto invertida: ")
        n=(len(x)-1)
        while n!=-1:
            y=str(x[n])
            ar2.write(str(y))
            n=n-1
    invertir()

creartxt()
grabar2()