class Descuento:
    def aplicar(self, precio):
        return precio


class DescuentoEstudiante(Descuento):
    def aplicar(self, precio):
        return precio * 0.90


class DescuentoJubilado(Descuento):
    def aplicar(self, precio):
        return precio * 0.80


class Compra:
    def __init__(self, precio, estrategia):
        self.precio = precio
        self.estrategia = estrategia

    def total(self):
        return self.estrategia.aplicar(self.precio)


compra = Compra(10000, DescuentoEstudiante())

print(compra.total())