#Função sem retorno de valor 

def exibir_status_aluno(n1, n2, n3): #n1 n2 e n3 são parametros para função
    media = (n1 + n2 + n3) / 3
    if media >= 7.0: 
        print(f"Aluno aprovado com média {media: .2f}")
    else: 
        print(f"Aluno reprovado com média {media: .2f}")

#chamada da função 
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundovalor: "))
n3 = float(input("Digite o terceiro valor: "))
exibir_status_aluno(n1, n2, n3)



def calcular_acrecimo(valor, perc):
    valor_com_acrecimo = valor + (valor * perc / 100)
    return(valor_com_acrecimo)

#chamada da função 
valor = float(input("Digite um valor: "))
perc = float(input("Digite o acrécimo a ser aplicado: "))
print(f"O valor com acrécimo é {calcular_acrecimo(valor, perc):.2f}")
