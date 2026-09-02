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
        b = input("Nome para consultar: ")
        achou = 0
        qtd = 0
        while qtd < len(nomes) and achou == 0:
            if nomes[qtd] == b:
                achou = 1
                print("Nome: " + nomes[qtd])
                print("Idade: " + str(idades[qtd]))
                print("E-mail: " + emails[qtd])
            else:
                qtd += 1
        if achou == 0:
            print("Nao encontrado")

    elif op == 3:
        b = input("Nome para alterar: ")
        achou = 0
        qtd = 0
        while qtd < len(nomes) and achou == 0:
            if b == nomes[qtd]:
                achou = 1
                print("Dados atuais:")
                print("Nome: " + nomes[qtd])
                print("Idade: " + str(idades[qtd]))
                print("E-mail: " + emails[qtd])
                nomes[qtd] = input("Novo nome: ")
                idades[qtd] = int(input("Nova idade: "))
                emails[qtd] = input("Novo e-mail: ")
                print("Alterado!")

        if achou == 0:
            print("Nao encontrado") 
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