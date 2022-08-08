## Functions
# Function to print an result and her type
def print_result_and_type(r) -> None:
  print(str(r) + ": " + type(r).__name__)

# Function to calc the iva of price
def calc_price_with_iva(price: float, iva: float = 0.19) -> float:
  return price + (price * iva)

def calc_iva_of_price(price: float, iva: float = 0.19) -> float:
  return price * iva

def iva_calc(price: float, iva: float = 0.19) -> None:
  print(f'Price({price}) with iva: ' + str(calc_price_with_iva(price, iva)))
  print(f'Iva of price({price}): ' + str(calc_iva_of_price(price, iva)))


## Steps
# First Step:
number = 10
number_two = 20 

result = number + number_two

print_result_and_type(result)

# Second Step:
number = 10
number_two = 20.5

result = number + number_two

print_result_and_type(result)

# Third Step:
price = 100
iva_calc(price)