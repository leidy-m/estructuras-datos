class Instrumento:
   def __init__(self, precio):
       self.precio = precio
       self.nombre = ""


   def tocar(self):
       print("Estamos tocando el instrumento")


   def vender(self):
       print(self.nombre, "vendido!")


class Bateria(Instrumento):
   def __init__(self, precio):
       super().__init__(precio)
       self.nombre = "Bateria"


class Guitarra(Instrumento):
   def __init__(self, precio):
       super().__init__(precio)
       self.nombre = "Guitarra"


instrumento1 = Bateria(400000)
instrumento1.vender()



