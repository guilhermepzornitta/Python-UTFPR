# Sistema de Cadastro de Pessoas - versao 2
# novos requisitos: menu, consulta, alteracao e listagem
 
def exibir_menu():
    print("=========================")
    print(" CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Sair")
    return int(input("Escolha uma opcao: "))

def cadastrar_pessoa(nomes, idades, emails):
    n = input("Nome: ")
    i = int(input("Idade: "))
    e = input("E-mail: ")
    nomes.append(n)
    idades.append(i)
    emails.append(e)
    print("Pessoa cadastrada!")
    print("Nome: " + n)
    print("Idade: " + str(i))
    print("E-mail: " + e)
    if i >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade") 

def exibir_pessoa(nomes, idades, emails, pos):
    print("Nome: " + nomes[pos])
    print("Idade: " + str(idades[pos]))
    print("E-mail: " + emails[pos])
    if idades[pos] >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")

def buscar_pessoa(nomes, buscar_nome):
    pos = 0
    while pos < len(nomes):
        if nomes[pos] == buscar_nome:
            return pos
        pos += 1
    return -1

def consultar_pessoa(nomes, idades, emails):
    buscar = input("Nome para consultar: ")
    pos = buscar_pessoa(nomes, buscar)
    if pos != -1:
        exibir_pessoa(nomes, idades, emails, pos)
    else:
        print("Nao encontrado")

def alterar_pessoa(nomes, idades, emails):
    b = input("Nome para alterar: ")
    buscar = buscar_pessoa(nomes, b)
    if buscar != -1:
        print("Dados atuais:")
        exibir_pessoa(nomes, idades, emails, buscar)
        nomes[buscar] = input("Novo nome: ")
        idades[buscar] = int(input("Nova idade: "))
        emails[buscar] = input("Novo e-mail: ")
        print("Alterado!")
    else:
        print("Nao encontrado")

nomes = []
idades = []
emails = []
 
qtd = 0
op = 0
 
while op != 5:

    op = exibir_menu()

    if op == 1:
        cadastrar_pessoa(nomes, idades, emails)

    elif op == 2:
        consultar_pessoa(nomes, idades, emails)

    elif op == 3:
        alterar_pessoa(nomes, idades, emails)

    elif op == 4:
        pos = 0
        while pos < len(nomes):
            print("Nome: " + nomes[pos])
            print("Idade: " + str(idades[pos]))
            print("E-mail: " + emails[pos])
            pos += 1
    elif op == 5:
        print("Saindo...")
 
    else:
        print("Opcao invalida")
 
print("Fim do programa")