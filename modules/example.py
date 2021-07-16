"""
Modulo Ejemplo

Este modulo sera un ejmplo para que se use como base,
para el dearrollo futuro de otros modulos.

NOTA:
    No debes importara ninguna cuestion relaciona con _bottle_.

"""


def example_helper_function(*args, **kwargs):
    """
    Ejemplo de documentacion para funcion
    `example_helper_function`.
    esta funcion recibe una cantidad arbiraria de
    argumentos posicionales y nombrados, los
    imprime y no regresa nada.

    >>> example_helper_function(1, 2, 3, uno="dos")
    (1, 2, 3)
    {'uno': 'dos'}
    >>> example_helper_function(1)
    (1,)
    {}
    """
    print(args)
    print(kwargs)
    return None
