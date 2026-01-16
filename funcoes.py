from pathlib import Path

pessoas = Path(r'Cadastro de pessoas_V2\cadastro-pessoas-cli-python\pessoas.txt')

def checar_arquivo():
    if not pessoas.exists():
        pessoas.open('w').close()
        print(f'Arquivo {pessoas.name} criado')
    else:
        print(f'Arquivo {pessoas.name} já existe')


def form():
    print('-=' * 20)


def cabecalho(texto):
    form()
    print(f'{texto:^40}')
    form()


def menu(opcoes):
    cabecalho('Menu')

    for cont in range(0, len(opcoes)):
        print(f'{cont + 1} - {opcoes[cont]}')
    


def adicionar_pessoas(nome, idade, telefone):
    checar_arquivo()
    
    with pessoas.open('a', encoding='utf-8') as arquivo:
        arquivo.write(f'{nome};{idade};{telefone}\n')


def listar_pessoas():

    checar_arquivo()
    
    vazio = True
    dados = []
    # Gravo todos os dados na lista
    with pessoas.open('r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha == '':
                continue

            dados.append(linha.strip().split(';'))
            vazio = False

        form()
        if vazio:
            print('Nunhuma pessoa cadastrada')
        else:
        # Formato a lista para impressão
            for linha in dados:
                print(f'Nome: {linha[0]} | Idade: {linha[1]} | Telefone: {linha[2]}')


def buscar_pessoa(texto):
    dados = []
    vazio = True
    encontrou = False
    with pessoas.open('r',encoding='utf-8') as arquivo:
        for linhas in arquivo:
            linhas = linhas.strip()
            if linhas == '':
                continue

            dados.append(linhas.strip().split(';'))
            vazio = False
    if vazio:
        print('Arquivo Vazio')
        return
    
    texto = texto.lower()
   
    for linha in dados:
        if texto in linha[0].lower():
            form()
            print(f'Nome encontrado: {linha[0].title()}')
            encontrou = True
    if encontrou ==  False:
        form()
        print('Nenhum nome encontrado')

    
def remover_pessoa(nome):
    nome = nome.strip().lower()

    linhas_mantidas = []
    encontrou = False

    with pessoas.open('r', encoding='utf-8') as arquivo:
        for linhas in arquivo:
            linhas = linhas.strip()
            if linhas[0] == '':
                continue

            dados = linha.split(';')
            
            if dados[0].lower() == nome:
                encontrou = True
            else:
                linhas_mantidas.append(dados)

        if encontrou:
            print(f'{nome.title()} apagado com sucesso.')
        else:
            print(f'{nome.title()} não encontrado.')

    with pessoas.open('w', encoding='utf-8') as arquivo:
        for linha in linhas_mantidas:
            linha = ';'.join(linha)
            arquivo.write(f'{linha}\n')


        
        

            


    
    

    
        


