def monitorear_motor_dc():
    # Definición de variables iniciales y umbrales
    umbral_bajo = 500
    umbral_alto = 3000
    
    rpm = None
    estado = ""
    rpm_prev = None
    contador_vibracion = 0
    contador_mediciones = 0

    ejecutando = True

    while ejecutando:
        print("\n=== MENÚ DEL PROGRAMA ===")
        print("1. Registrar RPM del motor")
        print("2. Clasificar estado del motor")
        print("3. Detectar vibración anómala")
        print("4. Salir y generar reporte final")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            try:
                rpm_ingresada = float(input("Ingrese las RPM del motor (0 - 10000): "))
            except ValueError:
                print("Error: rpm debe ser numérica.")
                continue

            # Validación del rango permitidos: 0 <= rpm <= 10000
            if rpm_ingresada < 0 or rpm_ingresada > 10000:
                print("Error: Las RPM deben estar entre 0 y 10000.")
            else:
                rpm = rpm_ingresada
                contador_mediciones += 1

                # Clasificación automática del estado del motor
                if rpm < umbral_bajo:
                    estado = "bajo"
                elif rpm <= umbral_alto:
                    estado = "normal"
                else:
                    estado = "alto"

                # Detección de variaciones bruscas (vibración anómala: diferencia > 500 RPM)
                if rpm_prev is not None:
                    diferencia = abs(rpm - rpm_prev)
                    if diferencia > 500:
                        contador_vibracion += 1
                        print("⚠️ ALERTA: Cambio brusco de RPM detectado (Posible vibración anómala).")

                # Actualización de la última RPM registrada
                rpm_prev = rpm

                # Salida esperada para cada medición
                print(f"\n✓ Lectura #{contador_mediciones} registrada correctamente:")
                print(f"  • RPM: {rpm}")
                print(f"  • Estado: {estado}")

        elif opcion == "2":
            if rpm is None:
                print("Aún no se ha registrado ninguna lectura de RPM.")
            else:
                print(f"\n[Último estado clasificado: {estado} (RPM actuales: {rpm})]")

        elif opcion == "3":
            print(f"\n[Detecciones de vibración anómala acumuladas: {contador_vibracion}]")

        elif opcion == "4":
            ejecutando = False

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

    # --- Salida Final ---
    print("\n" + "="*40)
    print("            REPORTE FINAL")
    print("="*40)
    print(f"• Total de mediciones realizadas: {contador_mediciones}")
    print(f"• Vibraciones anómalas detectadas (contador_vibracion): {contador_vibracion}")
    
    # Mensaje según el valor de contador_vibracion
    if contador_vibracion > 0:
        print("• Mensaje: Se detectan posibles vibraciones anómalas, revisar motor")
    else:
        print("• Mensaje: Motor operando de forma estable")


# Llamada a la función
monitorear_motor_dc()