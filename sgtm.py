import ast
def is_valid_python(code):
   try:
       ast.parse(c0de)
   except SyntaxError:
       return False
   return True
