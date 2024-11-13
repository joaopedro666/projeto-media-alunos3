# media.py (atualizado para média ponderada)

def calcular_media_ponderada(notas):
    # A primeira e a segunda nota têm peso 1, e a terceira tem peso 2
    return (notas[0] + notas[1]) / 2 + notas[2] * 2 / 4

def verificar_situacao(media):
    if media >= 6.0:
        return "Aprovado"
    elif 5.0 <= media < 6.0:
        return "Recuperação"
    else:
        return "Reprovado"

def main():
    notas = []
    for i in range(3):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
    
    media = calcular_media_ponderada(notas)
    situacao = verificar_situacao(media)
    
    print(f"A média ponderada das notas é: {media:.2f}")
    print(f"Situação do aluno: {situacao}")

if __name__ == "__main__":
    main()