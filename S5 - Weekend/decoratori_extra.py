"""

Decorators extra

Implementati o clasa User, cu urmatoarele cerinte:
– constructorul va primi nume, email, parola, si data nasterii
– o metoda login, care va primi email si parola ca parametrii; daca acestea sunt corecte, userul va fi marcat ca logat
– o metoda get_info, care va returna toate informatiile despre user DOAR DACA acesta este logat, folosind un decorator `@require_login`
– o metoda logout, fara params, care delogheaza userul.


Se va testa apelarea metodei get_info inainte de logare, dupa logare, dupa delogare, si dupa inca o logare.

"""
