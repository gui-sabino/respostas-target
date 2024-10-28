def verifica_fibonacci(numero):
    if numero < 0:
        return False, []
    if numero == 0:
        return True, [0]
    if numero == 1:
        return True, [0, 1]
    
    # Inicializa a sequência com os dois primeiros números
    sequencia = [0, 1]
    
    # Gera a sequência até encontrar um número maior que o número informado
    while True:
        proximo = sequencia[-1] + sequencia[-2]
        if proximo > numero:
            # Imprime o booleano (se o número pertence a lista ou não) e a sequência até o momento
            return numero in sequencia, sequencia 
        sequencia.append(proximo)

def main():
    # Solicita a entrada
    try:
        numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

        # Verifica se o número está na sequência
        pertence, sequencia = verifica_fibonacci(numero)

        # Exibe a sequência gerada
        print("\nSequência de Fibonacci gerada:")
        print(", ".join(map(str, sequencia)))

        # Exibe o resultado
        if pertence:
            print(f"\nO número {numero} PERTENCE à sequência de Fibonacci!")
        else:
            print(f"\nO número {numero} NÃO pertence à sequência de Fibonacci!")

    # Trata valores diferentes de Int
    except ValueError:
        print("Por favor, digite um número inteiro válido!")
        main()

if __name__ == "__main__":
    main()