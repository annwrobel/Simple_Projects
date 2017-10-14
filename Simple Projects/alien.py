class Player(object):
    def blast(self, enemy):
        print("Gracz razi wroga laserem.\n")
        enemy.die()

class Alien(object):
    def die(self):
         print("Umieram, żegnajcie")

#main
print("\t\tSmierc obcego\n")
hero = Player()
invader = Alien()
hero.blast(invader)
