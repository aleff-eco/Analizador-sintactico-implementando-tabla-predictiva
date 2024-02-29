def parse_table():
      
      terminals = [ "function", "(", "var",":", "string", "real", "boolean", "integer", ";", ")",  "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
      
      non_terminals = ["FUNCION", "PARAMETROS", "PARAMLIST", "VARIABLE", "PNOMBRE", "RESTOL", "LETRA", "IDENTIPO", "LIST"]

      parse_table = {
      "FUNCION": {
            "function": ["function", "PNOMBRE", "PARAMETROS"],
            "(": None,
            "var": None,
            ":": None,
            "string": None,
            "real": None,
            "boolean": None,
            "integer": None,
            ";": None,
            ")": None
      },

      "PARAMETROS": {
            "function": None,
            "(": ["(", "PARAMLIST", ")"],
            "var": None,
            ":": None,
            "string": None,
            "real": None,
            "boolean": None,
            "integer": None,
            ";": None,
            ")": None
      },

      "PARAMLIST": {
            "function": None,
            "(": None,
            "var": ["var", "VARIABLE", "LIST"],
            ":": None,
            "string": None,
            "real": None,
            "boolean": None,
            "integer": None,
            ";": None,
            ")": None
      },

      "VARIABLE": {
            "function": None,
            "(": None,
            "var": None,
            ":": None,
            "string": None,
            "real": None,
            "boolean": None,
            "integer": None,
            ";": None,
            ")": None,
            "a": ["PNOMBRE", ":", "IDENTIPO", ";"], "b": ["PNOMBRE", ":", "IDENTIPO"], "c": ["PNOMBRE", ":", "IDENTIPO"], "d": ["PNOMBRE", ":", "IDENTIPO"], "e": ["PNOMBRE", ":", "IDENTIPO"], "f": ["PNOMBRE", ":", "IDENTIPO"], "g": ["PNOMBRE", ":", "IDENTIPO"], "h": ["PNOMBRE", ":", "IDENTIPO"], "i": ["PNOMBRE", ":", "IDENTIPO"], "j": ["PNOMBRE", ":", "IDENTIPO"], "k": ["PNOMBRE", ":", "IDENTIPO"], "l": ["PNOMBRE", ":", "IDENTIPO"], "m": ["PNOMBRE", ":", "IDENTIPO"], "n": ["PNOMBRE", ":", "IDENTIPO"], "o": ["PNOMBRE", ":", "IDENTIPO"], "p": ["PNOMBRE", ":", "IDENTIPO"], "q": ["PNOMBRE", ":", "IDENTIPO"], "r": ["PNOMBRE", ":", "IDENTIPO"], "s": ["PNOMBRE", ":", "IDENTIPO"], "t": ["PNOMBRE", ":", "IDENTIPO"], "u": ["PNOMBRE", ":", "IDENTIPO"], "v": ["PNOMBRE", ":", "IDENTIPO"], "w": ["PNOMBRE", ":", "IDENTIPO"], "x": ["PNOMBRE", ":", "IDENTIPO"], "y": ["PNOMBRE", ":", "IDENTIPO"], "z": ["PNOMBRE", ":", "IDENTIPO"],
      },

      "PNOMBRE": {
            "function": None,
            "(": None,
            "var": None,
            ":": None,
            "string": None,
            "real": None,
            "boolean": None,
            "integer": None,
            ";": None,
            ")": None,
            "a": ["LETRA", "RESTOL"], "b": ["LETRA", "RESTOL"], "c": ["LETRA", "RESTOL"], "d": ["LETRA", "RESTOL"], "e": ["LETRA", "RESTOL"], "f": ["LETRA", "RESTOL"], "g": ["LETRA", "RESTOL"], "h": ["LETRA", "RESTOL"], "i": ["LETRA", "RESTOL"], "j": ["LETRA", "RESTOL"], "k": ["LETRA", "RESTOL"], "l": ["LETRA", "RESTOL"], "m": ["LETRA", "RESTOL"], "n": ["LETRA", "RESTOL"], "o": ["LETRA", "RESTOL"], "p": ["LETRA", "RESTOL"], "q": ["LETRA", "RESTOL"], "r": ["LETRA", "RESTOL"], "s": ["LETRA", "RESTOL"], "t": ["LETRA", "RESTOL"], "u": ["LETRA", "RESTOL"], "v": ["LETRA", "RESTOL"], "w": ["LETRA", "RESTOL"], "x": ["LETRA", "RESTOL"], "y": ["LETRA", "RESTOL"], "z": ["LETRA", "RESTOL"],
      },

      "RESTOL": {
            "function": None,
            "(": [],
            "var": None,
            ":": [],
            "string": None,
            "real": None,
            "boolean": None,
            "integer": None,
            ";": None,
            ")": None,
            "a": ["LETRA", "RESTOL"], "b": ["LETRA", "RESTOL"], "c": ["LETRA", "RESTOL"], "d": ["LETRA", "RESTOL"], "e": ["LETRA", "RESTOL"], "f": ["LETRA", "RESTOL"], "g": ["LETRA", "RESTOL"], "h": ["LETRA", "RESTOL"], "i": ["LETRA", "RESTOL"], "j": ["LETRA", "RESTOL"], "k": ["LETRA", "RESTOL"], "l": ["LETRA", "RESTOL"], "m": ["LETRA", "RESTOL"], "n": ["LETRA", "RESTOL"], "o": ["LETRA", "RESTOL"], "p": ["LETRA", "RESTOL"], "q": ["LETRA", "RESTOL"], "r": ["LETRA", "RESTOL"], "s": ["LETRA", "RESTOL"], "t": ["LETRA", "RESTOL"], "u": ["LETRA", "RESTOL"], "v": ["LETRA", "RESTOL"], "w": ["LETRA", "RESTOL"], "x": ["LETRA", "RESTOL"], "y": ["LETRA", "RESTOL"], "z": ["LETRA", "RESTOL"],
      },

      "LETRA": {
            "function": None,
            "(": None,
            "var": None,
            ":": None,
            "string": None,
            "real": None,
            "boolean": None,
            "integer": None,
            ";": None,
            ")": None,
            "a": ["a"], "b": ["b"], "c": ["c"], "d": ["d"], "e": ["e"], "f": ["f"], "g": ["g"], "h": ["h"], "i": ["i"], "j": ["j"], "k": ["k"], "l": ["l"], "m": ["m"], "n": ["n"], "o": ["o"], "p": ["p"], "q": ["q"], "r": ["r"], "s": ["s"], "t": ["t"], "u": ["u"], "v": ["v"], "w": ["w"], "x": ["x"], "y": ["y"], "z": ["z"],
      },

      "IDENTIPO": {
            "function": None,
            "(": None,
            "var": None,
            ":": None,
            "string": ["string"],
            "real": ["real"],
            "boolean": ["boolean"],
            "integer": ["integer"],
            ";": None,
            ")": None
      },

      "LIST": {
            "function": None,
            "(": None,
            "var": None,
            ":": None,
            "string": None,
            "real": None,
            "boolean": None,
            "integer": None,
            ";": [";", "VARIABLE", "LIST"],
            ")": []

      },
}
      return terminals, non_terminals, parse_table
