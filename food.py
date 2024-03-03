import pygame
import random

class Food:
  def __init__(food, shape, name, price):
    food.shape = shape
    food.name = name
    food.price = price

# Array of vegetable names
vegetable_types = ["tomato", "blueberry", "cherry"]

# Function to create a random vegetable with a specified index
def create_vegetable(index):
    x = random.randint(100, 700)  # Adjust the range based on your screen dimensions
    y = random.randint(100, 500)
    vegetable_name = vegetable_types[index % len(vegetable_types)]
    vegetable_rect = pygame.Rect(x, y, 20, 20)
    vegetable = Food(vegetable_rect, vegetable_name, 1.00)
    return vegetable