###############
# Bibliotecas #
###############

import scrapy


####################
# Inicio do codigo #
####################

class ImdbSpider(scrapy.Spider):
    start_urls = ['https://www.cbf.com.br/futebol-brasileiro?csrt=8376204594349034325']

    def parse(self, response):
        for timesa in response.css('td:nth-child(1)'):
            yield{
                "Classificacao": timesa.css('b.m-l-10::text').get(),
                " nome do time": timesa.css('span.hidden-xs::text').get()[:-4],
                " estado do time": timesa.css('span.hidden-xs::text').get()[-2:]
            }
#################
# Fim do codigo #
#################


# for nome in nomesdostimes:
#   print(nome[:-5])    NOME DOS TIMES SEM ESTADO
#   print(nome[-2:])    ESTADO SEM O NOME DOS TIMES
