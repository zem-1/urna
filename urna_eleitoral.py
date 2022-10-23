import os
candidatos = {}
v = {}   
v_b = 0   
v_n = 0   
while True:
    print('1 - Cadastrar candidato')
    print('2 - Votar')
    print('3 - Resultado')
    print('4 - Sair')
    funcao = int(input('Operação: '))
    if funcao > 4 or funcao < 1:
        os.system ('cls')
        print('Operação inválido')
    elif funcao == 1:
        os.system ('cls')
        nome = input('Nome do candidato: ')
        n_c = int(input('Codigo do candidato: '))
        if n_c in candidatos:
            print('Codigo já cadastrado já cadastrado')
        else:
            candidatos[n_c] = nome
            v[n_c] = 0
        os.system ('cls')    
    elif funcao == 2:
        print('Caso queira anular o voto Digite: Anular ')
        print('Caso queira votar em Branco digite: Branco ')
        n = input('Digite o codigo do candidato:') 
        if n.isnumeric():
            n = int(n)
            print('Voto registrado com sucesso')
        elif n == 'Branco':
            v_b += 1
            print('Voto registrado com sucesso')
        elif n == 'Anular':
            v_n += 1
            print('Voto registrado com sucesso')
        if n not in candidatos:
            v_n += 1
            print('Voto registrado com sucesso')
        if n in v:
            v[n] += 1
            print('Voto registrado com sucesso')
        os.system ('cls')
    elif funcao == 3:
        print(f'V anulados: {v_n}')
        atual = 0
        maior = 0
        i_maior = 0
        for i in sorted(v):
            atual = v[i]
            if atual > maior:
                maior = atual
                i_maior = i
        maior += v_b
        v[i_maior] = maior
        for i in sorted(v, key = v.get, reverse=True):
            print(f'Candidato:{candidatos[i]}| Número:{i}| V:{v[i]}')
        os.system ('cls')        
    else:
        os.system ('cls')
        print ('Operação encerrada.')
        break