from table import *
from table import parse_table
import re

terminals, non_terminals, parse_table = parse_table()

class Parser:
    def __init__(self, input_string):
        try:
            invalid_chars = re.findall(r'#|\$|%|&|1|2|3|4|5|6|7|8|9|0|/|=|\?', input_string)
            if invalid_chars:
                print(f"Error: Caracteres invalidos: {' '.join(invalid_chars)}")
                print('Error de gramatica')
                raise ValueError("Caracteres invalidos en la sentencia")

            self.input_string = re.findall(r'function|string|real|boolean|integer|\(|\)|var|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|r|s|t|u|v|w|x|y|z|:|;', input_string)
            self.stack = ["$", "FUNCION"]
            self.stack_trace = []

        except Exception as e:
            print(f"Error: {e}")
            self.stack = []  
            self.stack_trace = []

    def parse(self):
        i = 0
        pos = 0
        error = None
        try:
            while len(self.stack) > 0 and i < len(self.input_string):
                top = self.stack[-1]
                self.stack_trace.append((self.stack[:], self.input_string[i], pos, error))
                print(f"\nstack '{self.stack}'")
                print(f"input string '{self.input_string[i]}'")
                print(f"posicion '{pos}'")
                print(f"Pila '{self.input_string[i]}' |-| {' '.join(self.stack)}")
                if top in terminals:
                    if top == self.input_string[i]:
                        self.stack.pop()
                        i += 1
                        pos += 1
                    else:
                        error = f"Error: Se esperaba '{top}', pero se encontró '{self.input_string[i]}' en la posición {pos}."
                        print(error)
                        return {'success': False, 'stack_trace': self.stack_trace, 'error': error}
                elif top in non_terminals:
                    if self.input_string[i] in parse_table[top]:
                        production = parse_table[top][self.input_string[i]]
                        self.stack.pop()
                        pos += 1
                        if production != ["vacio"]:
                            self.stack.extend(production[::-1])
                    else:
                        error = f"Error: No hay producción definida para '{top}' con '{self.input_string[i]}' en la posición {pos}."
                        print(error)
                        return {'success': False, 'stack_trace': self.stack_trace, 'error': error}
                else:
                    error = f"Error: Elemento inesperado '{top}' en la posición {pos}."
                    print(error)
                    return {'success': False, 'stack_trace': self.stack_trace, 'error': error}

            if len(self.stack) == 1 and self.stack[0] == "$":
                return {'success': True, 'stack_trace': self.stack_trace}
            else:
                error = f"Error: La pila no está vacía al final del análisis en la posición {pos}."
                print(error)
                return {'success': False, 'stack_trace': self.stack_trace, 'error': error}
        except Exception as e:
            print(f"Error durante el parse: {e}")
            error = f"Error: Excepción inesperada en la posición {pos}."
            print(error)
            return {'success': False, 'stack_trace': self.stack_trace, 'error': error}