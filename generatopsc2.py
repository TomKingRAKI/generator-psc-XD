import random

while True:
    user_input = input("Wpisz 'start' aby rozpocząć generowanie kodów lub 'stop' aby zakończyć: ")
    
    if user_input == "start":
        while True:
            num_codes = input("Podaj liczbę kodów, które chcesz wygenerować: ")
            
            if not num_codes.isdigit():
                print("Nieprawidłowa wartość. Podaj liczbę całkowitą.")
                continue
            
            num_codes = int(num_codes)
            
            for i in range(num_codes):
                code = "0" + str(random.randint(100000000000, 999999999999))
                print("Wygenerowany kod Paysafecard: ", code)
                
            next_action = input("Wpisz 'stop' aby zakończyć generowanie lub 'dalej' aby kontynuować: ")
            
            if next_action == "stop":
                break
                
    elif user_input == "stop":
        print("Program zakończył działanie.")
        break
        
    else:
        print("Nieprawidłowe polecenie. Wpisz 'start' lub 'stop'.")
