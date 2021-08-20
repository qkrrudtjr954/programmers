class Truck:
    def __init__(self, weight, time):
        self.weight = weight
        self.time = time

    def go(self):
        self.time -= 1

    def is_reach_the_end(self):
        return self.time == 0


class Bridge:
    def __init__(self, length, weight):
        self.length = length
        self.weight = weight
        self.trucks = list()

    def put(self, truck):
        self.trucks.insert(0, truck)

    def get(self):
        self.trucks.pop()

    def move_trucks(self):
        for t in self.trucks:
            t.go()

    @property
    def total_weight(self):
        return sum(t.weight for t in self.trucks)

    def is_addable(self, truck_weight):
        return len(self.trucks) + 1 <= self.length and self.total_weight + truck_weight <= self.weight

def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(length=bridge_length, weight=weight)

    truck_weights.reverse()
    bridge.put(Truck(weight=truck_weights.pop(), time=bridge_length))

    answer = 1

    while bridge.trucks:
        answer += 1

        bridge.move_trucks()

        if bridge.trucks[-1].is_reach_the_end():
            bridge.get()

        if not truck_weights:
            continue

        if bridge.is_addable(truck_weights[-1]):
            bridge.put(Truck(weight=truck_weights.pop(), time=bridge_length))

    return answer
