import statistics

def _print(N, wrong=False):
    """Imprime el mensaje al usuario
    Si no estuvo mal la operacion se retorna la mediana de la lista de valores

        Parametros
        ----------
        N : list
            lista con valores
        wrong : boolean, optional
            indica si la operacion tuvo error
    """
    msg='Wrong!' if wrong else statistics.median(N)
    print(msg)

def _add(N,x):
    """Adiciona un nuevo valor y envia a imprimir

        Parametros
        ----------
        N : list
            lista con valores
        x : int
            nuevo valor a la lista
    """
    N.append(x)
    _print(N)
    
def _remove(N,x):
    """Elimina el valor de la lista
    -Se valida que el valor exista antes de enviar a imprimir
        Parametros
        ----------
        N : list
            lista con valores
        x : int
             valor a eliminar de la lista
    """
    if x not in N:
        _print(N,True)
    else:
        N.remove(x)
        _print(N,len(N)==0)

# En esta seccion se crea la lista de valores y se indica la operacion a realizar
M = int(input())
N=[]
for i in range(0, M):
    in_line = input().split(' ')
    operation, x = [xx for xx in in_line]
    x=int(x)
    if operation=='a':
        _add(N,x)
    else:
        _remove(N,x)
