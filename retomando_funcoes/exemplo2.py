def main(): #   Função principal do programador
    resp = 1
    lista =[]
    while resp != 0:
        print("1-leitura da lista")
        print("2-calcular a soma dos divisiveis por 3")
        print("3-calcular a lista dos quadrados")
        print("4-exibir a lista")
        opc = int(input("Digite a opção desejada 1 até 4: "))
        match opc:
            case 1: 
                tam = int(input("Dihite o tamanho da lista: "))
                ler_lista(lista, tam )
            case 2:
                if (len(lista) > 0): 
                    print(f"A soma dos divisiveis por 3 da lista é {somar_divisivel3(lista)}")
                else: 
                    print("A lista está vazia")
            case 3:
                if (len(lista) > 0): 
                    exibir_lista(retornar_lista(lista))
                else: 
                    print("A lista está vazia")
            case 4:
                if (len(lista) > 0): 
                    exibir_lista(lista)
                else: 
                    print("A lista está vazia")
            case _: 
                print("Opção inválida")
        resp = int(input("Deseja continnuar? 1-SIM 0- NÃO"))



# Função que vai receber uma lista e um tamanho. Objetivo: Pedir para o usuário para preencher a lista
def ler_lista(lista, tam):
    for i in range(tam):
        lista.append(int(input("Digite um elemento da lista: ")))

# Função que recebe uma lista e retorna  a soma dos números divisíveis por 3
def somar_divisivel3(lista):
    soma = 0
    for i in range (len(lista)):
        if (lista[i] % 3 == 0):
            soma += lista[i]
    return(soma)

# Função que recebe uma lista e retornar outra lista com elementos da lista original ()
def retornar_lista(lista):
    lista_quadrado = []
    for i in range(len(lista)):
        lista_quadrado.append(lista[i]**2)
    return lista_quadrado

# Função para exibir elementos da minha lista
def exibir_lista(lista):
    for i in range(len(lista)):
        print(lista[i])

if (__name__ == '__main__'):
    main()