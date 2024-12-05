''' Desenvolva um cpf'''
"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
while True:
    try:
        cpf = input('Digite um CPF:\n')
        if not cpf.isdigit() or  len(cpf)!= 11:
           print("CPF inválido. Certifique-se de digitar 11 números.")   
        elif cpf == cpf[0] * 11:
            print("CPF inválido. Não pode ter todos os dígitos iguais.")    
        soma1 = 0
        contador_reverso1 = 10
        for i in range(9):
            soma1 += int(cpf[i]) * contador_reverso1
            contador_reverso1-=1
        resto1 = soma1%11
        digito1 = 0 if resto1 < 2 else 11 - resto1
        soma2 = 0
        contador_reverso2 = 11
        for i in range(10):
            soma2 +=int(cpf[i]) * contador_reverso2
            contador_reverso2-=1
        resto2 = soma2%11
        digito2 = 0 if resto2 < 2 else 11 - resto2
        if digito1 == int(cpf[9]) and digito2 == int(cpf[10]):
            print(f'O CPF {cpf}, é válido')
        else:
            print(f'O CPF {cpf}, é inválido')
        continuar = input('Deseja fazer uma nova consulta?\n')
        if continuar:
            if continuar == 'sim':
                continue
            if continuar =='nao':
               print('Até mais!!!')
               break    
    except ValueError:
        print('Digite apenas números, letras e caracteres não são aceitos')
            