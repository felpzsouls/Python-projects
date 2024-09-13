from random import randint

def get_response(user_input : str ) -> str:
  lowerd : str = user_input.lower()

  if lowerd == '':
    return 'Só restou o silêncio...'
  elif 'olá' in lowerd:
    return 'Olá, tudo bem?'
  elif 'tchau' in lowerd:
    return 'Tchau, até a próxima!'
  elif 'como vai' in lowerd:
    return 'Estou bem, obrigada!'
  elif 'd4' in lowerd:
    return str(randint(1, 4))
  elif 'd6' in lowerd:
    return str(randint(1, 6))
  elif 'd8' in lowerd:
    return str(randint(1, 8))
  elif 'd10' in lowerd:
    return str(randint(1, 10))
  elif 'd12' in lowerd:
    return str(randint(1, 12))
  elif 'd20' in lowerd:
    return str(randint(1, 20))
  elif 'd100' in lowerd:
    return str(randint(1, 100))
  else:
    return 'Não entendi, pode repetir?'
