
class ListMerger:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def merge_lists(self):
        self.list1.extend(self.list2)
        return self.list1