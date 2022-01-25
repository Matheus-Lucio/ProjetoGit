inventario=[]
continuar = "S"

while continuar == "S":
  resposta1 = "S"
  print("1 - Cadastrar produto")
  print("2 - Buscar produto")
  print("3 - Descontar produto")
  print("4 - Excluir produto")
  print("5 - Sair")
  resposta = int(input("Digite o número da ação a ser tomada: "))
  if resposta == 1:
    while resposta1 == "S":
      equipamento = [input("Equipamento: "),
                     float(input("Valor: ")),
                     int(input("Número Serial: ")),
                     input("Departamento: ")]
      inventario.append(equipamento)
      resposta1 = input("Digite S para continuar: ").upper()
    continuar = input("Digite S caso queira voltar ao Menu: ").upper()

# Buscador de produtos
  if resposta == 2:
    while resposta1 == "S":
      busca = input("Digite o nome do equipamento que deseja buscar: ")
      for elemento in inventario:
        if busca == elemento[0]:
          print("Valor..: ", elemento[1])
          print("Serial.:", elemento[2])
          resposta1 = input("Digite S para continuar: ").upper()
    continuar = input("Digite S caso queira voltar ao Menu: ").upper()

# Descontando 10% do valor de um equipamento
  if resposta == 3:
    while resposta1 == "S":
      depreciacao = input("Digite o nome do equipamento que será depreciado: ")
      for elemento in inventario:
        if depreciacao == elemento[0]:
          print("Valor antigo: ", elemento[1])
          elemento[1] = elemento[1] * 0.9
          print("Novo valor: ", elemento[1])
          resposta1 = input("Digite S para continuar: ").upper()
    continuar = input("Digite S caso queira voltar ao Menu: ").upper()

# Eliminado determinado equipamento pelo seu número serial
  if resposta == 4:
    while resposta1 == "S":
      serial = int(input("Digite o serial do equipamento que será excluído: "))
      for elemento in inventario:
        if elemento[2] == serial:
          inventario.remove(elemento)

      for elemento in inventario:
        print("Nome.........: ", elemento[0])
        print("Valor........: ", elemento[1])
        print("Serial.......: ", elemento[2])
        print("Departamento.: ", elemento[3])

      resposta1 = input("Digite S para continuar: ").upper()
    continuar = input("Digite S caso queira voltar ao Menu: ").upper()

  if resposta == 5:
    exit()