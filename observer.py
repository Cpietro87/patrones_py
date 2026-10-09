
class Observador:
    def actualizar(self, medicamento, stock):
        raise NotImplementedError


class Administrador(Observador):
    def actualizar(self, medicamento, stock):
        print(
            f"Administrador: stock de {medicamento}: {stock}"
        )

class Compras(Observador):
    def actualizar(self, medicamento, stock):
        if stock <= 5:
            print(
                f"Compras: solicitar reposición de {medicamento}"
            )

class StockMedicamento:
    def __init__(self, medicamento, stock):
        self.medicamento = medicamento
        self.stock = stock
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def quitar_observador(self, observador):
        self.observadores.remove(observador)

    def notificar(self):
        for observador in self.observadores:
            observador.actualizar(
                self.medicamento,
                self.stock
            )

    def cambiar_stock(self, nuevo_stock):
        self.stock = nuevo_stock
        self.notificar()

stock = StockMedicamento("Paracetamol", 20)

administrador = Administrador()
compras = Compras()

stock.agregar_observador(administrador)
stock.agregar_observador(compras)

stock.cambiar_stock(10)
print("----------")
stock.cambiar_stock(3)