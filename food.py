import pygame
import random

# Array of vegetable names
vegetable_types = ["bread", "cheese", "egg", "jam", "pb", "milk"]

# Dictionary mapping food types to image file paths
food_images = {
    "bread": "images/bread.png",
    "cheese": "images/cheese.png",
    "egg": "images/egg-removebg-preview.png",
    "jam": "images/jam.png",
    "pb": "images/pb.png",
    "milk": "images/milk-removebg-preview.png"
}

class Food:
  def __init__(self, shape, name, price):
    self.shape = shape
    self.name = name
    self.price = price
    
    # Load the image based on the food type
    self.image_path = food_images.get(self.name, "images/default.png")
    self.image = pygame.image.load(self.image_path)
    self.image = pygame.transform.scale(self.image, (self.shape.width, self.shape.height))

# Function to create a random vegetable with a specified index
def create_vegetable(index):
    x = random.randint(100, 700)  # Adjust the range based on your screen dimensions
    y = random.randint(100, 500)
    vegetable_name = vegetable_types[index % len(vegetable_types)]
    vegetable_rect = pygame.Rect(x, y, 30, 30)
    vegetable = Food(vegetable_rect, vegetable_name, 1.00)
    return vegetable