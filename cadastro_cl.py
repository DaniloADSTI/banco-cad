import os
import cadastro_de_cliente
import cadastro_contas
import cadastro_cliente


def menu_inicial():
    os.system('cls')
    print('BOAS-VINDAS AO *BANCO FICTÍCIO*.\nAQUI SEU DINHEIRO RENDE 50% AO DIA.\nESCOLHA UMA OPÇÃO PARA CONTINUAR.')
    print('Digite 1 se você é CLIENTE')
    print('Digite 2 se você é FUNCIONÁRIO')
    print('Digite 0 para encerrar')

if __name__ == '__main__':
    lista_de_clientes = []
    lista_de_contas = []
    sistema = True
    cliente_logado = None

    while sistema:
        menu_inicial()
        try:
            opcao = int(input('Digite o número da opção desejada: '))
            if opcao == 1:
                verificar = int(input('Digite 1 para Cadastrar ou 2 para efetuar Login: '))
                if verificar == 1:
                    cadastro_de_cliente.cadastrando(lista_de_clientes)
                elif verificar == 2:
                    cliente_logado = cadastro_de_cliente.login(lista_de_clientes)
                    if cliente_logado:
                        if 'conta' not in cliente_logado:
                            cadastro_contas.criar_conta(lista_de_contas, cliente_logado)
                            cliente_logado['conta'] = lista_de_contas[-1]['numero']
                            print(f"Conta {cliente_logado['conta']} criada para o cliente {cliente_logado['nome']}.")
                        while True:
                            print('Selecione a operação:')
                            print('1. Depósito')
                            print('2. Saque')
                            print('3. Transferência')
                            print('4. Mostrar Saldo')
                            print('0. Sair')
                            escolha = int(input('Digite o número da opção desejada: '))
                            if escolha == 1:
                                valor_deposito = float(input('Digite o valor do depósito: '))
                                cadastro_contas.realizar_deposito(lista_de_contas, cliente_logado['conta'], valor_deposito)
                            elif escolha == 2:
                                valor_saque = float(input('Digite o valor do saque: '))
                                cadastro_contas.realizar_saque(lista_de_contas, cliente_logado['conta'], valor_saque)
                            elif escolha == 3:
                                numero_destinatario = int(input('Digite o número da conta destinatária: '))
                                destinatario = None
                                for conta in lista_de_contas:
                                    if conta['numero'] == numero_destinatario:
                                        destinatario = conta
                                        break
                                if destinatario:
                                    valor_transferencia = float(input('Digite o valor da transferência: '))
                                    cadastro_contas.realizar_transferencia(lista_de_contas, cliente_logado['conta'], destinatario, valor_transferencia)
                                else:
                                    print('Conta destinatária não encontrada.')
                            elif escolha == 4:
                                cadastro_contas.mostrar_saldo(lista_de_contas, cliente_logado['conta'])
                            elif escolha == 0:
                                break
                            else:
                                print('Opção inválida.')
                    else:
                        print('Login não realizado. Tente novamente.')
                else:
                    print('Opção inválida.')
            elif opcao == 2:
                def executar():
                    # Seu código da opção 2 aqui
                    print("Código da opção 2 executado.")


                # Definindo a classe Cliente
                class Cliente:
                    def __init__(self, nome, cpf, endereco, telefone, ):
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
                def criar_cliente(nome, cpf, endereco, telefone, ):
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

                            editar_cliente(cliente, nome, cpf, endereco, telefone, )
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
                            # pra sair
                            print("Volte Sempre :)")
                            break

                        else:
                            # Mensagem para escolha inválida
                            print("Escolha de 1 a 6.")


                # Verificando se o script está sendo executado diretamente
                if __name__ == "__main__":
                    main()

            elif opcao == 0:
                print('Volte sempre!')
                sistema = False
            else:
                print('Opção inválida. Tente novamente.')
        except ValueError:
            print('Valor inválido. Por favor, digite um número.')
