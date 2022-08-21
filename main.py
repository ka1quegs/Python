from random import randint
nome = input("Digite seu apelido: ")
sorteado = randint(0,100)  #Gera um valor aleatorio
print(sorteado)
num_user = 0
chance = 10
while num_user != sorteado:  
    num_user = int(input('Chute um número entre 0 a 100: '))
    if chance != sorteado:
        chance = chance - 1 #Cada vez que o usuario tenta um numero subtrai uma chance
        if (num_user == sorteado):
            print('')
            print("Parabens {}, voce acertou".format(nome))
            break;
        elif (num_user > sorteado):
            print('')
            print("Chutou alto")
            print('Você ainda possui {} chances.'.format(chance))
                
        else:
            print('')
            print("Chutou baixo")
            print('Você ainda possui {} chances.'.format(chance))
        if chance == 0:
            print('')
            print("Voce perdeu suas chances.")
            break;
        
new_tentativa = input("Digite S para receber mais 10 chances: ").upper() #caso o usuario digite /S/ dará mais 10 tentativas 

if new_tentativa == "S": 
    print("Voce ganhou mais 10 chances! Boa sorte")
    chance = 10
    while num_user != sorteado:
        num_user = int(input('Chute um número entre 0 a 100: '))
        if chance != sorteado:
            chance = chance - 1   
            if (num_user == sorteado):
                    print('')
                    print("Parabens {}, voce acertou".format(nome))
                    break;
            elif (num_user > sorteado):
                    print('')
                    print("Chutou alto")
                    print('Você ainda possui {} chances.'.format(chance))
                    
            else:
                    print('')
                    print("Chutou baixo")
                    print('Você ainda possui {} chances.'.format(chance))
            if chance == 0:
                print("Suas chances acabaram")
                print("Fim de jogo.")
                break;