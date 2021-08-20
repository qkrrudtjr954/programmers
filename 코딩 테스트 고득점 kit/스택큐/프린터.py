class PrintItem:
    def __init__(self, priority, location):
        self.priority = priority
        self.location = location

class Printer:
    def __init__(self, items):
        self.queue = items

    def put(self, item):
        self.queue.append(item)

    def get(self):
        return self.queue.pop(0)

    def has_more_priority_than(self, priority):
        return any(item.priority > priority for item in self.queue)

def solution(priorities, location):
    printer = Printer(items=[PrintItem(location=idx, priority=p) for idx, p in enumerate(priorities)])

    answer = 0

    while True:
        print_item = printer.get()

        if printer.has_more_priority_than(print_item.priority):
            printer.put(print_item)
            continue

        answer += 1

        if print_item.location == location:
            return answer

    return answer
