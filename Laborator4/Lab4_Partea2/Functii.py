import random
import math

def calcfitness(x1, x2):
    fitness = -math.cos(x1) * math.cos(x2) * (math.exp(-(x1 - math.pi)**2 - (x2 - math.pi)**2))
    return fitness
