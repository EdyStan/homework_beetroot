from dll import OrderedLinkedList
from binary_search import binary_search

if __name__ == '__main__':
    the_list = OrderedLinkedList()
    the_list.add_node(10)
    the_list.print()
    the_list.add_node(5)
    the_list.print()
    the_list.add_node(7)
    the_list.print()
    the_list.add_node(13)
    the_list.print()
    the_list.add_node(7)
    the_list.print()

    print(binary_search(the_list.head, 10))
    print(binary_search(the_list.head, 5))
    print(binary_search(the_list.head, 7))
    print(binary_search(the_list.head, 13))
    # assert 5 == binary_search(the_list, 5)
    # assert 10 == binary_search(the_list, 10)
    # assert 7 == binary_search(the_list, 7)
    # assert 13 == binary_search(the_list, 13)
