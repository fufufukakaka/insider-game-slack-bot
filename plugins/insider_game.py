class Game(object):
    def __init__(self):
        self.member_list = []
        self.insider = ""
        self.game_master = ""
        self.observer_list = []

    def add_member(self,user_name):
        self.member_list.append(user_name)

    def return_count_members(self):
        count = len(self.member_list)
        return count
