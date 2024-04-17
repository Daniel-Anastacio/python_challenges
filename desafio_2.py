class Comidas:
    def __init__(self, name, code, price) -> None:
        self.name = name
        self.code = code
        self.price = price


menu = [
    ("Cachorro Quente", "101", 1.20),
    ("Bauru Simples", "102", 1.30),
    ("Bauru com ovo", "103", 1.50),
    ("Hambúrguer", "104", 1.20),
    ("Cheeseburguer", "105", 1.30),
    ("Refrigerante", "106", 1.00)
]

def note_issue (request:list):
    total_price:float = 0.0
    for i in range(len(request)):
        item_code = search(request[i][0])#Variável local para melhor leitura
        print(f"O pedido número {i+1}, {item_code[0]}, quantidade: {request[i][1]} custa: R${pricing(item_code[2], request[i][1])}")
        total_price+=pricing(item_code[2], request[i][1])
    print(f"O valor total do pedido é de R${total_price}")

def search(code:int)->any:
    for x in menu:
        if x[1] == code:
            return x
    return False

def pricing(unit_price:float, quantify:int) -> float:
    return unit_price*quantify

def number_int():
    try:
        number = int(input("Quantos deste você vai querer?\n"))
        return number
    except:
        print("Digite um número inteiro por favor!")
        number_int()

def request()->list:
    request_item:list = []
    code:str = input("Qual é o código do seu pedido?\n")

    if search(code) == False:
        print("Código não encontrado")
        request()
    
    quantify:int = number_int()
    request_item.append(code)
    request_item.append(quantify)
    print(f"O pedido, {search(code)[0]} a R${search(code)[2]} cada um, sendo {quantify}, custam {pricing(search(code)[2], quantify)}")
    print("Item escolhido com sucesso")
    return request_item

def finish():
    finish_ask = input("Deseja finalizar o pedido? (S/N)")
    match finish_ask:
        case "S":
            print("Finalizando pedido...")
            return False
        case "N":
            print("Escolha mais um então")
            return True
        case _:
            print("Digite algo válido por favor! (S/N)")
            finish()

def main():
    request_list:list = []
    request_list.append(request())
    while finish()==True:
        request_list.append(request())
    note_issue(request_list)
    
main()