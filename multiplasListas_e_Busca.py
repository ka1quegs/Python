#Listas multiplas: inserção e busca
equipamentos = []
valores = []
serial = []
departamentos = []
resposta= "S" 
while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    serial.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento:" ))
    resposta=input("Digite \"s\" para continuar: ").upper()
busca= input("\nDigite o nome do equipamento que deseja buscar: ")
for indice in range (0,len(equipamentos)):
    if busca == equipamentos[indice]:
        print("Valor..: ", valores[indice])
        print("Serial.:", serial[indice])