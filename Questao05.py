nota = input("Digite a nota 0 a 10 ")

try:
    nota = float(nota)

    if nota < 0 or nota > 10:
        print("A nota deve estar entre 0 e 10")
    elif nota >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

except ValueError:
    print("Digite apenas um número.")
