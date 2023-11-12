
# Definindo a classe Cliente
class Cliente:
    def __init__(self, nome, cpf, endereco, telefone,):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone


# Definindo a classe ContaBancaria
class ContaBancaria:
    def __init__(self, numero_conta, cliente):
        self.numero_conta = numero_conta
        self.cliente = cliente
        self.saldo = 0.0

# Listas para armazenar clientes e contas bancárias
clientes = []
contas_bancarias = []

# Função para criar um novo cliente
def criar_cliente(nome, cpf, endereco, telefone,):
    cliente = Cliente(nome, cpf, endereco, telefone, )
    clientes.append(cliente)
    return cliente

# Função para editar informações de um cliente existente
def editar_cliente(cliente, nome, cpf, endereco, telefone, ):
    cliente.nome = nome
    cliente.cpf = cpf
    cliente.endereco = endereco
    cliente.telefone = telefone

# Função para criar uma nova conta bancária para um cliente
def criar_conta_bancaria(cliente):
    numero_conta = len(contas_bancarias) + 1
    conta = ContaBancaria(numero_conta, cliente)
    contas_bancarias.append(conta)
    return conta

# Função para mostrar a conta de um cliente
def exibir_contas_cliente(cliente):
    contas_cliente = [conta.numero_conta for conta in contas_bancarias if conta.cliente == cliente]
    return contas_cliente

# Função para exibir os dados de um cliente
def exibir_dados_cliente(cliente):
    print(f"Nome: {cliente.nome}")
    print(f"CPF: {cliente.cpf}")
    print(f"Endereço: {cliente.endereco}")
    print(f"Telefone: {cliente.telefone}")

# Menu
def main():
    while True:
        print("\033[1;32m 1. Criar Cliente\033[m")
        print("\033[1;32m 2. Editar Cliente\033[m")
        print("\033[1;32m 3. Criar Conta Bancária\033[m")

        print("\033[1;32m 4. Exibir todos os Clientes\033[m")
        print("\033[1;32m 5. Visualizar Dados do Cliente\033[m")
        print("\033[1;32m 6. Sair\033[m")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # criar um novo cliente
            nome = input("Nome do cliente: ")
            cpf = input("CPF do cliente: ")
            endereco = input("Endereço do cliente: ")
            telefone = input("Número de telefone do cliente: ")

            cliente = criar_cliente(nome, cpf, endereco, telefone, )
            print(f"\033[7;33m Cliente '{cliente.nome}' criado com sucesso!\033[m")

        elif opcao == "2":
            # editar informações de um cliente
            if not clientes:
                print("Nenhum cliente cadastrado. Crie um cliente primeiro.")
                continue

            print("Clientes disponíveis:")
            for i, cliente in enumerate(clientes, start=1):
                print(f"{i}. {cliente.nome}")

            escolha_cliente = int(input("Escolha um cliente pelo número: "))
            cliente = clientes[escolha_cliente - 1]

            nome = input("Novo nome do cliente: ")
            cpf = input("Novo CPF do cliente: ")
            endereco = input("Novo endereço do cliente: ")
            telefone = input("Novo número de telefone do cliente: ")

            editar_cliente(cliente, nome, cpf, endereco, telefone,)
            print(f"Dados do cliente {cliente.nome} editados com sucesso!")

        elif opcao == "3":
            # criar uma nova conta bancária
            if not clientes:
                print("Nenhum cliente cadastrado. Crie um cliente primeiro.")
                continue

            print("Clientes disponíveis:")
            for i, cliente in enumerate(clientes, start=1):
                print(f"{i}. {cliente.nome}")

            escolha_cliente = int(input("Escolha um cliente pelo número: "))
            cliente = clientes[escolha_cliente - 1]
            conta = criar_conta_bancaria(cliente)
            print(f"Conta bancária {conta.numero_conta} criada para o cliente {cliente.nome}.")


        elif opcao == "4":
            # exibir as contas do cliente
            if not clientes:
                print("Nenhum cliente cadastrado. Crie um cliente primeiro.")
                continue

            print("Clientes Disponíveis:")
            for i, cliente in enumerate(clientes, start=1):
                print(f"{i}. {cliente.nome}")

            escolha_cliente = int(input("Escolha um cliente pelo número: "))
            cliente = clientes[escolha_cliente - 1]
            contas_cliente = exibir_contas_cliente(cliente)

            if not contas_cliente:
                print(f"O cliente {cliente.nome} não possui contas bancárias.")
            else:
                print(f"Contas bancárias do cliente {cliente.nome}: {contas_cliente}")

        elif opcao == "5":
            # visualizar dados do cliente
            if not clientes:
                print("Nenhum cliente cadastrado. Crie um cliente primeiro.")
                continue

            print("Clientes Disponíveis:")
            for i, cliente in enumerate(clientes, start=1):
                print(f"{i}. {cliente.nome}")

            escolha_cliente = int(input("Escolha o cliente pelo número: "))
            cliente = clientes[escolha_cliente - 1]
            exibir_dados_cliente(cliente)

        elif opcao == "6":
            #pra sair
            print("Volte Sempre :)")
            break

        else:
            # Mensagem para escolha inválida
            print("Escolha de 1 a 6.")

# Verificando se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
