from normal import Normal
from vip import VIP
from camarote_inferior import CamaroteInferior
from camarote_superior import CamaroteSuperior

def main():
    ingresso_normal = Normal(50)
    ingresso_normal.imprimeValor()
    ingresso_normal.imprimeTipo()

    ingresso_vip = VIP(50, 30)
    print(f"Valor do ingresso VIP: R${ingresso_vip.valorVIP():.2f}")

    camarote_inferior = CamaroteInferior(50, 30, "Setor A - Frente do palco")
    camarote_inferior.imprimeLocalizacao()
    print(f"Valor do Camarote Inferior: R${camarote_inferior.valorVIP():.2f}")

    camarote_superior = CamaroteSuperior(50, 30, 20)
    print(f"Valor do Camarote Superior: R${camarote_superior.valorCamaroteSuperior():.2f}")

if __name__ == "__main__":
    main()
