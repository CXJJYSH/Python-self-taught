from random import shuffle

class Card:
    suits=["spates","hearts","diamonds","clubs"]
    values=[None,None,"2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    
    def __init__(self,v,s):
        """value和suit的值都为整型数"""
        self.value=v
        self.suit=s

    def __lt__(self,c2):
        if self.value<c2.value:
            return True
        if self.value==c2.value:
            if self.suit<c2.value:
                return True
            else:
                return False
        return False

    def __gt__(self,c2):
        if self.value>c2.value:
            return True
        if self.value==c2.value:
            if self.suit>c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v=self.values[self.value]+" of "+self.suits[self.suit]#4#现在知道了，字符串“... of ...”实在这里实现打印的。并且要注意" of "这里其实是“空格”+“of”+“空格”哦。
        return v

class Deck:
    def __init__(self):
        
        self.cards=[]

        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))#这里并没有实现打印“... of ...”的字符串，要留意一下实在哪里实现的这个功能。
                
        shuffle(self.cards)
    def rm_cards(self):
        if len(self.cards)==0:
            return
        return self.cards.pop()#3

class Player:
    def __init__(self,name):
        self.wins=0
        self.card=None
        self.name=name

class Game:
    def __init__(self):
        name1=input("p1 name")
        name2=input("p2 name")
        self.deck=Deck()
        self.p1=Player(name1)
        self.p2=Player(name2)

    def winner(self,p1,p2):
        if p1.wins>p2.wins:
            return p1.name
        if p1.wins<p2.wins:
            return p2.name
        return "It was a tie!"

    def wins(self,winner):
        w="{} wins this round"
        w=w.format(winner)
        print(w)

    def draw(self,p1n,p1c,p2n,p2c):
        d="{} drew {} {}drew {}"
        d=d.format(p1n,p1c,p2n,p2c)#1（Debug进程）
        print(d)

    def play_game(self):
        cards=self.deck.cards
        print("Beginning War!")
        while len(cards)>=2:
            m="q to quit. Any "+"key to play:"
            response=input(m)
            if response=="q":
                break
            p1c=self.deck.rm_cards()#2
            p2c=self.deck.rm_cards()
            p1n=self.p1.name
            p2n=self.p2.name
            self.draw(p1n,p1c,p2n,p2c)
            if p1c>p2c:
                self.p1.wins+=1
                self.wins(self.p1.name)
            else:
                self.p2.wins+=1
                self.wins(self.p2.name)
        win=self.winner(self.p1,self.p2)
        times=0
        if self.p1.wins>self.p2.wins:
            times=self.p1.wins
        else:
            times=self.p2.wins
        print("War is over.{} wins.{} wins for {} rounds.If it was a tie,you can neglect the former sentence.".format(win,win,times))


game=Game()
game.play_game()
