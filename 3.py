
def creartxt():
    ar3=open("3.txt","w")
    ar3.close()

def grabar3():
    ar3=open("3.txt","a")

    def codificador():
        numero=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
        letra=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
        codigo=[numero,letra]
        mensaje="ANTES"  #codigo=3 12 0 22 15
        ar3.write("\n"+str(codigo))
        ar3.write("\nMensaje: "+str(mensaje))
        ar3.write("\nCodigo: ")
        for l in mensaje:
            ar3.write("\n" +str(l))

    codificador()

    ar3.close()

creartxt()
grabar3()



