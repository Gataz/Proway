def creditopt():
    print ("""\nTemos as seguintes opções de crédito:
        1 - investimento
        2 - capital de giro
        3 - financiamento
        4 - sair\n""")
    clientopt = int(input('\nSobre qual linha de crédito você deseja maiores informações?\n'))
    while clientopt == 1:
        investinit()
    while clientopt == 2:
       cginit() 
    while clientopt == 3:
        finantinit()
    while clientopt == 4:
        print ('\nObrigado por nos procurar, volte quando quiser contratar uma de nossas linhas de crédito!\n')
        exit()
    else:
        print ('\nNão entendi, por favor repita')
        creditopt()
    
def investinit():
    print('É nossa linha de crédito voltada para implementação de melhorias')
    qinvestinit = int(input("""\nGostaria de contratar?
        1 - sim
        2 - não
        3 - sair\n"""))
    while qinvestinit == 1:
        print('Vamos dar uma olhadinha?\n')
        investrev()
    while qinvestinit == 2:
        print('Entendo. Veremos as linhas de crédito disponíveis.\n')
        creditopt()
    while qinvestinit == 3:
        print ('\nFoi um prazer lhe atender!\n')
        exit()
    else:
        print('Opção não reconhecida')
        exit()

def cginit():
    print ('É nossa linha de crédito destinada a despesas empresariais')
    qcginit = int(input("""\nGostaria de contratar?
        1 - sim
        2 - não
        3 - sair\n"""))
    while qcginit == 1:
        print('Vamos dar uma olhadinha?')
        cgrev()
    while qcginit == 2:
        print('Entendo. Veremos as linhas de crédito disponíveis.\n')
        creditopt()
    while qcginit == 3:
        print ('\nFoi um prazer lhe atender!\n')
        exit()
    else:
        print('Opção não reconhecida')
        exit()

def finantinit():
    print ('É nossa linha de crédito com finalidade definida previamente')
    qfinantinit = int(input("""\nGostaria de contratar?
        1 - sim
        2 - não
        3 - sair\n"""))
    while qfinantinit == 1:
        print('\nVamos dar uma olhadinha?\n')
        finantrev()
    while qfinantinit == 2:
        print('\nEntendo. Veremos as linhas de crédito disponíveis.\n')
        creditopt()
    while qfinantinit == 3:
        print ('\nFoi um prazer lhe atender!\n')
        exit()
    else:
        print('\nOpção não reconhecida\n')
        exit()

def investrev():
    print('\nA opção de INVESTIMENTO é nossa linha de crédito voltada para implementação de melhorias\n')
    qinvestrev= int(input("""\nVocê confirma a contratação?
    1 - sim
    2 - não
    3 - sair\n"""))
    while qinvestrev == 1:
        print ('\nParabéns pela contratação\n')
        exit()
    while qinvestrev == 2:
        print ('\nOk!Acredito que deseja ver outra linha de crédito.\n')
        creditopt()
    while qinvestrev == 3:
        print ('\nPoxa, não desanmime e volte em breve. Obrigado pela atenção!\n')
        exit()
    else:
        print ('\nNão entendi. Tente novamente.\n')
        investrev()

def cgrev():
    print('\nA opção de CAPITAL DE GIRO é nossa linha de crédito destinada a despesas empresariais\n')
    qcgrev= int(input("""\nVocê confirma a contratação?
    1 - sim
    2 - não
    3 - sair\n"""))
    while qcgrev == 1:
        print ('\nParabéns pela contratação\n')
        exit()
    while qcgrev == 2:
        print ('\nOk!Acredito que deseja ver outra linha de crédito.\n')
        creditopt()
    while qcgrev == 3:
        print ('\nPoxa, não desanmime e volte em breve. Obrigado pela atenção!\n')
        exit()
    else:
        print ('\nNão entendi. Tente novamente.\n')
        cgrev()

def finantrev():
    print('\nA opção de FINANCIAMENTO é nossa linha de crédito com finalidade definida previamente\n')
    qfinantrev= int(input("""\nVocê confirma a contratação?
    1 - sim
    2 - não
    3 - sair\n"""))
    while qfinantrev == 1:
        print ('\nParabéns pela contratação\n')
        exit()
    while qfinantrev == 2:
        print ('\nOk!Acredito que deseja ver outra linha de crédito.\n')
        creditopt()
    while qfinantrev == 3:
        print ('\nPoxa, não desanmime e volte em breve. Obrigado pela atenção!\n')
        exit()
    else:
        print ('\nNão entendi. Tente novamente.\n')
        finantrev()

greetings = True
while greetings != 3:
    print('Olá!\nResponda a pergunta: está precisando de crédito?\n')
    greetings = input("""
    1 - sim
    2 - não
    3 - Apenas curiosidade?\n""").lower()
    
    if greetings == '1':
        creditopt()
    elif greetings == '2':
        print ('\nEstaremos aqui quando precisar\n!')
        exit()
    elif greetings == '3':
        creditopt()
    else:
        print('\nDesculpe não entendi\n')
        exit()