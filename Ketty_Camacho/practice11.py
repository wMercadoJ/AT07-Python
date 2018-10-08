class SmsStore:

    def __init__(self):
        self.arrive = []

    def add_new_arriva(self, from_name, time_arrive, test_of_sms):
        self.arrive.append([False, from_name, time_arrive, test_of_sms])

    def message_count(self):
        return len(self.arrive)

    def get_unread_indexes(self):
        arrive_01 = []
        for i in range(len(self.arrive)):
            if not self.arrive[i][0]:
                arrive_01.append(i)
        print(arrive_01)

    def get_message(self, index):
        for i in range(len(self.arrive)):
            if i == index:
                self.arrive[i][0] = True
                return self.arrive[i]
        return None

    def delete(self, index):
        del self.arrive[index]
        print(self.arrive)

    def clean(self):
        return self.arrive.clear()


my_inbox = SmsStore()
my_inbox.add_new_arriva(725363, '6:40', "llllll")
my_inbox.add_new_arriva(72211225336, '6:40', "llllll")
my_inbox.add_new_arriva(725336, '6:40', "llllll")
print(my_inbox.arrive)
print(my_inbox.message_count())
my_inbox.get_unread_indexes()
my_inbox.get_message(1)
my_inbox.delete(1)
print(my_inbox.clean())
