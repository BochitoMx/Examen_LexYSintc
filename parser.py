import ply.yacc as yacc
from lexer import tokens


def p_programa(p):
    '''programa : PROGRAMA IDENTIFICADOR PARENTESIS_APERTURA PARENTESIS_CIERRE LLAVE_APERTURA declaraciones LLAVE_CIERRE'''
    print("Programa correctamente definido.")

def p_declaraciones(p):
    '''declaraciones : declaraciones declaracion
                     | declaraciones instruccion
                     | declaracion
                     | instruccion'''
    pass

def p_declaracion(p):
    '''declaracion : tipo lista_variables PUNTOYCOMA'''
    print(f"Declaración: {p[1]} {p[2]}")

def p_lista_variables(p):
    '''lista_variables : lista_variables COMA IDENTIFICADOR
                       | IDENTIFICADOR'''
    print(f"Lista de variables: {p[1:]}")

def p_instruccion(p):
    '''instruccion : READ IDENTIFICADOR PUNTOYCOMA
                   | PRINTF CADENA PUNTOYCOMA
                   | IDENTIFICADOR ASIGNAR expresion PUNTOYCOMA
                   | END PUNTOYCOMA'''
    print(f"Instrucción: {p[1:]}")

def p_tipo(p):
    '''tipo : INT'''
    print(f"Tipo: {p[1]}")

def p_expresion(p):
    '''expresion : expresion SUMA termino
                 | expresion RESTA termino
                 | termino'''
    print(f"Expresión: {p[1:]}")

def p_termino(p):
    '''termino : termino MULT factor
               | termino DIV factor
               | factor'''
    print(f"Término: {p[1:]}")

def p_factor(p):
    '''factor : PARENTESIS_APERTURA expresion PARENTESIS_CIERRE
              | NUMERO
              | IDENTIFICADOR'''
    print(f"Factor: {p[1]}")

def p_error(p):
    if p:
        error_message = f"Error de sintaxis cerca del token '{p.value}' en la línea {p.lineno}, columna {p.lexpos}."
        print(error_message)
        raise SyntaxError(error_message)
    else:
        raise SyntaxError("Error de sintaxis: fin inesperado de entrada.")


parser = yacc.yacc()

def analizar_sintaxis(codigo):
    try:
        result = parser.parse(codigo)
        return "La sintaxis ingresada está correctamente estructurada" if result else "Error de sintaxis"
    except SyntaxError as e:
        return str(e)