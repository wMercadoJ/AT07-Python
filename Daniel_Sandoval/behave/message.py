# Create a new class, SMS_store. The class will instantiate SMS_store objects,
# similar to an inbox or outbox on a cellphone:


class SMS_Store:

    def __init__(self):
        self.arrival = []

    # Makes new SMS tuple, inserts it after other messages
    # in the store. When creating this message, its
    # has_been_viewed status is set False.
    def add_new_arrival(self, status, from_number, time_arrived, text_of_SMS):
        self.arrival.append([status, from_number, time_arrived, text_of_SMS])

    # Returns the number of sms messages in my_inbox
    def message_count(self):
        print (len(self.arrival))

    # Returns list of indexes of all not-yet-viewed SMS messages
    def get_unread_indexes(self):
        list_view = []
        for ini in range(len(self.arrival)):
            if self.arrival[ini][0] == False:
                list_view.append(ini)
        print (list_view)

    # Return (from_number, time_arrived, text_of_sms) for message[i]
    # Also change its state to "has been viewed".
    # If there is no message at position i, return None
    def get_message(self, i):
        if i < len(self.arrival):
            self.arrival[i][0] = True
            print (self.arrival[i])
        else:
            print ("None")

    # Return (from_number, time_arrived, text_of_sms) for message[i]
    # Also change its state to "has been viewed".
    # If there is no message at position i, return None
    def delete_message(self, i):
        if i < len(self.arrival):
            self.arrival.pop(i)
            print (self.arrival[i])
        else:
            print ("None")

    # Delete the message at index i my_def clear()
    # Delete all messages from inbox
    def clear_message(self):
        self.arrival.clear()
        # while len(self.arrival) > 0:
        #     self.arrival.pop(len(self.arrival) - 1)
        print (self.arrival)


test = SMS_Store()
test.add_new_arrival(False, 45121, "10:11", "first message")
test.add_new_arrival(False, 86320, "2:45", "Second message")
test.add_new_arrival(False, 87456, "1:21", "third message")
test.add_new_arrival(False, 95123, "12:5", "forth message")

test.message_count()

test.get_unread_indexes()

test.get_message(0)

print(test.arrival)

test.delete_message(2)

test.clear_message()

print (test.arrival)