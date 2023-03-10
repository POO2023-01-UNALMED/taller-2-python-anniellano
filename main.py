class Auto:
    #Atributos de clase
    cantidadCreados = 0
    #Constructor
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        #Atributos
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    #Métodos
    def cantidadAsientos(self):
        cont = 0

        for i in self.asientos:
            #comprobamos si es una instancia
            if isinstance(i, Asiento) == True:
                cont += 1
            
        return cont

    def verificarIntegridad(self):
        for puesto in self.asientos:
            if puesto != None and puesto.registro != self.registro:
                return "Las piezas no son originales"
        if self.motor.registro != self.registro: 
            return "Las piezas no son originales"
        
        return "Auto original"


class Asiento: 
    #constructor
    def __init__(self, color, precio, registro):
        #Atributos
        self.color = color
        self.precio = precio
        self.registro = registro
    
    #metodos
    def cambiarColor(self, color):
        permitidos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in permitidos:
            #print("ha cambiado el color a",color)
            self.color = color


class Motor:
    #Constructor
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    #metodos
    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        permitidos = ["electrico", "gasolina"]
        if tipo in permitidos:
            #print("funciona c:")
            self.tipo = tipo


        
