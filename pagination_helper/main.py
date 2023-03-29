import math


class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return math.ceil(len(self.collection) / self.items_per_page)

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index > self.page_count()-1:
            return -1
        else:
            count = 0
            end_index = (page_index + 1) * self.items_per_page
            start_index = end_index - self.items_per_page
            if end_index > len(self.collection):
                end_index = len(self.collection)
            for i in range(start_index, end_index):
                count += 1
            return count

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index < 0:
            return -1
        if item_index > self.item_count() -1 or self.item_count() == 0:
            return -1
        else:
            return math.floor(item_index / self.items_per_page)


if __name__ == '__main__':
    helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)

    print(helper.page_index(6))

