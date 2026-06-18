preço = int(input("Digite um valor: R$"))
print(f"Você digitou R${preço:.2f}")
novo_preço = preço - (preço * 0.05)
print(f"Seu produto com desconto tem valor de R${novo_preço:.2f}")
