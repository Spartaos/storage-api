"""
Modulo Ejemplo

Este modulo sera un ejmplo para que se use como base,
para el dearrollo futuro de otros modulos.

NOTA:
    No debes importara ninguna cuestion relaciona con _bottle_.

"""
import datetime as dt


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


def estructurar_mensaje(fecha, mensaje):
    """
    Funcion para estructurar mensaje
    recibe como argumentos
     - fecha, una cadena de texto que represente la fecha
     en formato iso.
     - mensaje, una cadena de texto que carga el mensaje
     a estructurar.

    En caso de que el argumento no sea una fecha
    valida en formato iso, se levantara un Excepcion
    con mesanje `Fecha invalida.`.

    Esta funcion regresara un diccionario con 2
    llaves, `date` y `message`.

    >>> estructurar_mensaje('2021-05-01T20:23:22', 'Hola mundo')
    {'date': '2021-05-01T20:23:22', 'message': 'Hola mundo'}
    >>> estructurar_mensaje('foo', 'Hola mundo')
    Traceback
     ...
    Exception: Fecha invalida.
    """
    try:
        date = dt.datetime.fromisoformat(fecha)
    except:
        raise Exception("Fecha invalida.")
    return {
        "date": date.isoformat(),
        "message": mensaje
    }
