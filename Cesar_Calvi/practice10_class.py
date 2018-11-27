import datetime


class SMS_store:
    def __init__(self):
        self.inbox = []
        self.BEEN_VIEWED = 0
        self.FROM = 1
        self.TIME = 2
        self.TEXT = 3

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        has_been_viewed = False
        self.inbox.append((has_been_viewed, from_number, time_arrived, text_of_SMS))

    def add_new_arrival_time_stamp(self, from_number, text_of_SMS):
        has_been_viewed = False
        self.inbox.append((has_been_viewed, from_number, datetime.datetime.now(), text_of_SMS))


    def message_count(self):
        return len(self.inbox)

    def get_unread_indexes(self):
        notRead = []
        for i in range(0, len(self.inbox)):
            if self.inbox[i][self.BEEN_VIEWED] == False:
                notRead.append(i)
        return notRead

    def get_message(self, i):
        if len(self.inbox) > i:
            self.inbox[i] = (True, self.inbox[i][self.FROM], self.inbox[i][self.TIME], self.inbox[i][self.TEXT])
            msg = self.inbox[i]
            if msg[self.TEXT] == "":
                return None
            else:
                return msg[self.FROM], msg[self.TIME], msg[self.TEXT]
        else:
            return None

    def delete(self, i):
        if len(self.inbox) >= i:
            self.inbox.pop(i)

    def clear(self):
        self.inbox = []


if __name__ == '__main__':
    sms = SMS_store()
    sms.add_new_arrival()
