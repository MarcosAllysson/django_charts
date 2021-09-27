from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class DadosJSONView(BaseLineChartView):
    def get_labels(self):
        """ Retorna 12 labels pra representação do X """
        labels =  [
            'Janeiro',
            'Fevereiro',
            'Março',
            'Abril',
            'Maio',
            'Junho',
            'Julho',
            'Agosto',
            'Setembro',
            'Outubro',
            'Novembro',
            'Dezembro'
        ]

        return labels

    def get_providers(self):
        """ Retorna os nomes dos datasets """
        datasets = [
            'Programação Para Leigos',
            'Algoritmos e lógico de programação',
            'Programação em C',
            'Programação em Java',
            'Programação em Python',
            'Banco de dados'
        ]

        return datasets

    def get_data(self):
        """
        Retorna 6 datasets para plotar o gráfico
        Cada linha de get_providers representa 1 dataset
        Cada coluna representa 1 label

        A quantidade de dados precisa ser igual aos datasets/labels
        12 labels, então 12 colunas
        6 datasets, então 6 linhas
        """

        dados = []

        for linha in range(6):
            for coluna in range(12):
                dado = [
                    randint(1, 200),  # jan
                    randint(1, 200),  # fev
                    randint(1, 200),  # mar
                    randint(1, 200),  # abr
                    randint(1, 200),  # mai
                    randint(1, 200),  # jun
                    randint(1, 200),  # jul
                    randint(1, 200),  # ago
                    randint(1, 200),  # set
                    randint(1, 200),  # out
                    randint(1, 200),  # nov
                    randint(1, 200)   # dez
                ]

            dados.append(dado)

        return dados

