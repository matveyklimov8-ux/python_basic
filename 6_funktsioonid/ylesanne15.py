# Ülesanne 15. Celsius Fahrenheitiks

def celsius_fahrenheit(c):
    return c * 9 / 5 + 32

for c in (0, 20, 37, 100):
    print(f"{c} °C = {celsius_fahrenheit(c):.1f} °F")
