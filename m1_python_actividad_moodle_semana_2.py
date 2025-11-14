#defino el true con la palabra follow
follow = True
#aqui dejo la lista vacia para el print y los procesos de mas adelante
inventory=[]

#aqui este while se encarga de mantener el ciclo activo hasta que se cierre
while follow:
        #aqui hago los prints de las opciones, en estas se define lo que se puede realizar dentro del menu
        print("===BIENVENIDO A TU MENU===\nseleccione la opcion que desea realizar")
        print("1. Agregar un producto: ")
        print("2. Mostrar el inventario: ")
        print("3. Calcular estadisticas")
        print("4. SALIR")
        #este while se encarga de de mantener el ciclo en este bloque de codigo activo por si llega  aocurrir un error
        while follow:
            #este bloque se encarga de leer el input, en caso de que no se encuentre un valor valido o se pongan opciones que no estan, pondra error y redirecionara a la opcion del input para que vuelva  aingresar una respuesta
            try:
                ask = int(input("ingrese la opcion que deseas realizar: "))
                break
            # este es el que devuelve el error si es que se obtiene un valor invalido
            except ValueError:
                print("ERROR: solo datos numericos")    
        #esta condicion se encarga de reproducir un bloque de codigo si la opcion ask es igual al numero 1
        if ask == 1:
            #aqui otro ciclo poara que se siga repitiendo elbucle en caso de valor invalido    
            while follow:
                
                try:
                    #segunda pregunta, estas preguntas entan dentro de la opcion 1, al terminar de ingresar los datos del producto uno vuelve a empezar ya que se encuentra dentro del ciclo while. para eso se hizo dentro de el
                    ask_2=int(input("que opcion deseas realizar?\n1. crear un prodcuto\n2. salir al menu: "))                    
                    #aqui se toma una decision de lo que se quiere hacer dentro de este menu, si se quiere ingresar un producto o volver al menu principal
                    if ask_2 == 1:
                        #en este apartado nos encargamos de ingresar todos los datos del prodcto definiendolos en variabl;es para su uso despues
                        input_product = input("ingrese el nombre de su producto: ")
                        price_product = float(input("ingrese el precio de su producto: "))
                        quantity_product = int(input("ingrese la cantidad de su producto: "))
                        #en este diccionario nos encargamos de guardar toda la informacion de los productos que recien ponemos en los inputs correspondientes de la parte de arriba
                        dictionary={
                            #aqui definimos las calves y los valores, estos valores se hacen con las variables de los inputs ya que se pueden agregar varios productos de forma continua
                            "nombre":input_product,
                            "precio": price_product,
                            "cantidad":quantity_product
                        }
                        #aqui nos encargamos de agregar a nuestra lista que esta definida al inicio del codigo toda la informacion que vamos a gregando al diccionario con los inputs definidos
                        inventory.append(dictionary)
                    #aqui esta la seguinda opcion del menu interno, este nos redirecciona al menu principal    
                    elif ask_2 == 2:
                        #aqui paramos la secuencia para retirarse de esta parte del codigo
                        break
                    #aqui definios un error, si la respuesta que se ingresa en el input es diferente a las opciones propuestas se hace el print de error    
                    elif ask_2 !=1 or 2:
                        #mensaje de error por dato invalido
                        print("================================")
                        print("ERROR: ingrese una opcion valida")
                        print("================================")
                #aqui tambien definimos un error, si alguna de las opciones qeu se ingresen es diferente a las que se solicitan se accede a esta parte del codigo y printea el error        
                except ValueError:
                    print("\nERROR: solo valores numericos")
        #aqui regresamos al inventario principal, especificamente a la opcion
        elif ask == 2:
            #aqui hacemos una validacion del invenatrio, si no se agrego ningun producto a la lista despues de todos estos procesos se imprime que el inventario esta vacio
            if inventory == []:
                print("========================")
                print("su inventario esta vacio")
                print("========================")
            #aqui revisamos que si el inventario no esta vacio entonces muestre todos los productos que temeos en el, con su nombre, precio y cantidad   
            else:
                print("========TU INVENTARIO========")
                for y in inventory:
                    print(f"Producto: {y['nombre']} | Precio: {y['precio']} | Cantidad: {y['cantidad']}")
                print("=============================")    
        #aqui realizamos los calculos, con los datos que ya tenemos de bloques de codigo anteriores y imprimimos el nobre de cada producto y el total de dinero que hay en el invenatrio de ese producto    
        elif ask == 3:
            for i in inventory:
                print("========================")
                print(f"-----su producto es {i['nombre']} su precio es {i['precio']} su cantidad es {i['cantidad']}-----\n-----El precio total de {i['nombre']} es {i['precio'] * i['cantidad']}-----")                
                print("========================")
        #aqui si se toma la decision de salir del menu principal se va a cerrar la ejecucion por completo ya que tenemos un break que hace que se detenga todo el codigo
        elif ask == 4:
            break                   

