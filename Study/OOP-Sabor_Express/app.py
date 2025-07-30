from modelos.restaurante import Restaurante

restaurante_abbraccio = Restaurante('abbraccio', 'Italiana')
restaurante_abbraccio.receber_avaliacao('Gui', 5)
restaurante_abbraccio.receber_avaliacao('Lê', 4.5)
restaurante_abbraccio.receber_avaliacao('Monica', 3.5)

def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()