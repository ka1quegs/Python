nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
diabetico=input("O paciente é diabético? ").upper()
if idade>=65:
    print("O paciente  " + nome + " possui acesso prioritário!")
elif diabetico =="SIM" or "s".upper:
    print("O paciente " + nome + " deve ser direcionado a fila prioritária!!")
else:
    print("O paciente " + nome + " nao possui acesso prioritário!")
print("fim")