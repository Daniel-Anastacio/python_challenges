def number_int():
    try:
        number = int(input("Digite um número\n"))
        return number
    except:
        print("Digite um número inteiro por favor!")
        number_int()

def finish():
    finish_ask = input("Deseja adicionar outro número? (S/N)")
    match finish_ask:
        case "S":
            print("Escolha mais um então")
            return True
        case "N":
            print("Fechando lista")
            return False
        case _:
            print("Digite algo válido por favor! (S/N)")
            finish()

def treatment(list_numbers, intervalo_1, intervalo_2, intervalo_3, intervalo_4):
    list_numbers.append(number_int())
    while finish() == True:
        list_numbers.append(number_int())
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

def main():
    list_numbers:list = []
    intervalo_1 = 0 #[0-25]
    intervalo_2 = 0 #[26-50]
    intervalo_3 = 0 #[51-75]
    intervalo_4 = 0 #[76-100]
    treatment(list_numbers, intervalo_1, intervalo_2, intervalo_3, intervalo_4)
    

main()