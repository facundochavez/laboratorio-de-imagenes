# Laboratorio de imágenes

Aplicativo web interactivo que resuelve los **Trabajos Prácticos 1 y 2** de la optativa *Procesamiento de Imágenes* de la Diplomatura en Ciencia de Datos (Diplodatos 2026).

**Grupo 2:** [Chavez Facundo](https://www.facundochavez.dev/es), [Droz Mariano Rafael](https://www.linkedin.com/in/marianodroz/)

## Ejercicios

| Ejercicio | Tema | |
|---|---|---|
| 1.1 | Luminancia y saturación en YIQ | |
| 1.2 | Manipulación del histograma de luminancias (raíz, cuadrado, lineal a trozos) | |
| 1.3 | Visualización de datos 2D con paletas | optativo |
| 1.4 | Aritmética de píxeles (RGB / YIQ, clampeada / promediada, if-lighter / if-darker) | optativo |
| 2.1 | Filtrado por convolución (pasabajos, Laplaciano, Sobel, pasabanda) | |
| 2.2 | Morfología en niveles de gris (erosión, dilatación, apertura, cierre, bordes, mediana, top-hat) | |
| 2.3 | Remuestreo ×2 y cuantización (uniforme, dithering aleatorio, difusión del error) | optativo |

Todos los algoritmos están **implementados a mano, píxel por píxel**, sin bibliotecas de procesamiento de imágenes, como pide la consigna. El navegador solo se usa para decodificar los archivos de imagen y pintar los píxeles resultantes. Cada pestaña muestra en vivo el código fuente de las funciones que se están ejecutando, con los parámetros elegidos.

## Uso

Abrir `dist/laboratorio-de-imagenes.html` en cualquier navegador moderno. Es un único archivo autocontenido: incluye las imágenes de prueba y funciona sin servidor. Con conexión a internet carga la tipografía Geist desde Google Fonts; sin conexión usa la fuente del sistema.

- Elegir una imagen en la barra lateral o cargar una propia con **Nueva imagen** (también se puede arrastrar sobre la página).
- **Aplicar** reemplaza la imagen de origen por el resultado, para encadenar procesos entre pestañas. El ícono de deshacer sobre la miniatura la restaura.
- **Descargar** guarda el resultado en PNG a resolución real.

## Estructura

```
src/app.html          código fuente del aplicativo (HTML, CSS y JS)
src/demo-images.js    imágenes de prueba embebidas en base64
build.py              arma el archivo final
dist/                 aplicativo listo para usar
```

## Desarrollo

Editar `src/app.html` y regenerar:

```
python build.py
```

## Créditos

Las imágenes de prueba son las de ejemplo que distribuyen `imageio` y `scikit-image`. La matriz RGB → YIQ, los kernels y las operaciones siguen las filminas de la cátedra (Claudio Delrieux, LCI – UNS – CONICET).
