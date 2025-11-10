#class Calculator:
    def add(self, a: float, b: float) -> float:
        """Сложение двух чисел"""
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """Вычитание двух чисел"""
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """Умножение двух чисел"""
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """Деление двух чисел"""
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b calculator-project-24.2.4/
# ├── calculator.py
# └── tests/
#     └── test_calculator.py

