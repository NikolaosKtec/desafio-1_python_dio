class Banco:
    def __init__(self):
        self.saldo = float(0)
        self.extratostr = str("")
        self.vlimite_diario = float(500)
        self.limite_atingido = bool(False)
        self.limite_saques = bool(False)
        self.LIMITE_SAQUES = int(3)
        self.numero_saques = int(0)
        self.CADASTRO_PESSOA_FISICA = set()
        # self.CADASTRO_CONTAS = set()
        self.users = list()
        self.contas_c = list()
        self.seq = int(0)
    # [d] Depositar
    def deposito(self):
        
        try:
            valor = float(input("Informe o valor do depósito: "))
        except:
            print("valor de entrada é invalido!")

        if valor > 0:
            self.saldo += valor
            self.extratostr += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é negativo!")

    # [s] Sacar
    def saque(self):
        valor = float(input("Informe o valor do saque: "))

        if valor>self.saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor <= 0:
            print("Você nao pode sacar valores menor ou igual a zero!")


        self.limite_atingido = valor > self.vlimite_diario

        self.limite_saques = self.numero_saques >= self.LIMITE_SAQUES
  
        if self.limite_atingido:
            print("Operação falhou! O valor do saque excede o limite.")
            return
        elif self.limite_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            return
        self.saldo -= valor
        self.extratostr += f"Saque: R$ {valor:.2f}\n"
        self.numero_saques += 1

    # [e] Extrato
    def extrato(self):
        print("\n================ EXTRATO ================")

        if len(self.extratostr) == 0:
            print("Não foram realizadas movimentações.")

        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")
        print(f"\n {self.extratostr}")
        print("==========================================")

    def menu_principal(self):

        menu = """

        \t[d] Depositar
        \t[s] Sacar
        \t[e] Extrato
        \t[cc] Criar conta corrente
        \t[lc] Listas contas
        \t[c] Cadastrar usuario
        \t[q] Sair
        """
        while True:

            opcao = input(menu)

            if opcao == "d":
                self.deposito()
            elif opcao =="s":
                self.saque()
            elif opcao =="e":
                self.extrato()
            elif opcao == "q":
                break
            else:
                break

    def criar_usuario(self):

        nome = str(input("informe o Nome"))
        nas = str(input("informe a Data de nascimento"))

        try:
            cpf = int(input("Informe o CPF (somente números):"))
        except ValueError:
            print("somente números de 0-9 !")
        except:
            print("algo deu errado :(")
        
        if( cpf in self.CADASTRO_PESSOA_FISICA):
            print("Ops, ja existe alguém cadastrado com este CPF!, saindo do menu...")
            return
        
        self.CADASTRO_PESSOA_FISICA.add(cpf)
        self.users.append(Usuario(cpf, nome, nas, "endereço qualquer"))
        
    def criar_conta_corrente(self):
        
        agencia = input("informe agência (x-xxxx)")

        try:
            cpf = int(input("informe o cpf do titular"))
        except ValueError:
            print("somente números de 0-9 !")
        except:
            print("algo deu errado :(")

        if( not cpf in self.CADASTRO_PESSOA_FISICA):
            print("Não existe este CPF cadastrado em nosso banco! , saindo do menu...")
            return
        
        self.seq=+1
        n_conta = "000"+self.seq

        self.contas_c.append(Conta_c(agencia,n_conta,cpf))

    def listar_contas(self):
        print("\n================ CONTAS ================ \n")
        for i in self.contas_c:
            print("\t================ TITULAR ================\n")
            print(f"{i.usuario_key}\n")
            print("\t================ N° CONTA ================\n")
            print(f"{i.n_conta}\n")

class Usuario:
    def __init__(self, cpf, nome, nasc, ender):
        self.CPF = int(cpf)
        self.NOME = str(nome)
        self.DATA_NAS = str(nasc)
        self.ENDERECO = str(ender)

class Conta_c:
    def __init__(self,agencia, conta, usua_cpf):
        self.agencia = str(agencia)
        self.n_conta = str(conta)
        self.usuario_key = int(usua_cpf)