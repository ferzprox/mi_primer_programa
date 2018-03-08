model_to_guess = "Intel Core i7 6700K 4.2"

user_model = str(input("¿Cual era el antiguo procesador de nate?"))

if model_to_guess == user_model:
    print("Has ganado el dragon de msi")
else:
    user_model = str(input("Prueba de nuevo, te quedan 4 intentos restantes!!"))

    if model_to_guess == user_model:
        print("Has ganado el dragon de msi")
    else:
        user_model = str(input("Prueba de nuevo, te quedan 3 intentos restantes!!"))

        if model_to_guess == user_model:
            print("Has ganado el dragon de msi")
        else:
            user_model = str(input("Prueba de nuevo, te quedan 2 intentos restantes!!"))

            if model_to_guess == user_model:
                print("Has ganado el dragon de msi")
            else:
                user_model = str(input("Prueba de nuevo, te quedan 1 intentos restantes!!"))

                if model_to_guess == user_model:
                    print("Has ganado el dragon de msi")
                else:
                    user_model = str(input("Mira que eres subnormal, como no vas a saber su puto procesador"))
