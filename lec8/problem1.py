models.py 



class Equation(db.Model):
    ..... 
    ..... 
    .... 


In python interpretator:
from app import db
from app.models import Equation 

e1 = Equation(a=0, b=2, c=3) # ax^2 + bx + c = 0
print(e1)
<Equation 0*x^2 + 2*x + 3=0 has 1 solution(s)>