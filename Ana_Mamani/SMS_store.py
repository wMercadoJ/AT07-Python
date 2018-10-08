# class SMS STORE
# author Ana Mamani Zenteno
# since 10/05/2018
class SMS_store:
    def __init__(self):
        self.messages_arrival = []

    def add_new_messages_arrival(self, from_number, time_arrived, text_of_SMS):
        self.messages_arrival.append([False, from_number, time_arrived, text_of_SMS])

    def my_inbox_message_count(self):
        print(len(self.messages_arrival))

    def get_unread_indexes(self):
        list_not_riewed = []
        for i in range(len(self.messages_arrival)):
            if self.messages_arrival[i][0] == False:
                list_not_riewed.append(i)
        return list_not_riewed

    def return_messager(self, index):
        variable = instance_class.get_unread_indexes()
        for i in variable:
            if i == index:
                self.messages_arrival[i][0] = True
                return self.messages_arrival[i]

    def my_inbox_delete(self, index):
        index_delete = instance_class.get_unread_indexes()
        index_delete.remove(index)
        return index_delete

    def my_inbox_clear(self):
        self.messages_arrival.clear()


instance_class = SMS_store()
instance_class.add_new_messages_arrival(1234, "12:34", "hello elmer")
instance_class.add_new_messages_arrival(2124, "18:34", "I love elmer")
print(instance_class.messages_arrival)
print(instance_class.my_inbox_message_count())
print(instance_class.my_inbox_get_message())
print(instance_class.get_unread_indexes())
print(instance_class.return_messager(1))
print(instance_class.get_unread_indexes())
print(instance_class.my_inbox_delete(1))
print(instance_class.get_unread_indexes())
print(instance_class.my_inbox_delete())
