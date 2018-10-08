import time
import datetime


class SMS_store:
    def __init__(self):
        self.arrival = []  # creat a new sms store

    def add_new_arrival(self, from_number, time_arrival, text_of_SMS):
        self.arrival.append([False, from_number, time_arrival, text_of_SMS])

    def message_count(self):
        return self.arrival.__len__()

    def get_unread_indexed(self):
        list_not_viewed = []
        for i in range(len(self.arrival)):
            if self.arrival[i][0] == False:
                list_not_viewed.append(i)
        return list_not_viewed

    def get_messages(self, index):
        if index < len(self.arrival):
            list_messages = self.arrival[index]
            list_messages[0] = True
            return list_messages[1:]

    def delete_message(self, index):
        return self.arrival.pop(index)

    def clear_all_sms(self):
        return self.arrival.clear()


ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
sms = SMS_store()

sms.add_new_arrival('11111111', date, 'hello')
sms.add_new_arrival('22222222', date, 'hello my friend')
sms.add_new_arrival('33333333', date, 'hello how are you?')

print ("inbox messages:", sms.arrival)
print ("number of messages:", sms.message_count())
print ("Unread Messages:", sms.get_unread_indexed())
print("message:", sms.get_messages(2))

sms.delete_message(1)
print ("number of messages:", sms.message_count())

print ("message was deleted:", sms.arrival)
sms.clear_all_sms()
print ("empty inbox:", sms.arrival)
