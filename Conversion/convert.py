class Conversion:
    def __init__(self, value):
        self.value = value
        self.source = "Celsius"  # Lähdeyksikkö
        self.destination = "Fahrenheit"  # Kohdeyksikkö

class TemperatureConversion(Conversion):
    def convert(self): #celsius to fahrenheit
        result = float((9 * self.value) / 5 + 32)
        return result

    def convertBack(self): #fahrenheit to celsius
        result = float((self.value - 32) * 5 / 9)
        return result