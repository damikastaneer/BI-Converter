class NumberConverter:
    def __init__(self, value, input_base):
        self.decimal = int(value, input_base)

    def convert_to(self, output_base):
        converters = {
            2: lambda x: bin(x)[2:],
            10: lambda x: str(x),
            16: lambda x: hex(x)[2:].upper(),
        }

        if output_base not in converters:
            raise ValueError("Base niet ondersteund")

        return converters[output_base](self.decimal)
