# isso é um comentário de 1 linha
print("""
      Day 1 - Python Print Function
      The function is declared like this:
      print('what to print')
      use ''' texto 
      a ser escrito
      '''
      três aspas para criar texto com quebra 
      de texto sem o contrabarra N
      """)

name = "Slim"
idade = 36 

print(f"Meu nome é {name} e tenho {idade} anos\ncontrabarra N para criar uma nova linha")



print("""
      Use a função input("Digite sua pergunta") 
      para pegar informação do usuário
      """)

#print(f'Olá {input("qual é o seu nome?")}!\n')
print(f"""use string literals para agrupar funções
      ex: (f'Olá conchetes input("qual é o seu nome?") conchetes !' """)


#print( len( input("What is your string? ") ) )

name = input("What is your name? ")
print(f"Olá {name}, seu nome tem {len(name)} letras")


## Alternating variables
a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)

