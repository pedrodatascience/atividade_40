from modulo import *

if __name__ == "__main__":
    #instancia objeto da subclasse
    h = Filho('','','','',0.0,0.0,'')
     
    #entrada dos dados
    h.nome = input('Infome o nome: ')
    h.email = input('Infome o email: ')
    h.profissao = input('Infome a profissão: ')
    h.olhos = input('Infome a cor dos olhos: ')
    h.peso = float(input('Infome o peso: ')).replace(',', '.')
    h.altura = float(input('Infome a altura: ')).replace(',','.')
    h.cabelo = input('Infome a cor do cabelo: ')

    #saída de dados
    h.exibir_cartao_visitas()
    h.exibir_fisico()