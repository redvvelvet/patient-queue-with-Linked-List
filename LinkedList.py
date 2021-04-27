from tabulate import tabulate
import pandas as pd


class Patient:
    def __init__(self):
        self.name = None
        self.age = None
        self.next = None

    def __repr__(self):
        return "<name: {}, age: {}, next: {}>".format(self.name, self.age, self.next)


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def __repr__(self):
        return "<Linked List: Head: {}>".format(self.head)


def append(linkedlist, name, age):
    new_patient = Patient()
    new_patient.name = name
    new_patient.age = age
    new_patient.next = None

    if linkedlist.head is None:
        linkedlist.head = new_patient
        linkedlist.count += 1
    else:
        current = linkedlist.head
        while current.next is not None:
            if linkedlist.count == 14:
                print('QUEUE IS FULL!!!')
                return linkedlist
            current = current.next
        current.next = new_patient
        linkedlist.count += 1
    return linkedlist


def pop(linkedlist):
    if linkedlist.head is None:
        return None
    else:
        current = linkedlist.head
        linkedlist.head = linkedlist.head.next
        current.next = None
        linkedlist.count -= 1
        return linkedlist


def remove(linkedlist, name):
    current = linkedlist.head
    if current is None:
        return None
    else:
        # key is in head
        if current.name is name:
            # key is in head and linked list only has one node
            if current.next is None:
                linkedlist.head = None
                linkedlist.count -= 1
            # key is in head and linked list has many nodes
            else:
                linkedlist.head = linkedlist.head.next
                current.next = None
                linkedlist.count -= 1
        else:
            # key is not in head, loop to find key
            prev = None
            counter = 1
            while current is not None:
                if current.name is name:
                    if current.next is None:
                        prev.next = None
                        linkedlist.count -= 1
                        break
                    prev.next = current.next
                    current.next = None
                    linkedlist.count -= 1
                if current.name is not name and linkedlist.count == counter:
                    print('PATIENT NOT FOUND!!!')
                prev = current
                current = current.next
                counter += 1
    return linkedlist


def count(linkedlist):
    return linkedlist.count


def to_list(linkedlist):
    current = linkedlist.head
    name_list = []
    age_list = []
    while current is not None:
        name_list.append(current.name)
        age_list.append(current.age)
        current = current.next
    return name_list, age_list


def show():
    global patient_name
    linkedlist = LinkedList()

    choice = None
    while choice != 4:
        if choice == 1:
            patient_name = input("Nama: ")
            age = int(input("Umur: "))
            print(append(linkedlist, patient_name, age))
        elif choice == 2:
            print(pop(linkedlist))
        elif choice == 3:
            patient_name = input("Nama: ")
            print(remove(linkedlist, patient_name))

        print("""
        KrenkenHause ScharfeSpitze
                Ilsestr 23.
                  B-12051

        Daftar Pasien Penerima Vaksin
        """)

        # patient table
        patient_queue = pd.DataFrame({'Name': to_list(linkedlist)[0], 'Age': to_list(linkedlist)[1]})
        patient_queue = patient_queue.sort_values('Age', ascending=False).reset_index().drop(['index'], axis=1)
        patient_queue.index += 1
        print(tabulate(patient_queue, headers='keys', tablefmt='psql'))

        print("""
        Jumlah pasien   : {}
        """.format(linkedlist.count))

        # error message if queue is full
        if linkedlist.count == 14:
            print('!!! ANTRIAN PENUH !!!')

        # error message if patient is not found
        current = linkedlist.head
        counter = 1
        while current is not None:
            if current.name is not patient_name and linkedlist.count == counter:
                print('!!! PASIEN TIDAK DITEMUKAN !!!')
            current = current.next

        print("""
        Pilihan:
        1   Tambah pasien
        2   Panggil pasien berikutnya
        3   Panggilan darurat
        4   Keluar
        """)

        choice = int(input("Pilihan: "))


def test_for_append_if_linkedlist_is_empty():
    linkedlist = LinkedList()
    expected = "<Linked List: Head: <name: z, age: 12, next: None>>"
    result = str(append(linkedlist, 'z', 12))

    assert expected == result, "expected %s got %s" % (expected, result)


def test_for_append_if_linkedlist_has_two_elements():
    linkedlist = LinkedList()
    expected = "<Linked List: Head: <name: x, age: 10, next: <name: y, age: 11, next: <name: z, age: 12, next: None>>>>"
    result_3 = append(linkedlist, 'x', 10)
    result_2 = append(result_3, 'y', 11)
    result = str(append(result_2, 'z', 12))

    assert expected == result, "expected %s got %s" % (expected, result)


def tests():
    test_for_append_if_linkedlist_is_empty()
    test_for_append_if_linkedlist_has_two_elements()


def main():
    linkedlist = LinkedList()

    list_1 = append(linkedlist, 'Artemis', 40)
    list_2 = append(list_1, 'Apollo', 42)
    list_3 = append(list_2, 'Daphne', 38)
    list_4 = append(list_3, 'Orion', 35)
    list_5 = append(list_4, 'Athena', 20)
    list_6 = append(list_5, 'Neptune', 70)
    list_7 = append(list_6, 'Selene', 68)
    list_8 = append(list_7, 'Morpheus', 24)
    list_9 = append(list_8, 'Eloise', 27)
    list_10 = append(list_9, 'Ares', 55)
    list_11 = append(list_10, 'Nyx', 45)
    list_12 = append(list_11, 'Helios', 49)
    list_13 = append(list_12, 'Calypso', 62)
    list_14 = append(list_13, 'Hephaestus', 73)

    print(list_14)
    print(append(linkedlist, 'Hades', 100))
    print(remove(linkedlist, 'Hephaestus'))
    print(remove(linkedlist, 'Poseidon'))
    print(pop(linkedlist))
    print(append(linkedlist, 'Hades', 100))

    show()


if __name__ == '__main__':
    tests()
    main()
