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
    print("5 - Analisar pessoas")
    print("6 - Sair")
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

def listar_pessoas(nomes, idades, emails):
    pos = 0
    if len(nomes) == 0:
        print("Nenhuma pessoa cadastrada")
        
    while pos < len(nomes):
        exibir_pessoa(nomes, idades, emails, pos)
        pos += 1

def analizar_pessoa(nomes, idades, emails):
    procurado = input("Nome para analisar: ")
    pos = buscar_pessoa (nomes, procurado)

    if pos == -1:
        print("Pessoa não encontrada")
    else:
        idade = idades [pos]
        email = emails [pos]

        if idade < 12:
            print("Faixa etaria: Crianca")
        elif idade < 18:
            print("Faixa etaria: Adolescente")
        elif idade < 30:
            print("Faixa etaria: Adulto jovem")
        elif idade < 60:
            print("Faixa etaria: Adulto")
        else:
            print("Faixa etaria: Idoso")
        if email == "":
            print("Cadastro incompleto: sem e-mail")
        else:
            if "@" not in email:
                print("E-mail invalido")
            else:
                if email.endswith("@gmail.com"): 
                    print("Provedor: Gmail")
                elif email.endswith("@outlook.com"): 
                    print("Provedor: Outlook")
                elif email.endswith("@hotmail.com"): 
                    print("Provedor: Hotmail")
                elif email.endswith("@utfpr.edu.br"):
                    print("Provedor: UTFPR")
                else:
                    print("Provedor: Outro")
                    if idade >= 18 and email != "":
                        print("Cadastro apto para contato")
                    elif idade > 18 and email == "":
                        print("Maior de idade sem contato")
                    elif idade < 18 and email != "":
                        print("Menor de idade com contato")
                    else: print("Menor de idade sem contato")

nomes = []
idades = []
emails = []
 
qtd = 0
op = 0
 
while op != 6:

    op = exibir_menu()

    if op == 1:
        cadastrar_pessoa(nomes, idades, emails)

    elif op == 2:
        consultar_pessoa(nomes, idades, emails)

    elif op == 3:
        alterar_pessoa(nomes, idades, emails)

    elif op == 4:
        listar_pessoas(nomes, idades, emails)

    elif op == 5:
        analizar_pessoa(nomes, idades, emails)

    elif op == 6:
        print("Saindo...")

    else:
        print("Opcao invalida")

print("Fim do programa")