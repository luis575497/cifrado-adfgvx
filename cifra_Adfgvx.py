import random

class CifraAdfgvx:
    
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, clave_alfabeto):
        self.clave_alfabeto = clave_alfabeto
    
    def cifrar(self, mensaje, clave_mensaje):
        matriz = self.crear_matriz(self.clave_alfabeto)
        mensaje_sutituido = self.__sustitucionMensaje(matriz,mensaje)
        criptograma = self.__trasponerMensaje(clave_mensaje,mensaje_sutituido,0)
        return criptograma
    
    def descifrar(self, criptograma, clave_mesaje):
        matriz = self.crear_matriz(self.clave_alfabeto)
        trasposicion = self.__trasponerMensaje(clave_mesaje,criptograma,1)
        mensaje = self.__sustCripto(matriz,trasposicion)
        return mensaje

    def crear_matriz(self,clave):
        alfabeto = [x for x in self.alfabeto]
        clave = [x.upper() for x in clave if x.upper() in self.alfabeto]
        num = [x for x in "0123456789"]
        alfabeto_nuevo = []

        # Crear un alfabeto con letras, la clave y los numeros
        alfa_completo = list(clave + alfabeto + num)
        
        # Desordenar la lista de letras siempre de la misma manera
        random.Random(3).shuffle(alfa_completo)
        
        # Eliminar duplicados del alfabeto
        for letra in alfa_completo:
            if letra not in alfabeto_nuevo:
                alfabeto_nuevo.append(letra)
        
        # Crear la matriz de 6x6
        matriz = [[],[],[],[],[],[]]
        for pos,letra in enumerate(alfabeto_nuevo):
            matriz[pos % 6].append(letra)
        
        return matriz
    
    def __sustitucionMensaje(self, matriz, mensaje):
        # indices de letras
        index = [x for x in "ADFGVX"]

        # limpiar mensaje
        mensaje = mensaje.replace(" ","")        
        criptograma = []

        # buscar la fila y columa de cada letra y relacionar con el index
        for letra in mensaje:
            letra = letra.upper()
            digrama = ""
            for pos,linea in enumerate(matriz):
                if letra in linea:
                    pos_letra = linea.index(letra)
                    digrama += index[pos_letra]
                    digrama += index[pos]
            
            criptograma.append(digrama)

        return "".join(criptograma)

    def __trasponerMensaje(self,clave,criptograma,mode):
        clave_limpia = []
        
        for letra in clave:
            if letra.upper() not in clave_limpia:
                clave_limpia.append(letra.upper())

        clave_ordenada = sorted(clave_limpia)
        trasposicion_columnar = [[] for x in range(len(clave_limpia))]

        # Completar las columnas para que tengan el mismo largo 
        if len(criptograma) % len(clave_limpia) != 0:
            add = int(len(clave_limpia) - ((len(criptograma) % len(clave_limpia))))
            for _ in range(add):
                criptograma += "X"

        trasposicion = []

        if mode == 0:
            # ordenar el mensaje por columnas
            for pos,letra in enumerate(criptograma):
                trasposicion_columnar[pos % len(clave_limpia)].append(letra)

            # Ordenar las columnas segun la clave ordenada
            for letra in clave_ordenada:
                index = clave_limpia.index(letra)
                columna = ''.join(trasposicion_columnar[index])
                trasposicion.append(columna)

        if mode == 1:
            criptograma = [letra for letra in criptograma]
            size = int(len(criptograma) / len(clave_limpia))
            matriz_desordenada = [criptograma[i:i+size] for i in range(0,len(criptograma),size)]
            
            # Ordenar la matriz
            matriz_ordenada = []
            for letra in clave_limpia:
                index = clave_ordenada.index(letra)
                matriz_ordenada.append(matriz_desordenada[index])

            for columna in range(len(matriz_ordenada[0])):
                for fila in matriz_ordenada:
                    trasposicion.append(fila[columna])
                    
        return "".join(trasposicion)
        
    def __sustCripto(self,matriz,mensaje):
        cifrado = 'ADFGVX'
        pos_matriz = [cifrado.index(x) for x in mensaje]
        coordenadas = [pos_matriz[i:i+2] for i in range(0,len(pos_matriz),2)]
        mensaje_claro = []
        for coord in coordenadas:
            try:
                mensaje_claro.append(matriz[coord[1]][coord[0]])
            except:
                mensaje_claro.append(" ")

        return ''.join(mensaje_claro)
    
    def generar_clave(self,size):
        clave = ""
        for _ in range(size):
            pos = random.randint(0,25)
            clave += self.alfabeto[pos]
        return clave