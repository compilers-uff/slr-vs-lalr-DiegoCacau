import ply.lex as lex
import ply.yacc as yacc

# definição de tokens
tokens = ['id', 'EQUAL', 'MULT']

t_EQUAL = r'\='
t_MULT  = r'\*'

# funcoes de erro para evitar warnings
def t_error(t):
    print ("Erro no token")

# definicao da gramatica
def p_error(p):
    print(f"Erro ao parsear")

def p_s(p):
    '''S : L EQUAL R 
         | R'''
    return p

def p_l(p):
    '''L : MULT R 
       | id'''
    return p

def p_r(p):
    'R : L '
    return p

# settando inicio 
start = 'S'

lex.lex() 

yacc.yacc(method="SLR")