class Mago:
    def __init__(self, nome, defesa, elemento, vida, ataque):
        self.nome = nome
        self.defesa = defesa
        self.elemento = elemento
        self.vida = vida
        self.ataque = ataque

    def atacar(self, alvo):
        print('o', self.nome, 'ataca', alvo, 'com', self.ataque)
    def defender(self, inimigo):
        print('o', self.nome, 'defende ataque do', inimigo, 'com', self.defesa)
    def conjurar(self):
        print('o', self.nome, 'conjura', self.elemento)
    def recuperar(self):
        print('o', self.nome, 'se recupera')

    def salvar(self, cursor, conexao):
        sql = 'INSERT INTO personagens (nome, defesa, elemento, vida, ataque, classe) VALUES (%s, %s, %s, %s, %s, %s)'
        valores = (self.nome, self.defesa, self.elemento, self.vida, self.ataque, 'Mago')
        cursor.execute(sql, valores)
        conexao.commit()