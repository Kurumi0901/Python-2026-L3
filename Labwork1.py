# Ex 1:
r = float(input("Radius is: "));
area = 3.14 * r * r;
print(f"Circle area is: ", area);

# Ex 2:
C = float(input("Celcius is: "));
F =C * 1.8 + 32;
print(f"The temperature in Fahrenheit is: ", F);

# Ex 3:
num = int(input("Enter a number: "));
if num < 2:
  is_prime = False;
else:
  is_prime = True;
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      is_prime = False;
      break;

if is_prime:
  print(num, "is a prime number");
else:
  print(num, "is not a prime number");

# Ex 4:
num = int(input("Enter a number? "))

total_divisors = sum([i for i in range(1, num) if num % i == 0])

if total_divisors == num and num > 0:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is a NOT perfect number")


# Ex 5:
colors = ["green", "blue", "yellow", "pink", "red", "brown"];
fav_color = input("What's your favorite color?");
if fav_color in colors:
  print(f"Your color is at index {colors.index(fav_color)} in my list");
else:
  print(f"Sorry, I could not find your color")


# Ex 6:
range1 = list(range(0, 7))
range2 = list(range(1, 11, 3))
range3 = list(range(5, 0, -1))
range4 = list(range(6, -3, -2))

print("range1:", ", ".join(map(str, range1)))
print("range2:", ", ".join(map(str, range2)))
print("range3:", ", ".join(map(str, range3)))
print("range4:", ", ".join(map(str, range4)))

# Ex 7:
def remove_dollar_sign(s):
    return s.replace("$", "")
# Example:
print(remove_dollar_sign("100$ USD"))


# Ex 8:
def extract_even(l):
    return [x for x in l if x % 2 == 0]
# Example:
print(extract_even([1, 4, 5, -1, 10]))  


# Ex 9:
def factorial(n):
    if n < 0:
        return "N/A"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# Example:
print(factorial(5))  

# Ex 10:
def get_divisors(n):
    return [i for i in range(1, abs(n) + 1) if n % i == 0]
# Example:
print(get_divisors(12))  


# Ex 11:

x1 = float(input("Enter point x1: "))
y1 = float(input("Enter point y1: "))
x2 = float(input("Enter point x2: "))
y2 = float(input("Enter point y2: "))

distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
print("Distance = ",distance)


# Ex 12:
def print_pattern(m, n):
    for _ in range(m):
        print("*" * n)

# Example:
print_pattern(3, 4)