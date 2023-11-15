# таблица умножения от 1 до n 

# Парадигма структурная, так как отсутствует Goto и есть структурный код в "main"  и процедурная парадигма так как  таблица умножения выделена в 
# функцию для многократного использования 



def multiplication(n:int):
    for i in range(1,n+1):
        for j in range(1,10):
            print(f"{i}*{j}={j*i}")


if __name__ == "__main__":
    
    while True:
        num = input("Введите число, либо иное для выхода =")
        try:
            multiplication(int(num))
        except:
             break        