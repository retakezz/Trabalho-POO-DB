class Cavaleiro:
    def __init__(self, nome, defesa, arma, vida, ataque):
        self.nome = nome
        self.defesa = defesa
        self.arma = arma
        self.vida = vida
        self.ataque = ataque

    def atacar(self, alvo):
        print('o', self.nome, 'ataca', alvo, 'com', self.ataque)
    def defender(self, inimigo):
        print('o', self.nome, 'defende ataque do', inimigo, 'com', self.defesa)
    def equipar(self):
        print('o', self.nome, 'equipa', self.arma)
    def recuparar(self):
        print('o', self.nome, 'se recupera')

    def salvar(self, cursor, conexao):
        sql = 'INSERT INTO personagens (nome, defesa, arma, vida, ataque, classe) VALUES (%s, %s, %s, %s, %s, %s)'
        valores = (self.nome, self.defesa, self.arma, self.vida, self.ataque, 'Cavaleiro')
        cursor.execute(sql, valores)
        conexao.commit()