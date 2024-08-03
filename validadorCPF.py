import re
import sys

entrada = input("Digite o seu CPF:")

cpf_enviado = re.sub(
    r'[^0-9]', 
    '',
    entrada
)

entrada_sequencial =  entrada == entrada[0] * len(entrada)

if entrada_sequencial:
    print("dados sequencias não são válidos.")
    sys.exit()
    
#calculo do primeiro digito do CPF
nove_digitos = cpf_enviado[:9]
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
if cpf_enviado == cpf_gerado:
    print(f"O CPF:{cpf_formatado} é válido")
else:
    print("o CPF é inválido")
