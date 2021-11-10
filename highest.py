import math

def highest(figures):
    numbers = sorted(figures, key=abs, reverse=True )
    neg_count = 0
    pos_count = 0
    
    for i in numbers[:4]:
        if i < 0:
            neg_count += 1
            if neg_count % 2 == 0:
               math.prod(i)
               





highest([-10, -20, 5, 2])
