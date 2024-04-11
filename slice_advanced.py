def slice_advanced():
    # Código a implementar utilizando input.
texto = "Awesome"
print(texto[0:3].lower())
print(texto[len(texto)//2-1:len(texto)//2+2].lower())
print(texto[0:4].lower() + texto[-2:].lower())
# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_advanced_test.py` o `python tp3_slice_advanced_test.py`
