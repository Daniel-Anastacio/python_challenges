menu = [
    ("Cachorro Quente", "101", 1.20),
    ("Bauru Simples", "102", 1.30),
    ("Bauru com ovo", "103", 1.50),
    ("Hambúrguer", "104", 1.20),
    ("Cheeseburguer", "105", 1.30),
    ("Refrigerante", "106", 1.00)
]

def note_issue (request:list)->None:
    """Função para ler uma lista de itens (um pedido)

    Args:
        request (list): Um pedido, é uma lista contendo outras listas cada uma dessas listas contidas possui apenas dois indíces, o pedido é do tipo [[a,b],[c,d]...]
    """
    total_price:float = 0.0
    for i in range(len(request)):
        item_code:tuple = search(request[i][0])#Variável local para melhor leitura
        print(f"O pedido número {i+1}, {item_code[0]}, quantidade: {request[i][1]} custa: R${item_code[2]* request[i][1]:.2f}")
        total_price+=item_code[2]*request[i][1]
    print(f"O valor total do pedido é de R${total_price}")

def search(code:str)->any:
    """Função para encontrar elemento do cardápio de acordo com um código inteiro

    Args:
        code (str): Código de algum item do cardápio ou não

    Returns:
        any: O retorno irá funcionar de acordo com a existência do código no cardápio no cardápio
    """
    for x in menu:
        if x[1] == str(code):     
            return x

def number_int()->int:
    """Função para gerar um número inteiro e não quebrar com interação 

    Returns:
        int: Número inteiro que representa a quantidade de itens escolhidos
    """
    try:
        number:int = int(input("Quantos deste você vai querer?\n"))
        if number < 0:
            print("Escreva um número maior que zero")
        else:
            return number
    except:
        print("Digite um número inteiro por favor!")
        number_int()

def check_request()->None:
    request_item:list = []
    code:str = input("Qual é o código do seu pedido?\n")

    while search(code) == None:
        code:str = input("Digite algo válido!!!\n")
    request_item.append(code)


def request()->list:
    """Função para gerar um item do pedido

    Returns:
        list: Esta lista é a representação de um item do pedido, com código e quantidade 
    """
    request_item:list = []
    code:str = input("Qual é o código do seu pedido?\n")
    while search(code) == None:
        code:str = input("Digite algo válido!!!\n")
    
    quantify:int = number_int()
    request_item.append(code)
    request_item.append(quantify)
    print(f"O pedido, {search(code)[0]} a R${search(code)[2]:.2f} cada um, sendo {quantify}, custam R${(search(code)[2]*quantify):.2f}")
    print("Item escolhido com sucesso")
    return request_item

def finish()->bool:
    """Função que testa se o usuário quer continuar ou finalizar o programa

    Returns:
        bool: Variável usada para interromper ou continuar o laço while
    """
    
    finish_ask:str = input("Deseja finalizar o pedido? (S/N)").strip().upper()
    while finish_ask != "S" and finish_ask != "N":
        print("Digite algo válido!!!")
        finish_ask:str = input("Deseja finalizar o pedido? (S/N)").strip().upper()  
    match finish_ask:
        case "S":
            print("Finalizando pedido...")
            return True
        case "N":
            print("Escolha mais um então")
            return False

def showing_menu()->None:
    """Função para exibir cardápio
    """
    print("\t\tCardápio")
    print("\n\tPrato || \tPreço")
    for x in menu:
        print(f"\n\t| {x[1]} || \t{x[0]} || \t{x[2]:.2f} |")
    print("\n\n")

def main()->None:
    """Função central que chama as outras
    """
    showing_menu()
    request_list:list = []
    while True:
        request_list.append(request())
        if finish():
            break
    note_issue(request_list)
    
main()
