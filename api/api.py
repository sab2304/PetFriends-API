import requests
import os

# Существующие методы + 2 новых

def find_pets_by_status(status: str, base_url: str = "https://petstore.swagger.io/v2") -> list:

def upload_image_to_pet(pet_id: int, image_path: str, base_url: str = "https://petstore.swagger.io/v2") -> dict:

# + 2 новых метода
def update_user(username: str, user_data: dict, base_url: str = "https://petstore.swagger.io/v2") -> dict:
    # моя реализация

def login_user(username: str, password: str, base_url: str = "https://petstore.swagger.io/v2") -> dict:
    # моя реализация
  
