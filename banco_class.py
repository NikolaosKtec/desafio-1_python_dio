class Banco:
    def __init__(self):
        self.saldo = float(0)
        self.extratostr = str("")
        self.vlimite_diario = float(500)
        self.limite_atingido = bool(False)
        self.limite_saques = bool(False)
        self.LIMITE_SAQUES = int(3)
        self.numero_saques = int(0)
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

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
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
