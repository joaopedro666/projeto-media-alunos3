# media.py (atualizado)

def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_aprovacao(media):
    if media >= 6.0:
        return "Aprovado"
    else:
        return "Reprovado"

def main():
    notas = []
    for i in range(3):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
    
    media = calcular_media(notas)
    situacao = verificar_aprovacao(media)
    
    print(f"A média das notas é: {media:.2f}")
    print(f"Situação do aluno: {situacao}")

if __name__ == "__main__":
    main()