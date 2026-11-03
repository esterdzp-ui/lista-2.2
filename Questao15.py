nome = input("Digite o nome do personagem: ")
nivel = int(input("Digite o nível:"))
tem_magia = input("Tem magia? (Sim/Não):").lower() == "sim"

print(f"Personagem:{nome}|Nível:{nivel}|Possui Magia:{tem_magia}")
