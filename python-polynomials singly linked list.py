class PolyNode:
    def __init__(self, coefficient=0, exponent=0, next=None):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = next

class PolyLinkedList:
    def __init__(self):
        self.head = PolyNode()

    def add_term(self, coefficient, exponent):
        # Find the node where the new term should be inserted
        curr = self.head
        while curr.next is not None and curr.next.exponent > exponent:
            curr = curr.next

        # Insert the new term
        if curr.next is not None and curr.next.exponent == exponent:
            curr.next.coefficient += coefficient
        else:
            new_node = PolyNode(coefficient, exponent, curr.next)
            curr.next = new_node

    def delete_term(self, exponent):
        if self.head is None:
            return

        if self.head.exponent == exponent:
            self.head = self.head.next
        else:
            current = self.head
            while current.next is not None and current.next.exponent != exponent:
                current = current.next
            if current.next is not None:
                current.next = current.next.next

    def add_polynomials(p1, p2):
        result = PolyLinkedList()
        curr1 = p1.head.next
        curr2 = p2.head.next

        while curr1 is not None and curr2 is not None:
            if curr1.exponent > curr2.exponent:
                result.add_term(curr1.coefficient, curr1.exponent)
                curr1 = curr1.next
            elif curr2.exponent > curr1.exponent:
                result.add_term(curr2.coefficient, curr2.exponent)
                curr2 = curr2.next
            else:
                result.add_term(curr1.coefficient + curr2.coefficient, curr1.exponent)
                curr1 = curr1.next
                curr2 = curr2.next

        while curr1 is not None:
            result.add_term(curr1.coefficient, curr1.exponent)
            curr1 = curr1.next

        while curr2 is not None:
            result.add_term(curr2.coefficient, curr2.exponent)
            curr2 = curr2.next

        return result

    def multiply_polynomials(p1, p2):
        result = PolyLinkedList()
        curr1 = p1.head.next

        while curr1 is not None:
            curr2 = p2.head.next
            while curr2 is not None:
                result.add_term(curr1.coefficient * curr2.coefficient, curr1.exponent + curr2.exponent)
                curr2 = curr2.next
            curr1 = curr1.next

        return result

    def print_polynomial(p):
        curr = p.head.next
        if curr is None:
            print("0")
            return

        while curr is not None:
            if curr.coefficient != 0:
                if curr.exponent == 0:
                    print(curr.coefficient, end="")
                elif curr.exponent == 1:
                    if curr.coefficient == 1:
                        print("x", end="")
                    elif curr.coefficient == -1:
                        print("-x", end="")
                    else:
                        print(curr.coefficient, "x", sep="", end="")
                else:
                    if curr.coefficient == 1:
                        print("x^", curr.exponent, sep="", end="")
                    elif curr.coefficient == -1:
                        print("-x^", curr.exponent, sep="", end="")
                    else:
                        print(curr.coefficient, "x^", curr.exponent, sep="", end="")
                if curr.next is not None and curr.next.coefficient > 0:
                    print(" + ", end="")
                elif curr.next is not None:
                    print(" ", end="")
            curr = curr.next
        print()

# Example usage
p1 = PolyLinkedList()
p1.add_term(3, 14)
p1.add_term(2, 8)
p1.add_term(4, 5)
p1.add_term(1, 0)
p1.print_polynomial()

p1.delete_term(5)
p1.print_polynomial()

p2 = PolyLinkedList()
p2.add_term(8, 14)
p2.add_term(-3, 10)
p2.add_term(10, 6)
p2.print_polynomial()

p3 = p1.add_polynomials(p2)
print("p1 + p2 = ", end="")
p3.print_polynomial()  

p4 = p1.multiply_polynomials(p2)
print("p1 * p2 = ", end="")
p4.print_polynomial()  


