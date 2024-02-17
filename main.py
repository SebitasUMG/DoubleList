import graphviz


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev

                return
            current = current.next

    def display_list(self):
        current = self.head
        while current:
            print(current.data, end=" | ")
            current = current.next
        print("Vacío")

    def visualize_list(self, filename='doubly_linked_list'):
        dot = graphviz.Digraph(comment='Lista doblemente enlazada')
        current = self.head
        while current:
            dot.node(str(id(current)), str(current.data))
            if current.prev:
                dot.edge(str(id(current.prev)), str(id(current)))
            current = current.next
        dot.render(filename, format='png', cleanup=True)
        print(f"Visualización de Graphviz:  {filename}.png")


def main():
    dll = DoublyLinkedList()

    while True:
        print("Bienvenidos al programa!!!!")
        print("\nOperaciones de la lista:")
        print("1. Insertar un elemento al principio")
        print("2. Insertart elemento al final")
        print("3. Borrar un elemento ")
        print("4. Mostrar lista en consola")
        print("5. Generar visualizacion en Graphviz")
        print("6. Salir")

        choice = int(input("Ingrese su opciòn a realizar: \n"))

        if choice == 1:
            data = input("Ingrese la frase que desea insertar al principio: ")
            dll.insert_at_beginning(data)
        elif choice == 2:
            data = input("Ingrese la frase que desea insertar al final: ")
            dll.insert_at_end(data)
        elif choice == 3:
            data = input("Ingrese la frase que desea eliminar: ")
            dll.delete_node(data)
        elif choice == 4:
            print("Mostrando la lista en consola....")
            dll.display_list()
        elif choice == 5:
            dll.visualize_list()
            print("Vista de Graphviz...")
        elif choice == 6:
            break
        else:
            print("Ingrese una opción correcta")


if __name__ == "__main__":
    main()
