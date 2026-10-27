from conta import ContaBancaria

def teste(numero=None, titular=None):
      try:
            ContaBancaria(numero=numero, titular=titular)
      
      except Exception as erro:
            print("algo deu errado", erro)
            


conta = ContaBancaria(numero=123, titular="Ana Lima")
teste(titular="Al")

conta.depositar(100)
print(conta.consultarSaldo())
conta.depositar(0)

conta.depositar(-50)
conta.sacar(40)
print(conta.consultarSaldo())
conta.saldo = 100
conta.sacar(100)
print(conta.consultarSaldo())
conta.saldo = 100
conta.sacar(100.01)

outraConta = ContaBancaria(titular="asd", numero=2)
print(conta.consultarSaldo())
conta.saldo = 100
conta.transferir(outraConta, 100.01)
print(conta.consultarSaldo())
print(outraConta.consultarSaldo())

print(conta.transferir(conta, 1))

conta3 = ContaBancaria("2", "Wanderley Nascimento de Jesus Maria")