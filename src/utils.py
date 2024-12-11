from config import *
from random import *



def check_collision (entity1, entity2):
     if entity1[0] < entity2[0] + larg_sprite and entity1[0] + longeur_sprite > entity2[0] and entity1[1] < entity2[1] + larg_sprite and entity1[1] + longeur_sprite > entity2[1]:
          return True
     else:
          return False
                    
