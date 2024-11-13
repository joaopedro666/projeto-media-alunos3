def calcular_media(notas):
    """Função para calcular a média aritmética"""
    return sum(notas) / len(notas)

def main():
    # Receber as 3 notas do aluno
    notas = []
    for i in range(3):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
    
    # Calcular a média
    media = calcular_media(notas)
    
    # Exibir o resultado
    print(f"A média das notas é: {media:.2f}")

if __name__ == "__main__":
    main()