# Cadastro de Pessoas em Python (CLI)

Projeto em Python para cadastro de pessoas utilizando interface de linha de comando (CLI), com persistência de dados em arquivo texto.

O objetivo deste projeto é praticar e demonstrar fundamentos sólidos da linguagem Python, como organização de código, manipulação de arquivos, funções e controle de fluxo.

---

## 📌 Funcionalidades

- Cadastrar pessoas (nome, idade e telefone)
- Listar todas as pessoas cadastradas
- Buscar pessoas pelo nome (busca parcial)
- Remover pessoas pelo nome
- Menu interativo no terminal
- Tratamento básico de erros de entrada

Os dados são armazenados em um arquivo `pessoas.txt`, no formato: nome,idade,telefone

---

## 🛠️ Tecnologias e Conceitos Utilizados

- Python 3
- Funções
- Estruturas de repetição (`while`, `for`)
- Estruturas condicionais (`if`, `elif`, `else`)
- Manipulação de arquivos (`open`, leitura e escrita)
- Tratamento de exceções (`try/except`)
- Organização do projeto em módulos (`main.py` e `funcoes.py`)

---

## 📁 Estrutura do Projeto

cadastro_pessoas_v2/
│
├─ main.py # Fluxo principal e menu do sistema
├─ funcoes.py # Funções de cadastro, listagem, busca e remoção
└─ pessoas.txt # Arquivo de dados (criado automaticamente)

---

## ▶️ Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/cadastro-pessoas-cli-python.git

```
2. Acesse a pasta do projeto
```bash
cd cadastro-pessoas-cli-python

```
3. Execute o projeto
```
python main.py

```
🎯 Objetivo do Projeto

Este projeto foi desenvolvido com foco em aprendizado e consolidação dos fundamentos de Python, servindo como base para projetos mais avançados no futuro, como aplicações com banco de dados, interfaces gráficas ou aplicações web.

🚀 Possíveis Melhorias Futuras

Validação mais robusta dos dados de entrada

Uso de arquivos CSV ou JSON

Implementação de IDs para os registros

Interface gráfica ou versão web

👤 Autor

Projeto desenvolvido por Cristovão Cavalcante
Com foco em aprendizado, prática e evolução contínua em Python.



