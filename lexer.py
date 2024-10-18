import ply.lex as lex

tokens = [
    'IDENTIFICADOR', 'NUMERO', 'PARENTESIS_APERTURA', 'PARENTESIS_CIERRE',
    'LLAVE_APERTURA', 'LLAVE_CIERRE', 'PUNTOYCOMA', 'ASIGNAR', 
    'SUMA', 'RESTA', 'MULT', 'DIV', 'CADENA', 'VARIABLE', 'COMA', 'IGUAL', 'MENORQUE',

]


reservadas = {
    'if': 'IF', 'else': 'ELSE', 'for': 'FOR', 'while': 'WHILE', 'return': 'RETURN',
    'programa': 'PROGRAMA', 'int': 'INT', 'float': 'FLOAT', 'char': 'CHAR', 'void': 'VOID',
    'switch': 'SWITCH', 'case': 'CASE', 'break': 'BREAK', 'default': 'DEFAULT', 'do': 'DO',
    'continue': 'CONTINUE', 'static': 'STATIC', 'const': 'CONST', 'struct': 'STRUCT',
    'typedef': 'TYPEDEF', 'union': 'UNION', 'enum': 'ENUM', 'signed': 'SIGNED',
    'unsigned': 'UNSIGNED', 'sizeof': 'SIZEOF', 'long': 'LONG', 'short': 'SHORT',
    'main': 'MAIN', 'read': 'READ', 'end': 'END', 'print': 'PRINT', 'printf': 'PRINTF', 'include':'INCLUDE'
}

tokens += list(reservadas.values())

t_ASIGNAR = r'='
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_PUNTOYCOMA = r';'
t_PARENTESIS_APERTURA = r'\('
t_PARENTESIS_CIERRE = r'\)'
t_LLAVE_APERTURA = r'\{'
t_LLAVE_CIERRE = r'\}'
t_COMA = r','
t_CADENA = r'\".*?\"'
t_ignore = ' \t'


def t_VARIABLE(t):
    r'[a-dA-D]'
    t.value = t.value.lower() 
    return t

def t_IDENTIFICADOR(t):
    r'[e-zE-Z_][a-zA-Z_0-9]*'  # Identificadores deben empezar con letras fuera de a-d
    t.value = t.value.lower() 
    t.type = reservadas.get(t.value, 'IDENTIFICADOR')  # Si es palabra reservada, cambia el tipo
    return t

# Regla para números
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Manejo de errores léxicos
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def analizar_codigo(codigo):
    lexer.input(codigo)
    resultado = []

    for token in lexer:
        # Determinación del tipo del símbolo
        if token.type in ['SUMA', 'RESTA', 'MULT', 'DIV']:
            tipo = 'Operador'
        elif token.type in ['PARENTESIS_APERTURA', 'PARENTESIS_CIERRE']:
            tipo = 'Paréntesis'
        elif token.type in ['LLAVE_APERTURA', 'LLAVE_CIERRE']:
            tipo = 'Llave'
        elif token.type in ['PUNTOYCOMA', 'COMA', 'ASIGNAR']:
            tipo = 'Símbolo'
        elif token.type == 'NUMERO':
            tipo = 'Número'
        elif token.type == 'CADENA':
            tipo = 'Cadena'
        elif token.type == 'VARIABLE':
            tipo = 'Variable'
        else:
            tipo = 'Otro'  # Si no encaja en ninguna categoría específica

        fila = {
            'token': token.value,
            'palabra_reservada': 'X' if token.type in reservadas.values() else '',
            'identificador': 'X' if token.type == 'IDENTIFICADOR' else '',
            'variable': 'X' if token.type == 'VARIABLE' else '',
            'cadena': 'X' if token.type == 'CADENA' else '',
            'numero': 'X' if token.type == 'NUMERO' else '',
            'simbolo': 'X' if token.type in ['PARENTESIS_APERTURA', 'PARENTESIS_CIERRE', 'LLAVE_APERTURA', 'LLAVE_CIERRE', 'PUNTOYCOMA', 'ASIGNAR', 'SUMA', 'RESTA', 'MULT', 'DIV'] else '',
            'tipo': tipo  # Aquí agregamos el tipo de símbolo
        }
        resultado.append(fila)

    return resultado
