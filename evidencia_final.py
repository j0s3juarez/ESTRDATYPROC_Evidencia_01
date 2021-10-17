ID_Registro = [] 
Venta = []
Articulo = {}
Num_Venta  = 1
Counter = 0

try:
    with open('DataBaseStore.txt','r') as file:
        control = 0
        control2 = 0
        for line in file:
            puntos = line.find(':')
            if puntos != -1:
                x = line[:puntos]
                y = line[puntos+1:-1]
                Articulo[x] = y
                control2 += 1
                if control2 == 3:
                    Venta.append(Articulo)
                    Articulo = {}
                    control2 = 0
                else:
                    if line == '':
                        continue
                    if control < 2:
                        Venta.append(int(line[:-1]))
                        control += 1
                else:
                    ID_Registro.append(Venta)
                    Num_Venta  = Venta[-2] + 1
                    Venta = []
                    control = 0
                    except:
                        w = 1
                        opcion = input("[1] Registrar una Venta \t[2] Consultar una Venta \t[3] Salir: ")
                        while opcion != "3":
                            if opcion == "1":
                                print(f'Venta {Num_Venta }')
                                opc2 = True
                                while opc2 == True:
                                    while True:
                                        des = input("Descripcion del Articulo:")
                                        if des == '':
                                            print('La descripcion no puede estar vacia')
                                            continue
                                        break
                                    while True:
                                        try:
                                            piezas = int(input("Cantidad de piezas vendidas:"))
                                            if piezas < 1:
                                                print('Las piezas tiene que ser mayor a 0')
                                                continue
                                            break
                                        except:
                                            print('El valor ingresado no es un int')
                                            continue
                                        while True:
                                            try:
                                                precio = int(input("Precio de Venta:"))
                                                if precio < 1:
                                                    print('El precio tiene que ser mayor a 0')
                                                    continue
                                                break
                                            except:
                                                print('El valor ingresado no es un int')
                                                continue
                                            Articulo['Descripcion'] = des
                                            Articulo['Piezas'] = piezas
                                            Articulo['Precio'] = precio
                                            Venta.append(Articulo)
                                            Articulo = {}
                                            while True:
                                                opc3 = input("Hay mas Articulos? si/no:")
                                                if opc3 == "no":
                                                    opc2 = False
                                                    break
                                                elif opc3 == "si":
                                                    break
                                                else:
                                                    print("Esa no es una opcion valida")
                                                    continue
                                                for arti in Venta:
                                                    sub_Counter = arti['Precio'] * arti['Piezas']
                                                    Counter += sub_Counter
                                                    print(f'Counter de la Venta es ${Counter}')
                                                    Venta.append(Num_Venta )
                                                    Venta.append(Counter)
                                                    ID_Registro.append(Venta)
                                                    Venta = []
                                                    Num_Venta  += 1
                                                    Counter = 0
                                                    elif opcion == "2":
                                                        consulta = int(input('Numero de Venta: '))
                                                        w = 1
                                                        j = 1
                                                        try:
                                                            for arti in ID_Registro[consulta-1]:
                                                                if type(arti) != int:
                                                                    print(f'Articulo {w}')
                                                                    w += 1
                                                                    for key in arti:
                                                                        print(f'{key:12}: {arti[key]}')
                                                                        else:
                                                                            if j == 1:
                                                                                nom = 'Venta'
                                                                                print(f'{nom:12}: {arti}')
                                                                                j += 1
                                                                                else:
                                                                                    nom = 'Counter'
                                                                                    print(f'{nom:12}: {arti}')
                                                                                    w = 1
                                                                                    j = 1
                                                                                    except:
                                                                                        print("No existe ese numero de Venta")
                                                                                        opcion = input("[1] Registrar una Venta \t[2] Consultar una Venta \t[3] Salir: ")
                                                                                        with open('DataBaseStore.txt','w') as file:
                                                                                            if ID_Registro != []:
                                                                                                for vent in ID_Registro:
                                                                                                    for arti in vent:
                                                                                                        if type(arti) != int:
                                                                                                            for key in arti:
                                                                                                                file.write(f'{key}:{arti[key]}\n')
                                                                                                                else:
                                                                                                                    file.write(str(arti)+'\n')
                                                                                                                    file.write('\n') 


