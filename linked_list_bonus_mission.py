#Linked lists bonus mission
#Data structures and algorithms
#Mikael Pennanen


valinnat = {}
valinnat[1] = "Henkilotiedon lisays"
valinnat[2] = "Henkilotietojen tulostus"
valinnat[3] = "Kaikkien henkilotietojen poisto"
valinnat[0] = "Lopetus"
valinnat[4] = "Youtube"

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data
    
class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> " .join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def print_nodes(self):
        node = self.head
        if node is not None:
            print(llist)
        else:
            print("Lista on tyhja.")

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_before(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        
        raise Exception("Node with '%s' not found" % target_node_data)

    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception("Lista on tyhja")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("Node with '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception("Lista on tyhja")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_all_nodes(self):
        if self.head is None:
            print("Lista on jo tyhja!")
        while (self.head is not None):
            tyhja = self.head
            self.head = self.head.next
            tyhja = None
        return

def valinnat():
    while True:
        print("""
        Mita tehdaan seuraavaksi?
        1 = Henkilotiedon lisays
        2 = Henkilotietojen tulostus
        3 = Kaikkien henkilotietojen poisto
        0 = Lopetus
        """)
        print()
        valinta = input("Valintasi: ")
        if valinta == "1":
            print("Henkilotietojen lisays ")
            print()
            print("Anna henkilon nimi: > ")
            nimi = input("")
            print()
            print("Anna henkilon osoite: > ")
            osoite = input("")
            print()
            print("Anna henkilon puhelinnumero: > ")
            numero = input("")
            tiedot = "[" + nimi + " : " + osoite + " : " + numero + " ] "
            llist.add_last(Node(tiedot))
            
        elif valinta == "2":
            print("Henkilotietojen tulostus ")
            llist.print_nodes()
            #print(llist)
            print()
        elif valinta == "3":
            llist.remove_all_nodes()
        elif valinta == "0":
            print("Ohjelma lopetettu.")
            break


llist = LinkedList()

valinnat()
