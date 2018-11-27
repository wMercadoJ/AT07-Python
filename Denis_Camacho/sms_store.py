import time


class SMS_store:
    def __init__(self):
        self.arrival = []  # creates a new store

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        self.arrival.append([False, from_number, time_arrived, text_of_SMS])

    def message_count(self):
        return self.arrival.__len__()

    def get_unread_indexes(self):
        list_not_view = []
        for i in range(0, len(self.arrival)):
            if not self.arrival[i][0]:
                list_not_view.append(i)
        return list_not_view

    def get_message(self, i):
        if i < len(self.arrival):
            self.arrival[i][0] = True
            return self.arrival[i]
        else:
            return "None"

    def delete(self, i):
        if i < len(self.arrival):
            self.arrival.__delitem__(i)
            return self.arrival
        else:
            return "None"

    def clear(self):
        self.arrival = []


times = time.strftime("%c")
sms_store = SMS_store()
sms_store.add_new_arrival('69489750', times, 'hello word')
sms_store.add_new_arrival('69489750', times, 'second message')
sms_store.add_new_arrival('69489750', times, 'hello word')
sms_store.add_new_arrival('69489750', times, 'second message')
sms_store.add_new_arrival('69489750', times, 'hello word')
sms_store.add_new_arrival('69489750', times, 'second message')

print(sms_store.arrival)
print("message total " + str(sms_store.message_count()))
print(sms_store.get_unread_indexes())
print(sms_store.get_message(2))
print(sms_store.get_unread_indexes())
print(sms_store.delete(0))
sms_store.clear()
print(sms_store.arrival)
