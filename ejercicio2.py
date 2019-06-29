import numpy as np

class TreeNode:
    """Clase para crear los nodos del arbol
    Atributos
    ----------
    val : int
        valor del nodo
    left : TreeNode
        nodo hijo a la izquieda
    right : TreeNode
        nodo hijo a la derecha
    root : TreeNode
        nodo padre
    is_leaf : Boolean
        indica si es una hoja(nodo final)
    """
    def __init__(self, x):
        """
        x : int
            numero correspondiente al nodo
        """
        self.val = x
        self.left = None
        self.right = None
        self.root = None
        self.is_leaf = True
        
    def add_node(self,node):
        """Metodo para adicionar nodo hijo
        -se indica que ya no es una hoja
        -se valida si se adiciona a la rama izquierda o derecha
        
        Parameters:
        node: TreeNode
            Nodo hijo
        """
        self.is_leaf = False
        node.root=self
        if self.left == None:
            self.left = node
        else:
            self.right = node
    
def path(node, k):
    """Metodo para encontrar la ruta de un nodo a otro, se valida si el nodo2 esta en los hijos(lef,right)
        
        Parameters:
            node: TreeNode
                Nodo1 root
            K: int
                valor del nodo2 a buscar en la ruta
        
        Returns:
            list
                lista de los nodos de la ruta de (n1 a n2)
    """
    if not node:
        return []
    if node.val == k:
        return [node.val]
    res = path(node.left, k)
    if res:
        return [node.val] + res
    res = path(node.right, k)
    if res:
        return [node.val] + res
    return []
    
def nodes_path(node, k):
    """Metodo para encontrar los nodos de la ruta entre node1 y node2
        
        Parameters:
            node: TreeNode
                Nodo1
            K: int
                valor del nodo2 a buscar en la ruta
        
        Returns:
            list
                lista de los nodos de la ruta de (n1 a n2)
    """
    # si no es un nodo hoja, se busca la ruta a partir de ese nodo
    if not node.is_leaf : 
        res = path(node,k)
        if res:
            return res
    
    # se itera nuevamente con el nodo padre para buscar la ruta        
    res = nodes_path(node.root,k)
    if res:
        return [node.val] + res

    return []
    
def sum_unique_colors(nodes,colors):
    """Metodo para encontrar los nodos de la ruta entre node1 y node2
        
        Parameters:
            nodes: list
                nodos de la ruta entre node1 y node2
            colors: list
                colores correspondientes a cada nodo
        
        Returns:
            int
                suma de colores unicos
    """
    colors_nodes=[colors[x-1] for x in nodes]
    return len(set( colors_nodes ))
    

# en esta seccion se toman los parametros de entrada del usuario para construir el arbol
M = int(input())
x = [None] * M
colors = [int(x) for x in input().split()]

for i in range(0, M-1):
    node1, node2 = map(int, input().split(' '))
    index1=int(node1)-1
    index2=int(node2)-1
    
    if x[index1] == None:
        x[index1] = TreeNode(node1)
    
    if x[index2] == None:
        x[index2] = TreeNode(node2)
    
    x[index1].add_node(x[index2])  


# en esta seccion se crea un matrix para guardar la suma de las rutas entre nodos (Node 0-Node n)
a = np.zeros(shape=(M,M))
np.fill_diagonal(a, 1)

for j in range(0, M):
    summ=0
    for i in range(0, M):
        if a[j][i] == 0: 
            node1=x[j]
            node2=x[i]
            
            nodes=nodes_path(node1, node2.val)
            
            summ=sum_unique_colors(nodes,colors)
            a[j][i] = summ
            a[i][j] = summ

print("Resumen sumatoria")
print (a)
print("Suma nodos:")
print (a.sum(axis=1))














