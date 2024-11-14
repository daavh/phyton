  # aqui o sistema pede o nome do usario
nome = input("Digite seu nome:")
# aqui o sistema pede a idade do usario
idade = int(input("Qual a sua idade?"))
# aqui mostra o nome e a idade que o usario informou
print(f"Bem vindo {nome}, voce tem {idade} anos.")

print("Como posso te ajudar hoje?")
# aqui e uma função que serve como menu
def menu():
    print("1 - Bebidas")
    print("2 - Salgados")
    print("3 - Doces")
#aqui grava a opção que o usari digitou
    opc = int(input("Digite o número da opção desejada:"))
# aqui começa a lógica do SE
    if opc == 1:
        print("Temos coca, fanta e juninho")

    elif opc == 2:
        print("Temos dog, quibe e coxinha")

    elif opc == 3:
        print("Temos brigadeiro, beijinho e bomba de doce de leite")

    else:
        print("Opção incorreta, escolha um número de 1 a 3")
menu()