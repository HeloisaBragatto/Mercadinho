print("Mercadinho do python!")

while True:
    print("Escolha a opção para ir para o setor do mercado desejado.")
    print("1-Hortifruti")
    print("2-Açougue")
    print("3-Padaria")
    print("4-Mercearia")
    print("0-Sair do programa.")
    print("_________")

    opcaoPrincipal = int(input("Digite a opção: "))

    if opcaoPrincipal == 0:
        print("Saindo do programa...")
        break

    sair = False

    match opcaoPrincipal:
        case 1:
            opcao = -1
            morango, maca, banana, laranja = [0,0,0,0]

            while opcao != 0 :
                print("Você escolheu a opção 'Hortifruti'")
                print("_________")
                print("Frutas do Hortifruti")
                print("1-Morango")
                print("2-Maça")
                print("3-Banana")
                print("4-Laranja")
                print("0-Para sair desse setor.")
                print("_________")

                if opcao == 1 :
                    morango+=1
                elif opcao == 2:
                    maca+=1
                elif opcao == 3:
                    banana+=1
                elif opcao == 4:
                    laranja+=1
                elif opcao == 0:
                    sair = True
                else:
                    print("Número inválido")

                opcao = int(input("Digite a opção: "))  
            
                print("_________")
                print(f"Nesse setor você selecionou:\n {morango}-Morango(s)\n {maca}-Maça(S)\n {banana}-Banana(s)\n {laranja}-Laranja(s)")
                print("_________")

                hortifruti = {
                "morango": {"nome": "Morango", "quantidade": morango},
                "maca": {"nome": "Maçã", "quantidade": maca},
                "banana": {"nome": "Banana", "quantidade": banana},
                "laranja": {"nome": "Laranja", "quantidade": laranja}
                }
            
        case 2:
            opcao = -1
            picanha, frango, linguica, carne = [0,0,0,0]

            while opcao != 0 :
                print("Você escolheu a opção 'Açougue'")
                print("_________")
                print("Carnes do Açougue")
                print("1-Picanha;")
                print("2-Peito de frango")
                print("3-Linguiça")
                print("4-Carne moída")
                print("0-Para sair desse setor.")
                print("_________")
                
                if opcao == 1 :
                    picanha+=1
                elif opcao == 2:
                    frango+=1
                elif opcao == 3:
                    linguica+=1
                elif opcao == 4:
                    carne+=1
                elif opcao == 0:
                    sair = True
                else:
                    print("Número inválido")

                opcao = int(input("Digite a opção: "))   

                print("_________")
                print(f"Nesse setor você selecionou:\n {picanha}-Picanha\n {frango}-Peito de Frango\n {linguica}-Linguiça\n {carne}-Carne Moída")
                print("_________")

                acougue = {
                "picanha": {"nome": "Picanha", "quantidade": picanha},
                "frango": {"nome": "Peito de frango", "quantidade": frango},
                "linguica": {"nome": "Linguiça", "quantidade": linguica},
                "carne": {"nome": "Carne moída", "quantidade": carne}
                }


        case 3:
            opcao = -1
            frances, doce, caseiro, croissant = [0,0,0,0]

            while opcao != 0 :
                print("Você escolheu a opção 'Padaria'")
                print("_________")
                print("Pães da Padaria")
                print("1-Francês")
                print("2-Doce")
                print("3-Caseiro")
                print("4-Croissant")
                print("0-Para sair desse setor.")
                print("_________")

                if opcao == 1 :
                    frances+=1
                elif opcao == 2:
                    doce+=1
                elif opcao == 3:
                    caseiro+=1
                elif opcao == 4:
                    croissant+=1
                elif opcao == 0:
                    sair = True
                else:
                    print("Número inválido")
                
                opcao = int(input("Digite a opção: "))   

                print("_________")
                print(f"Nesse setor você selecionou:\n {frances}-Francês\n {doce}-Doce\n {caseiro}-Caseiro\n {croissant}-Croissant")
                print("_________")

                padaria = {
                "frances": {"nome": "Francês", "quantidade": frances},
                "doce": {"nome": "Doce", "quantidade": doce},
                "caseiro": {"nome": "Caseiro", "quantidade": caseiro},
                "croissant": {"nome": "Croissant", "quantidade": croissant}
                }

        case 4:
            opcao = -1
            arroz, feijao, macarrao, cafe = [0,0,0,0]

            while opcao != 0 :
                print("Você escolheu a opção 'Mercearia'")
                print("_________")
                print("Itens da Mercearia")
                print("1-Arroz")
                print("2-Feijão")
                print("3-Macarrão")
                print("4-Café")
                print("0-Para sair desse setor.")
                print("_________")

                if opcao == 1 :
                    arroz+=1
                elif opcao == 2:
                    feijao+=1
                elif opcao == 3:
                    macarrao+=1
                elif opcao == 4:
                    cafe+=1
                elif opcao == 0:
                    sair = True
                else:
                    print("Número inválido")

                opcao = int(input("Digite a opção: "))   

                print("_________")
                print(f"Nesse setor você selecionou:\n {arroz}-Arroz\n {feijao}-Feijão\n {macarrao}-Macarrão\n {cafe}-Café")
                print("_________")

                mercearia = {
                "arroz": {"nome": "Arroz", "quantidade": arroz},
                "feijao": {"nome": "Feijão", "quantidade": feijao},
                "macarrao": {"nome": "Macarrão", "quantidade": macarrao},
                "cafe": {"nome": "Café", "quantidade": cafe}
                }

        case _:
            print("Escolha uma opção válida.")

print("______________")
print("Compras: ")
print("______________")

if hortifruti :
    for chave, produto in hortifruti.items():
        nome = produto["nome"]
        quantidade = produto["quantidade"]
        print(f"{nome}: {quantidade} unidade(s)")
        print("______________")

if acougue:
    for chave, produto in acougue.items():
        nome = produto["nome"]
        quantidade = produto["quantidade"]
        print(f"{nome}: {quantidade} unidade(s)")
        print("______________")

if padaria:
    for chave, produto in padaria.items():
        nome = produto["nome"]
        quantidade = produto["quantidade"]
        print(f"{nome}: {quantidade} unidade(s)")
        print("______________")

if mercearia:
    for chave, produto in mercearia.items():
        nome = produto["nome"]
        quantidade = produto["quantidade"]
        print(f"{nome}: {quantidade} unidade(s)")
        print("______________")