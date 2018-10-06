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
a = SMS_store()
a.add_new_arrival('69489750', times, 'hello word')
a.add_new_arrival('69489750', times, 'second message')
a.add_new_arrival('69489750', times, 'hello word')
a.add_new_arrival('69489750', times, 'second message')
a.add_new_arrival('69489750', times, 'hello word')
a.add_new_arrival('69489750', times, 'second message')

print a.arrival
print "message total " + str(a.message_count())
print a.get_unread_indexes()
print a.get_message(2)
print a.get_unread_indexes()
print a.delete(0)
a.clear()
print a.arrival
