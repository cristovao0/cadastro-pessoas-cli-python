import funcoes


while True:
    funcoes.menu(['Cadastrar Pessoas', 'Listar Pessoas','Buscar Pessoas', 'Remover Pessoa', 'Sair'])
    try:
        opcao = int(input('Digite a opção desejada: '))
    except(ValueError):
        print('Valor digitado não confere com umas das opções. Digite um valor válido.')
        continue
    else:
        if opcao == 1:

            nome = input('Nome ').title().strip()
            while nome == '':
                print('Campo vazio. Digite um nome.')
                nome = input('Nome ').title().strip()
            idade = int(input('Idade '))
            while idade < 0:
                print('Idade invalida, digite novamente')
                idade = int(input('Idade '))
            telefone = input('Telefone ')

            funcoes.adicionar_pessoas(nome,idade,telefone)
        
        elif opcao == 2:
            funcoes.listar_pessoas()

        elif opcao == 3:
            nome = input('Nome ').title().strip()

            funcoes.buscar_pessoa(nome)

        elif opcao == 4:
            nome = input('Nome ').title().strip()

            funcoes.remover_pessoa(nome)
        
        elif opcao == 5:
            break

        else:
            print('Decisão invalida. Entre com uma opção válida.')
            continue



