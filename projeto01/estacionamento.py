op = 0
acce = 0 
accs = 0 
hma = 0 
mma = 0 
hme = 0 
mme = 0 
din = 0

while op != 6:

    print('1. Cadastrar Tarifas')
    print('2. Registrar Entrada de Veículo')
    print('3. Registrar Saída de Veículo')
    print('4. Gerar Relatório diário')
    print('5. Gerar Relatório por tipo de veículo')
    print('6. Sair')

    op = int(input('Digite a opção:'))

    if op == 1:
        
        valor3h = int(input('Permanência por 3hrs:'))
        valorad = int(input('Adicional por hora:'))
        valorcg = int(input('Tarifa carro grande:'))
        valorcp = int(input('Tarifa carro pequeno:'))
        valorm = int(input('Tarifa moto:'))
        
    elif op == 2: 
        placa = input('Placa do carro:')
        port_carro = input('Tipo de veículo [Carro grande; Carro pequeno; Moto]:')
        entra = input('Horário de entrada do veículo [H:M]:')
        data = input("Data [DD/MM/AAAA]:")

        print('----RECIBO----')
        print('Placa:',placa)
        print('Tipo:',port_carro)
        print('Entrada:',entra)
        print('Data:',data)
        acce += 1

    elif op == 3:

        saida = input('Horário de saída do veículo [H:M]:')
        pag = (input('Forma de pagamento:'))

        len(entra.split(':'))
        len(saida.split(':'))
        he,me = entra.split(':')
        hs,ms = saida.split(':')

        hp = int(hs) - int(he) 
        mp = abs(int(ms) - int(me))

        val_m = mp*valor3h/180

        print('----RECIBO----')        
        print(f'Permanencia:{hp}:{mp}')

        if hp >= 4:
            h_ad = hp - 3 
            val_h = valor3h + (h_ad*valorad)   
            val_t = val_h + val_m
            print(f'Valor adcional por Hora:{h_ad*valorad}')
        else:
            val_h = valor3h
            val_t = val_h + val_m

        if port_carro.lower() == 'carro grande':
            val_tarifa = val_t + valorcg
            print('Taxa carro grande:',valorcg)
            
        elif port_carro.lower() == 'carro pequeno':
            val_tarifa = val_t + valorcp
            print('Taxa carro grande:',valorcp)

        elif port_carro.lower() == 'moto':
            val_tarifa = val_t + valorm
            print('Taxa carro grande:',valorm )

        if pag.lower() == 'pix':
            val_tarifa = val_tarifa - (val_tarifa*0.05)
            print('!!!Você recebeu um desconto de 5%!!!')

        print(f'Valor a ser pago:{val_tarifa:.2f}')

        accs += 1        

        hma == hp and hme == hp
        mma == mp and mme == mp

        if hp > hma:
            hma = hp
        if hp <= hme:
            hme = hp

        if mp > mma:
            mma = mp
        if mp <= mme:
            mme = mp

    elif op == 4:

        temp_mh = (hma - hme)/accs
        temp_mm = (mma - mme)/accs

        if round(temp_mm) > 60:
            x = temp_mm // 60 
            temp_mh = temp_mh + x

        din = din + val_tarifa

        print('----RELATÓRIO----')
        print(f'Veículos que deram entrada:{acce}')
        print(f'Veículos que deram saída:{accs}')
        print(f'Tempo médio se permanência:{round(temp_mh)}:{round(temp_mm)}')
        print(f'Valor arrecadado no dia:{din:.2f}')


    elif op == 5:

        port_carro += port_carro + ',' 

        len(port_carro.split(','))

        if 'carro grande'> 'moto' and 'carro grande'>'carro pequeno':
            ve_comu = 'carro grande'

        if 'carro pequeno'> 'moto' and 'carro pequeno'>'carro grande':
            ve_comu = 'carro pequeno'

        if 'moto'> 'carro grande' and 'moto'>'carro pequeno':
            ve_comu = 'moto'

        print('----RELATÓRIO----')
        print(f'Veículo mais comum:{ve_comu}')
        
print('Você saiu')