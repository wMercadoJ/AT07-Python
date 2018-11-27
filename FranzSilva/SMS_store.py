import datetime


class SMS_store:
    def __init__(self):
        self.sms_store = []

    def add_new_arrive(self, from_number, time_arrived, text_of_SMS):
        self.readed = False
        self.sms_store.append([self.readed, from_number, time_arrived, text_of_SMS])

    def message_count(self):
        return len(self.sms_store)

    def get_unread_indexes(self):
        unread_message = []
        for index in range(len(self.sms_store)):
            unread_message_one = self.sms_store[index]
            if unread_message_one[0] is False:
                unread_message.append(index)
        return unread_message

    def get_message(self, index):
        if 0 <= index < len(self.sms_store):
            lists = self.sms_store[index]
            lists[0] = True
            self.sms_store[index] = lists
            return lists[1], lists[2], lists[3]

    def delete(self, index):
        if 0 <= index < len(self.sms_store):
            del self.sms_store[index]

    def clear(self):
        self.sms_store.clear()


my_inbox = SMS_store()
my_inbox.add_new_arrive(123, str(datetime.datetime.now().today()), "hola mundo")
my_inbox.add_new_arrive(123, str(datetime.datetime.now().today()), "hola mundo 1")
my_inbox.add_new_arrive(123, str(datetime.datetime.now().today()), "hola mundo 2")
my_inbox.add_new_arrive(123, str(datetime.datetime.now().today()), "hola mundo 3")
print(my_inbox.sms_store)
print("cantidad de mensajes que tienes: ", my_inbox.message_count())
print("mensaje no leidos: ", my_inbox.get_unread_indexes())
print(my_inbox.get_message(2))
my_inbox.delete(1)
print("despues de eliminar: ", my_inbox.sms_store.__len__())
my_inbox.clear()
print("despues de limpuar: ", my_inbox.sms_store.__len__())
