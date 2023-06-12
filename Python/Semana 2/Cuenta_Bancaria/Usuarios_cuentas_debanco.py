class CuentaBancaria:
    todas_las_cuentas = []
    
    def __init__(self, tasa_int, balance):
        self.tasa_int = tasa_int
        self.balance = balance
        self.__class__.todas_las_cuentas.append(self)

    def deposito(self, amount):
        self.balance += amount
        return self
    
    def retiro(self, amount):
        if self.puede_retirar(amount):
            self.balance -= amount
        else:
            print("Fondos insuficientes: se le recarga $5 de impuestos")
            self.balance -=5
        return self

    def puede_retirar(self, amount):
        return self.balance >= amount

    def mostrar_info_cuenta(self):
        print(f'Balance: ${self.balance}, Tasa de interés: {self.tasa_int*100}%')
        return self
    

class Usuario:
    
    def __init__(self, name):
        self.name = name
        self.cuentas = {
            "vista":CuentaBancaria(.02, 1000),
            "ahorro": CuentaBancaria(.05, 3000)
        }

    def crear_cuenta(self, nombre_cuenta, tasa_int, balance):
        self.cuentas[nombre_cuenta] = CuentaBancaria(tasa_int, balance)
        return self

    def deposito(self, nombre_cuenta, amount):
        if nombre_cuenta in self.cuentas:
            self.cuentas[nombre_cuenta].deposito(amount)
        else:
            print(f'La cuenta {nombre_cuenta} no existe.')
        return self
    
    def retiro(self, nombre_cuenta, amount):
        if nombre_cuenta in self.cuentas:
            self.cuentas[nombre_cuenta].retiro(amount)
        else:
            print(f'La cuenta {nombre_cuenta} no existe.')
        return self
    
    def mostrar_info_cuenta(self):
        for cuenta, detalles in self.cuentas.items():
            print(f"Usuario: {self.name}, Cuenta: {cuenta},")
            detalles.mostrar_info_cuenta()
        return self
    
    def transferir(self, origen, destino, amount):
        if origen in self.cuentas and destino in self.cuentas:
            if self.cuentas[origen].puede_retirar(amount):
                self.cuentas[origen].retiro(amount)
                self.cuentas[destino].deposito(amount)
            else:
                print("Transferencia fallida, saldo insuficiente.")
        else:
            print('Una o ambas cuentas no existen.')
        return self

lorena = Usuario("Lorena")
lorena.crear_cuenta("inversiones", .07, 5000)

lorena.crear_cuenta('vista', .03, 0)
lorena.deposito('vista', 8000)
lorena.transferir('inversiones','vista',6000)
lorena.mostrar_info_cuenta()