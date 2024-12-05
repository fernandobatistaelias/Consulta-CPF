# Consulta-CPF
'''Consulta_CPF_Válidos'''
while True:
    try:
        cpf = input('Digite um CPF:\n')
        if not cpf.isdigit() or  len(cpf)!= 11: # Verifica se o CPF contém apenas números e tem 11 dígitos
           print("CPF inválido. Certifique-se de digitar 11 números.")   
        elif cpf == cpf[0] * 11:  # Verifica se todos os dígitos são iguais
            print("CPF inválido. Não pode ter todos os dígitos iguais.")     
        soma1 = 0
        contador_reverso1 = 10
        for i in range(9):
            soma1 += int(cpf[i]) * contador_reverso1
            contador_reverso1-=1
        resto1 = soma1%11
        digito1 = 0 if resto1 < 2 else 11 - resto1 # Calcula o primeiro dígito verificador
        soma2 = 0
        contador_reverso2 = 11
        for i in range(10):
            soma2 +=int(cpf[i]) * contador_reverso2
            contador_reverso2-=1
        resto2 = soma2%11
        digito2 = 0 if resto2 < 2 else 11 - resto2 # Calcula o segundo dígito verificador
        if digito1 == int(cpf[9]) and digito2 == int(cpf[10]): # Verifica os dígitos calculados com os fornecidos
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
