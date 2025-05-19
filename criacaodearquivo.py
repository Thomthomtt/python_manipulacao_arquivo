def escreverArquivo(frase):
    with open("Lista.txt", "a") as arquivo:
        arquivo.write(frase)

smptrue=True
while smptrue==True:
    resp=int(input("1. Escrever nome no arquivo \n"
          "2. Sair"))
    if resp==1:
        escreverArquivo("Patricio")
    if resp==2:
        print("Você saiu do menu")
        smptrue=False


