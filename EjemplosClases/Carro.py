class Carro:
   def __init__(self, marca, modelo, velocidad_maxima):
       self.marca = marca
       self.modelo = modelo
       self.velocidad_maxima = velocidad_maxima
       self.velocidad_actual = 0


   def acelerar(self):
       self.velocidad_actual = min(self.velocidad_actual + 10, self.velocidad_maxima)
       print(f"{self.marca} {self.modelo} acelerando a {self.velocidad_actual} km/h")


   def frenar(self):
       self.velocidad_actual = max(self.velocidad_actual - 10, 0)
       print(f"{self.marca} {self.modelo} frenando a {self.velocidad_actual} km/h")


class CarroDeportivo(Carro):
   def __init__(self, marca, modelo, velocidad_maxima):
       super().__init__(marca, modelo, velocidad_maxima)


   def turbo(self):
       self.velocidad_actual = min(self.velocidad_actual + 50, self.velocidad_maxima)
       print(f"{self.marca} {self.modelo} activó el turbo a {self.velocidad_actual} km/h")


mi_carro = CarroDeportivo("Ferrari", "F8", 300)
mi_carro.acelerar()
mi_carro.turbo()
mi_carro.frenar()


