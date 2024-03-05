"""
 * Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 * Desarrollado para el curso MSIN4101 - INGENIERIA CRIPTOGRAFICA
 *
 * 6 DE MARZO DE 2023 
 *
 * DESARROLLADO POR:
 *
 * DIEGO ALEJANDRO GONZALEZ VARGAS
 * COD: 202110240
 * MAIL: DA.GONZALEZV1@UNIANDES.EDU.CO
 *
"""

from mido import MidiFile, Message, MidiTrack
import mido
import sys
#OUTPUTMIDI.TICKS_PER_BEAT

# Función para convertir los números de programa a letras
def numeros_a_letras(numeros):
    mensaje = ""
    for numero in range(0, len(numeros), 2):
        letra = chr(numeros[numero])
        mensaje += letra
    return mensaje

def count_program_change_events(popo):
    program_change_events = 0
    for msg in popo:
        # Verifica si el mensaje es un evento de cambio de programa
        if msg.type == 'program_change':
            program_change_events+=1
    return program_change_events


def letras_a_numeros(texto):
    resultado = []
    for letra in texto:
        if letra.isalpha():  # Verifica si es una letra
            numero = ord(letra.lower())  # Calcula el número basado en el orden alfabético
            resultado.append(numero)
        else:
            numero = ord(letra.lower())
            resultado.append(numero)  # Si no es una letra, se añade tal cual al resultado
    return resultado  # Elimina el espacio en blanco extra al final, si lo hay

def ocultar_mensaje():
    # Solicitar al usuario que introduzca el path del archivo MIDI
    path_archivo_midi = input("Por favor, introduce el RELATIVE path del archivo MIDI: ")
    mid = MidiFile(path_archivo_midi)
    # Solicitar al usuario que introduzca el mensaje a ocultar
    mensaje = input("Por favor, introduce el mensaje que quieres ocultar[MAX "+str(count_program_change_events(mid)) +" CARACTERES] : ")
    centinela= 0
    msgOculto=mensaje
    listanum = letras_a_numeros(msgOculto)
    espaciosPaCompletar = letras_a_numeros("    ")
    outputFile = MidiFile()
    outputFile.ticks_per_beat = mid.ticks_per_beat
    for track in mid.tracks:
        outputTrack = MidiTrack()
        outputFile.tracks.append(outputTrack)
        print(outputTrack)
        for msg in track:
            if msg.type == 'program_change':
                if centinela < len(listanum):
                    outputTrack.append(Message('program_change', program=listanum[centinela], time=0))
                    centinela+=1
                else:
                    outputTrack.append(Message('program_change', program=espaciosPaCompletar[1], time=0))
                outputTrack.append(msg)
            else:
                outputTrack.append(msg)
    outputFile.save('mensajeOculto.mid')
    print("========================================================================================")
    print("*                                                                                      *")
    print("*   SU MENSAJE HA SIDO OCULTO DE MANERA EXITOSA EN EL ARCHIVO mensajeOculto.mid        *")
    print("*                                                                                      *")
    print("========================================================================================")


def desocultar_mensaje():
    # Solicitar al usuario que introduzca el path del archivo MIDI
    path_archivo_midi = input("Por favor, introduce el RELATIVE path del archivo MIDI: ")
    mid = MidiFile(path_archivo_midi)
    # Lista para almacenar los números de programa
    numeros_programa = []
    # Recorrer todas las pistas del archivo MIDI
    for track in mid.tracks:
        # Recorrer todos los mensajes de la pista
        for msg in track:
            # Si el mensaje es un mensaje de cambio de programa, obtener el número de programa
            if msg.type == 'program_change':
                numeros_programa.append(msg.program)
    # Convertir los números de programa a letras
    mensaje_oculto = numeros_a_letras(numeros_programa)
    # Mostrar el mensaje oculto
    print("Mensaje oculto encontrado:", mensaje_oculto)

def main():
    while True:
        print("========================================================================================")
        print("*                                                                                      *")
        print("*   BIENVENIDOS AL OCULTADOR DE MENSAJES EN ARCHIVOS MIDI MAS ESPECTACULAR DE TODOS    *")
        print("*             AUTOR: DIEGO ALEJANDRO GONZALEZ VARGAS - COD: 202110240                  *")
        print("*                                                                                      *")
        print("========================================================================================")
        print("\nMenú:")
        print("1. Ocultar mensaje en archivo MIDI")
        print("2. Desocultar mensaje de archivo MIDI")
        print("3. Salir")
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            ocultar_mensaje()
        elif opcion == "2":
            desocultar_mensaje()
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()