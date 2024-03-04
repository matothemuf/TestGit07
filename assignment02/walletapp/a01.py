#class vinyl
class Vinyl:
   def __init__(self, album, artist, year):
       self.__album = album
       self.__artist = artist
       self.__year = year

   def upgrade(self):
       return 0

   def display(self):
       print (self.__album + ' , ' + self.__artist + ' , ' + str(self.__year))

def run():
   For_You = Vinyl('For You','Tatsuro Yamashita','1982')
   Cassa_Nova = Vinyl('Cassa Nova','Sunset Rollercoaster','2018')
   Ego_Death = Vinyl('Ego Death','The Internet','2015')
   Breathless= Vinyl('Breathless', 'Kenny G', '1992')

   For_You.display()
   Cassa_Nova.display()
   Ego_Death.display()
   Breathless.display()