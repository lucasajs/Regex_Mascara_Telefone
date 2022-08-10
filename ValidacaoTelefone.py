import re


class ValidacaoTelefone:
    def __init__(self, telefone):
        if self.validacaoTelefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("numero incorreto! digite um número valido")

    def __str__(self):
        return self.MascaraNumero()


    def validacaoTelefone(self, telefone):
        padrao= "[0-9]{2}[0-9]{4,5}[0-9]{4}"
        resposta= re.search(padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def MascaraNumero(self):
        padrao= padrao= "([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta= re.search(padrao, self.numero)
        numero_formatado= (f'({resposta.group(1)}){resposta.group(2)}-{resposta.group(3)}')
        return numero_formatado