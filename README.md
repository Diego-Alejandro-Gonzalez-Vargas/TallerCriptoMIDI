
# Ocultar y Desvelar Mensajes en Archivos MIDI

Este programa permite ocultar mensajes de texto dentro de archivos MIDI y luego recuperarlos. Utiliza eventos de cambio de programa en las pistas MIDI para codificar y decodificar los mensajes.

## Requisitos

Para usar este programa, necesitas Python 3 y la biblioteca `mido`. Puedes instalar `mido` usando pip:

```bash
pip install mido
```

## Uso

El programa ofrece un menú interactivo con tres opciones:

1. **Ocultar mensaje en archivo MIDI**: Permite introducir un mensaje de texto y ocultarlo dentro de un archivo MIDI especificado por el usuario.
2. **Desocultar mensaje de archivo MIDI**: Recupera y muestra un mensaje de texto previamente ocultado en un archivo MIDI.
3. **Salir**: Cierra el programa.

### Ocultar un Mensaje

1. Ejecuta el programa. Se te presentará el menú principal.
2. Selecciona la opción 1 (`Ocultar mensaje en archivo MIDI`).
3. Introduce el path relativo del archivo MIDI en el que deseas ocultar el mensaje.
4. Introduce el mensaje que quieres ocultar. Asegúrate de que el mensaje no supere el número máximo de caracteres permitidos, que se calcula en base a la cantidad de eventos de cambio de programa en el archivo MIDI.
5. El programa modificará el archivo MIDI y guardará la versión modificada con el mensaje oculto.

### Desocultar un Mensaje

1. Desde el menú principal, selecciona la opción 2 (`Desocultar mensaje de archivo MIDI`).
2. Introduce el path relativo del archivo MIDI del que deseas recuperar el mensaje.
3. El programa analizará el archivo, recuperará el mensaje oculto y lo mostrará en pantalla.

### Salir del Programa

- Selecciona la opción 3 para salir del programa.

## Notas Adicionales

- El programa utiliza la conversión de caracteres a números y viceversa para codificar y decodificar mensajes. Solo se deben usar caracteres que puedan ser convertidos de esta manera (principalmente letras y números).
- Asegúrate de que el archivo MIDI de destino tiene suficientes eventos de cambio de programa para alojar tu mensaje.
