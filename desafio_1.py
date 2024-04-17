def number_int()->int:
    """Função para gerar um número inteiro e suportar as interações do usuário

    Returns:
        int: Número que será lido e colocado em um intervalo
    """
    try:
        number = int(input("Digite um número\n"))
        return number
    except:
        print("Digite um número inteiro por favor!")
        number_int()

def finish()->bool:
    """Função que suporta as interações do usuário e pergunta ao usuário se deseja finalizar o programa ou não

    Returns:
        bool: Variável que será interpretada como resposta do usuário
    """
    finish_ask:str = input("Deseja adicionar outro número e enviar este para leitura? (S/N)").strip().upper()
    while finish_ask != "S" and finish_ask != "N":
        print("Digite algo válido!!!")
        finish_ask:str = input("Deseja adicionar outro número e enviar este para leitura? (S/N)").strip().upper() 
    match finish_ask:
        case "S":
            print("Escolha mais um então")
            return False
        case "N":
            print("Fechando lista")
            return True
        
def main()->None:
    """Função que chama as outras e controla o fluxo do programa
    """
    list_numbers:list = []
    intervalo_1 = 0 #[0-25]
    intervalo_2 = 0 #[26-50]
    intervalo_3 = 0 #[51-75]
    intervalo_4 = 0 #[76-100]
    while True:
        list_numbers.append(number_int())
        if finish():
            break
        
    print(f"Esta é a sua lista de números {list_numbers}")
    for index in list_numbers:
        match index:
            case num if num in range(0, 26):
                intervalo_1+=1
            case num if num in range(26, 51):
                intervalo_2+=1
            case num if num in range(51, 76):
                intervalo_3+=1
            case num if num in range(76, 101):
                intervalo_4+=1
            case num if num < 0:
                print(f"{index} é um número negativo, finalizando contagem...")
                break
            case _:
                print("Fora do range")

    print(f"No primeiro intervalo de 0 a 25 temos {intervalo_1} números\nNo segundo intervalo de 26 a 50 temos {intervalo_2} números\nNo terceiro intervalo de 51 a 75 temos {intervalo_3} números\nNo quarto intervalo de 76 a 100 temos {intervalo_4} números")
    
main()
