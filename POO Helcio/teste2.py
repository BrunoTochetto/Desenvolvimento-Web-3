from helcio import ContaBancaria

# Crie três contas bancárias:
# Ana Lima: conta 123, saldo inicial de R$ 500,00.
# Carlos Souza: conta 456, saldo inicial de R$ 300,00.
# Maria Silva: conta 789, saldo inicial de R$ 100,00.
ana = ContaBancaria(123, "Ana Lima", 500)
carlos = ContaBancaria(456, "Carlos Souza", 300)
maria = ContaBancaria(789, "Maria Silva", 100)

# Realize as operações:
# Ana transfere R$ 200,00 para Carlos.
# Carlos transfere R$ 150,00 para Maria.
# Maria tenta transferir R$ 500,00 para Ana.
# O programa deve tratar a exceção da terceira transferência.
# Exiba o saldo final das três contas.

ana.transferir(carlos, 200)
carlos.transferir(maria, 150)

try:
    maria.transferir(ana, 500)
except ValueError as erro:
    print(f"Erro na transferência: {erro}")

print(f"Ana Lima: {ana.consultarSaldo()}")
print(f"Carlos Souza: {carlos.consultarSaldo()}")
print(f"Maria Silva: {maria.consultarSaldo()}")