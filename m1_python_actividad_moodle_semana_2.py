follow = True

inventory=[]

while follow:
    print("===BIENVENIDO A TU MENU===\nseleccione la opcion que desea realizar")
    print("1. Agregar un producto: ")
    print("2. Mostrar el inventario: ")
    print("3. Calcular estadisticas")
    print("4. SALIR")
    ask = int(input("ingrese la opcion que deseas realizar: "))
    if ask == 1:    
        while follow:
            ask_2=int(input("que opcion deseas realizar?\n1. crear un prodcuto\n2. salir al menu: "))
            try:                    
                if ask_2 == 1:
                    input_product = input("ingrese el nombre de su producto: ")
                    price_product = float(input("ingrese el preciom de su producto: "))
                    quantity_product = int(input("ingrese la cantidad de su producto: "))
                    dictionary={
                        "nombre":input_product,
                        "precio": price_product,
                        "cantidad":quantity_product
                    }
                    inventory.append(dictionary)
                    
                elif ask_2 == 2:
                    break
                elif ask_2 !=1 or 2:
                    print("================================")
                    print("ERROR: ingrese una opcion valida")
                    print("================================")
            except ValueError:
                print("\nERROR: solo valores numericos")
    elif ask == 2:
        if inventory == []:
            print("========================")
            print("su inventario esta vacio")
            print("========================")
        else:
            print("========TU INVENTARIO========")
            for y in inventory:
                print(f"Producto: {y['nombre']} | Precio: {y['precio']} | Cantidad: {y['cantidad']}")
            print("=============================")    
        
    elif ask == 3:
        for i in inventory:
            print("========================")
            print(f"-----su producto es {i['nombre']} su precio es {i['precio']} su cantidad es {i['cantidad']}-----\n-----El precio total de {i['nombre']} es {i['precio'] * i['cantidad']}-----")                
            print("========================")
    elif ask == 4:
        break                   

