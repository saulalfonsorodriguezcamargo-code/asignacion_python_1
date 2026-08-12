def evaluar_sensor():
    # Inicialización de variables requeridas
    activaciones = 0
    fallas = 0
    previo = None
    contador_consecutivos = 0
    
    ejecutando = True

    while ejecutando:
        print("\n=== Menú del Programa ===")
        print("1. Registrar lecturas digitales (0 o 1)")
        print("2. Contar activaciones del sensor")
        print("3. Detectar fallas en la señal")
        print("4. Salir y mostrar reporte")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            try:
                lectura = int(input("Ingrese el valor del sensor (0 o 1): "))
            except ValueError:
                print("Error: Debe ingresar un valor numérico.")
                continue

            # Validación: lectura solo puede ser 0 o 1
            if lectura != 0 and lectura != 1:
                print("Valor inválido. Solo se permite ingresar 0 o 1.")
            else:
                # Contar activaciones e incrementar o reiniciar consecutivos
                if lectura == 1:
                    activaciones += 1
                    contador_consecutivos += 1
                else:
                    contador_consecutivos = 0

                # Validación de falla: si contador_consecutivos > 5
                if contador_consecutivos > 5:
                    fallas += 1
                    print("⚠️ ALERTA: Patrón anómalo detectado (Ruido / Falla en la señal).")

                previo = lectura
                print("✓ Lectura registrada correctamente.")

        elif opcion == "2":
            print(f"\n[Activaciones registradas hasta el momento: {activaciones}]")

        elif opcion == "3":
            print(f"\n[Fallas detectadas hasta el momento: {fallas}]")

        elif opcion == "4":
            ejecutando = False
            
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

    # --- Salida Esperada ---
    print("\n" + "="*30)
    print("      REPORTE FINAL")
    print("="*30)
    print(f"• Número total de activaciones: {activaciones}")
    print(f"• Número de fallas detectadas: {fallas}")
    print("• Estado del sensor:")
    
    if fallas == 0:
        print("  -> Sensor operando correctamente")
    else:
        print("  -> Sensor presenta ruido o fallas en la señal")


# Llamada a la función principal
evaluar_sensor()