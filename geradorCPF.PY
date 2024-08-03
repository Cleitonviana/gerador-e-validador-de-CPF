import random
import os

quantidade_cpf = input("Digite quantos CPF deseja gerar: ")
for _ in range(int(quantidade_cpf)):
    nove_digitos =''
    for i in range(9):
        nove_digitos += str(random.randint(0,9))
        
    contador_regressivo_1 = 10
    resultado_digito_1 = 0

    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -=1
        
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <=9 else 0
    #calculo do segundo digito do CPF
    dez_digitos = nove_digitos + str(digito_1)
    contandor_regressivo_2 = 11
    resultado_digito_2 = 0

    for digito2 in dez_digitos:
        resultado_digito_2 += int(digito2) * contandor_regressivo_2
        contandor_regressivo_2 -=1
        
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado = f"{nove_digitos}{digito_1}{digito_2}"
    cpf_formatado = f"{cpf_gerado[:3]}.{cpf_gerado[3:6]}.{cpf_gerado[6:9]}-{cpf_gerado[9:]}"
    print(cpf_formatado)
  