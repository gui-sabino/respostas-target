def verifica_letra_a(texto):
    # Converte o texto para minúsculo para facilitar
    texto = texto.lower()
    
    # Conta quantas vezes a letra 'a' aparece
    quantidade = texto.count('a')
    
    # Retorna se existe e a quantidade
    return quantidade > 0, quantidade

def main():
    # Solicita o texto ao usuário
    texto = input("Digite um texto para verificar a existência da letra 'a': ")
    
    # Solicita de novo se estiver vazio
    while not texto.strip():
        print("Texto vazio! Por favor, digite algum texto.")
        texto = input("Digite um texto para verificar a existência da letra 'a': ")
    
    # Verifica a existência e quantidade da letra 'a'
    existe, quantidade = verifica_letra_a(texto)
    
    # Exibe os resultados
    print("\nResultados da análise:")
    print(f"Texto analisado: {texto}")
    
    if existe:
        if quantidade == 1:
            print(f"A letra 'a' aparece {quantidade} vez no texto.")
        else:
            print(f"A letra 'a' aparece {quantidade} vezes no texto.")
    else:
        print("A letra 'a' não aparece no texto.")
    
    # Mostra a posição de cada ocorrência
    if existe:
        print("\nPosições onde a letra 'a' aparece:")
        texto_lower = texto.lower()
        for i, letra in enumerate(texto_lower):
            if letra == 'a':
                letra_original = texto[i]  # Pega a letra original
                print(f"Posição {i + 1}: '{letra_original}'") # Printa a posição + letra original

if __name__ == "__main__":
    main()