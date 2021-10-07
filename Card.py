from PIL import ImageTk,Image
import os

cards_loc  = '.\cards'
hidden_card_loc = '.\Hidden Cards'

def collect_card():
    cards = os.listdir(cards_loc)
    cards = [card.split('.')[0] for card in cards]

    return cards

class Card():
    def init_(self,name,value = 11,is_displayed = True):
        self.name = name    
        self._is_displayed = is_displayed
        self._value = value

    @property
    def is_displayed(self):
        return self._is_displayed

    @is_displayed.setter
    def is_displayed(self,value):
        self._is_displayed = value

    @property

    def value(self):
        if str(self.name)[0] in ['J','Q','K']:
            self._value = 10               
        elif str(self.name)[0] == 'A':
            pass
        else:
            self._value = int(self.name.split('-')[0])
        return self._value

    @value.setter    
    def value(self,value):
        self._value = value



# returning heats,spade , etc..        


