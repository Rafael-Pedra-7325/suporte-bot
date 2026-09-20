import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from chatbot import SuporteBot


class SuporteBotTestCase(unittest.TestCase):
    def setUp(self):
        self.bot = SuporteBot()

    def test_reconhece_saudacao(self):
        _, intencao = self.bot.responder("Oi, bom dia!")
        self.assertEqual(intencao, "saudacao")

    def test_reconhece_horario(self):
        _, intencao = self.bot.responder("Qual o horário de funcionamento?")
        self.assertEqual(intencao, "horario_funcionamento")

    def test_reconhece_reclamacao(self):
        _, intencao = self.bot.responder("Estou com um problema no sistema, deu erro")
        self.assertEqual(intencao, "reclamacao")

    def test_mensagem_nao_reconhecida_usa_fallback(self):
        _, intencao = self.bot.responder("xablau flerdo blim")
        self.assertEqual(intencao, "fallback")

    def test_historico_registra_conversas(self):
        self.bot.responder("oi")
        self.bot.responder("qual o preço?")
        self.assertEqual(len(self.bot.historico), 2)
        self.assertEqual(self.bot.historico[1]["intencao"], "preco")


if __name__ == "__main__":
    unittest.main()
