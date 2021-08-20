import heapq
from operator import itemgetter


class HardDisk:
    def __init__(self):
        self.current_job = None
        self.scheduled = []
        self.finished = []

    def is_running(self):
        return self.current_job is not None or len(self.scheduled) > 0

    def put(self, jobs):
        for job in jobs:
            heapq.heappush(self.scheduled, (job[1], job))

    def process(self):
        if self.current_job is None:
            if self.scheduled:
                _, self.current_job = heapq.heappop(self.scheduled)
            else:
                return

        self.current_job[1] -= 1

        if self.current_job[1] == 0:
            self.current_job.append(current_time + 1)
            self.finished.append(self.current_job)
            self.current_job = None

    @property
    def process_average(self):
        return sum(j[2] - j[0] for j in self.finished) // len(self.finished)


global current_time


def solution(jobs):
    # 요청 시간, 작업 시간
    jobs.sort(key=itemgetter(0))

    hard_disk = HardDisk()

    global current_time
    current_time = 0

    while hard_disk.is_running() or len(jobs) > 0:
        requested_jobs = list(filter(lambda j: j[0] <= current_time, jobs))
        jobs = list(filter(lambda j: j[0] > current_time, jobs))

        hard_disk.put(requested_jobs)
        hard_disk.process()

        current_time += 1

    return hard_disk.process_average

