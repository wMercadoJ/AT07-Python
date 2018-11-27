class MSMStore:

    def __init__(self):
        self.arry_list = []
        self.not_yet_viewed = []

    def add_new_arrival(self, from_number, time_arrived, text_of_sms):
        been_viewed = False
        return self.arry_list.append([been_viewed, from_number, time_arrived, text_of_sms])

    def message_count(self):
        return len(self.arry_list)

    def get_unread_index(self):
        for mesagge_value in self.arry_list:
            if not mesagge_value[0]:
                self.not_yet_viewed.append(mesagge_value)
        return self.not_yet_viewed

    def get_message(self, position_message):
        if position_message < len(self.arry_list):
            self.arry_list[position_message][0] = True
            return self.arry_list[position_message]
        return None

    def message_delete(self, position_message):
        if position_message < len(self.arry_list):
            del self.arry_list[position_message]
        return self.arry_list

    def inbox_clear(self):
        self.arry_list.clear()
        return self.arry_list


my_box = MSMStore()
my_box.add_new_arrival("123345", "12:15", "hola como estas")
my_box.add_new_arrival("15878", "13:54", "donde andas")
print(my_box.message_count())
print(my_box.arry_list)
print(my_box.get_unread_index())
print(my_box.get_message(0))
print(my_box.message_delete(0))
print(my_box.inbox_clear())
