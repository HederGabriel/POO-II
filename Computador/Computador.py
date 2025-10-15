class Computador:
    def __init__(self, cpu, ram, tela, hd):
        self.cpu = cpu
        self.ram = ram
        self.tela = tela
        self.hd = hd

    def ligar(self):
        print("Computador foi ligado.")

    def desligar(self):
        print("Computador está sendo desligado.")


class Notebook(Computador):
    def __init__(self, cpu, ram, tela, hd, bateria, wifi):
        super().__init__(cpu, ram, tela, hd)
        self.bateria = bateria
        self.wifi = wifi
        self.usoCPU = 0
        self.usoRAM = 0

    def ligar(self):
        super().ligar()
        self.usoCPU += 15
        self.usoRAM += 30
        print(f"Notebook ligado. Uso de CPU: {self.usoCPU}%, Uso de RAM: {self.usoRAM}%.")

    def desligar(self):
        self.usoCPU = 0
        self.usoRAM = 0
        super().desligar()
        print("Notebook desligado. Uso de CPU e RAM zerados.")


class Desktop(Computador):
    def __init__(self, cpu, ram, tela, hd, gpu):
        super().__init__(cpu, ram, tela, hd)
        self.gpu = gpu
        self.usoCPU = 0
        self.usoRAM = 0
        self.usoGPU = 0

    def ligar(self):
        super().ligar()
        self.usoCPU += 20
        self.usoRAM += 20
        self.usoGPU += 10
        print(f"Desktop ligado. Uso de CPU: {self.usoCPU}%, RAM: {self.usoRAM}%, GPU: {self.usoGPU}%.")

    def desligar(self):
        self.usoCPU = 0
        self.usoRAM = 0
        self.usoGPU = 0
        super().desligar()
        print("Desktop desligado. Uso de CPU, RAM e GPU zerados.")


if __name__ == "__main__":
    notebook = Notebook(cpu="Core i5", ram="8GB", tela="15 polegadas", hd="1TB", bateria="60W", wifi="802.11ac")

    desktop = Desktop(cpu="Core i7", ram="16GB", tela="22 polegadas", hd="500GB", gpu="NVidia RTX 2080")

    print("\n--- Ligando o Notebook ---")
    notebook.ligar()

    print("\n--- Ligando o Desktop ---")
    desktop.ligar()

    print("\n--- Desligando o Notebook ---")
    notebook.desligar()

    print("\n--- Desligando o Desktop ---")
    desktop.desligar()
