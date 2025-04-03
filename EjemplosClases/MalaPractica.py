class Carro:
   def __init__(self, marca, modelo, velocidad_maxima):
       self.marca = marca
       self.modelo = modelo
       self.velocidad_maxima = velocidad_maxima
       self.velocidad_actual = 0

   def acelerar(self):
       if self.velocidad_actual + 10 <= self.velocidad_maxima:
           self.velocidad_actual += 10
       else:
           self.velocidad_actual = self.velocidad_maxima
       print(f"{self.marca} {self.modelo} acelerando a {self.velocidad_actual} km/h")


   def frenar(self):
       if self.velocidad_actual - 10 >= 0:
           self.velocidad_actual -= 10
       else:
           self.velocidad_actual = 0
       print(f"{self.marca} {self.modelo} frenando a {self.velocidad_actual} km/h")


def turbo(carro):
   carro.velocidad_actual += 50
   if carro.velocidad_actual > carro.velocidad_maxima:
       carro.velocidad_actual = carro.velocidad_maxima
   print(f"{carro.marca} {carro.modelo} usando turbo a {carro.velocidad_actual} km/h")


mi_carro = Carro("Toyota", "Corolla", 180)
mi_carro.acelerar()
turbo(mi_carro)
mi_carro.frenar()


