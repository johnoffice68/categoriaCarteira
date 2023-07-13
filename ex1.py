def verificar_categoria_veiculo(rodas, peso, pessoas):
    if rodas == 2 or rodas == 3:
        return "Categoria A"
    elif rodas == 4 and pessoas <= 8 and peso <= 3500:
        return "Categoria B"
    elif rodas >= 4 and peso > 3500 and peso <= 6000:
        return "Categoria C"
    elif rodas >= 4 and pessoas > 8:
        return "Categoria D"
    elif rodas >= 4 and peso > 6000:
        return "Categoria E"
    else:
        return "Categoria não determinada"


quantidade_rodas = int(input("Digite a quantidade de rodas do veículo: "))
peso_bruto = float(input("Digite o peso bruto do veículo (em kg): "))
quantidade_pessoas = int(input("Digite a quantidade de pessoas no veículo: "))

categoria = verificar_categoria_veiculo(quantidade_rodas, peso_bruto, quantidade_pessoas)
print("A melhor categoria de habilitação para o veículo informado é:", categoria)
