class Carro:
    def __init__(self, modelo, cor, valor, ano):
        """
        Inicializa um novo objeto Carro com os atributos fornecidos.
        
        :param modelo: Modelo do carro
        :param cor: Cor do carro
        :param valor: Valor do carro
        :param ano: Ano de fabricação do carro
        """
        self.modelo = modelo  # Linha 3: Criação do atributo modelo
        self.cor = cor        # Linha 4: Criação do atributo cor
        self.valor = valor    # Linha 5: Criação do atributo valor
        self.ano = ano        # Linha 6: Criação do atributo ano

    def calcular_valor_com_desconto(self, percentual_desconto):
        """
        Calcula o valor do carro com um desconto aplicado.
        
        :param percentual_desconto: Percentual de desconto a ser aplicado (em porcentagem)
        :return: Valor do carro após o desconto
        """
        desconto = self.valor * (percentual_desconto / 100)  # Linha 9: Calcula o valor do desconto
        valor_com_desconto = self.valor - desconto  # Linha 10: Calcula o valor com desconto
        return valor_com_desconto  # Linha 11: Retorna o valor com desconto

    def calcular_valor_parcelado(self, numero_de_parcelas):
        """
        Calcula o valor de cada parcela do carro, dado o número de parcelas.
        
        :param numero_de_parcelas: Número de parcelas em que o valor total será dividido
        :return: Valor de cada parcela
        """
        if numero_de_parcelas <= 0:
            raise ValueError("O número de parcelas deve ser maior que zero.")  # Linha 15: Levanta uma exceção se o número de parcelas for inválido
        valor_parcelado = self.valor / numero_de_parcelas  # Linha 16: Calcula o valor de cada parcela
        return valor_parcelado  # Linha 17: Retorna o valor de cada parcela

# Criação de 3 objetos da classe Carro
carro1 = Carro(modelo="Fusca", cor="azul", valor=20000, ano=2020)  # Linha 20: Criação do objeto carro1
carro2 = Carro(modelo="Civic", cor="preto", valor=60000, ano=2022)  # Linha 21: Criação do objeto carro2
carro3 = Carro(modelo="Onix", cor="branco", valor=30000, ano=2021)  # Linha 22: Criação do objeto carro3

# Utilização dos objetos criados
# Calcular e exibir o valor com desconto para carro1
valor_com_desconto_c1 = carro1.calcular_valor_com_desconto(10)  # Linha 25: Calcula o valor com 10% de desconto para carro1
print(f"Valor com 10% de desconto para {carro1.modelo}: R${valor_com_desconto_c1:.2f}")  # Linha 26: Exibe o valor com desconto para carro1

# Calcular e exibir o valor parcelado para carro2 em 12 vezes
valor_parcelado_c2 = carro2.calcular_valor_parcelado(12)  # Linha 28: Calcula o valor parcelado para carro2
print(f"Valor de cada parcela em 12 vezes para {carro2.modelo}: R${valor_parcelado_c2:.2f}")  # Linha 29: Exibe o valor de cada parcela para carro2

# Calcular e exibir o valor com desconto para carro3
valor_com_desconto_c3 = carro3.calcular_valor_com_desconto(15)  # Linha 31: Calcula o valor com 15% de desconto para carro3
print(f"Valor com 15% de desconto para {carro3.modelo}: R${valor_com_desconto_c3:.2f}")  # Linha 32: Exibe o valor com desconto para carro3
