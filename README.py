# meus-exercicios-python-iniciante - 5
# São questões simples para minha pessoa ter uma ser noção do meu progresso. 

nota1 = float(input("1ª Nota: "))
nota2 = float(input("2ª Nota: "))
nota3 = float(input("3ª Nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7.0:
    print(f"\033[0:32mAprovado:\nNota: {media:.2f}.")
    
elif media >= 5.0:
    print(f"\033[0:33mRecuperação:\nNota: {media:.2f}.")
    
else:
    print(f"\033[0:31mReprovado:\nNota: {media:.2f}")
