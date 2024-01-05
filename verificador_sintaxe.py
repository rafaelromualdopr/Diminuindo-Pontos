
def verifica_sintaxe(string):
    # Inicializa uma pilha vazia para armazenar os colchetes de abertura
    lista = []

    # Define um dicionário para mapear colchetes de fechamento aos correspondentes de abertura
    mapeamento = {')': '(', '}': '{', ']': '['}

    # Itera sobre cada caractere na string
    for caractere in string:
        # Se o caractere for um colchete de abertura, adiciona à pilha
        if caractere in mapeamento.values():
            lista.append(caractere)
        # Se o caractere for um colchete de fechamento
        elif caractere in mapeamento:
            # Verifica se a pilha está vazia ou se o colchete de fechamento corresponde ao último colchete de abertura
            if not lista or lista.pop() != mapeamento[caractere]:
                # Se não corresponder, a sintaxe é incorreta
                return False

    # A sintaxe é correta se a pilha estiver vazia no final
    return not lista

# Exemplos de uso
print(verifica_sintaxe("()(()())"))  # Saída: True
print(verifica_sintaxe("))))"))      # Saída: False
print(verifica_sintaxe(")("))        # Saída: False