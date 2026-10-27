class ContaBancaria:
      def __init__(self, numero, titular, saldo = 0):
            self.numero = self.__verificarNumero(numero)
            self.titular = self.__verificarTitular(titular)
            self.__saldo = saldo
            print("Conta criada")
      
      def __verificarNumero(self, numero):
            if not numero:
                  raise ValueError("Não pode ser valor nulo")
            
            return str(numero).strip()
      
      def __verificarTitular(self, titular: str):
            if not titular:
                  raise ValueError("IllegalArgumentValueError")
            
            if len(titular) < 3:
                  raise ValueError("Titular deve ter mais de 3 caractéres")
            
            return titular.strip()
            
      def depositar(self, valor):
            if valor <= 0:
                  raise ValueError("IllegalArgumentValueError")
            
            self.__saldo += float(valor)
            return True
            
      def sacar(self, valor):
            if valor <= 0:
                  raise ValueError("IllegalArgumentValueError")
            
            if valor > self.__saldo:
                  raise ValueError("SaldoInsuficienteValueError")

            self.__saldo -= float(valor)
            return True
      
      def transferir(self, destino, valor):
            if self is destino:
                  raise ValueError("Mesma conta!")
            
            if not isinstance(destino, ContaBancaria):
                  raise ValueError("Destino não é uma conta bancária")
            
            try:
                  self.sacar(valor)
            except ValueError or error:
                  raise ValueError("Não foi possível sacar o valor da própria conta")

            destino.depositar(valor)
            
      def consultarSaldo(self):
            return self.__saldo
                  

