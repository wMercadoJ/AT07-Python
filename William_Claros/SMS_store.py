# Create a new class, SMS_store. The class will instantiate SMS_store objects, similar to an inbox or outbox on a cellphone:
# With the following methods:
# add_new_arrival(status, from_number, time_arrived, text_of_SMS)
# message_count()
# get_unread_indexes()
# get_message(index)
# delete_message(index)
# clear_all()

class SMS_store:

    def __init__(self):
        self.arrival = []

    def add_new_arrival(self, status, from_number, time_arrived, text_of_SMS):
        self.arrival.append([status, from_number, time_arrived, text_of_SMS])

    def message_count(self):
        len(self.arrival)

    def get_unread_indexes(self):
        list_not_view = []
        for i in range(len(self.arrival)):
            if self.arrival[i][0] == False:
                list_not_view.append(i)
        return list_not_view

    def get_message(self, index):
        for message in self.get_unread_indexes():
            if message == index:
                self.arrival[message][0] = True
                return self.arrival[message][1:]
        return "None"

    def delete_message(self, index):
        del self.arrival[index]

    def clear_all(self):
        self.arrival.clear()

store = SMS_store()
store.add_new_arrival(False, 123456, "13:30", "Hello team, the meeting will be at 14:00")
store.add_new_arrival(False, 456789, "19:30", "The match will be on Sunday in the same court.")
store.add_new_arrival(False, 789123, "05:10", "The meeting was adjourned at 07:30. Do not forget.")
store.add_new_arrival(False, 159267, "03:00", "It's Friday and the body knows it.")
print(store.get_unread_indexes())
store.delete_message(1)
print(store.get_message(1))
store.clear_all()
print(store.get_message(5))
