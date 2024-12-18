import pandas as pd

class Job:
    def __init__(self, name, duration, start_time, priority):
        self.name = name
        self.duration = duration
        self.start_time = start_time
        self.priority = priority
        self.completion_time = 0
        self.response_time = 0
        self.waiting_time = 0

    def __repr__(self):
        return f"Job({self.name}, Duration: {self.duration}, Start: {self.start_time}, Priority: {self.priority})"


class Scheduler:
    def __init__(self, jobs, dispatch_latency=0):
        self.jobs = jobs
        self.dispatch_latency = dispatch_latency

    def fcfs(self):
        current_time = 0
        for job in sorted(self.jobs, key=lambda x: x.start_time):
            if current_time < job.start_time:
                current_time = job.start_time
            current_time += self.dispatch_latency  # Aggiungi latenza di dispatch
            job.waiting_time = current_time - job.start_time
            job.response_time = job.waiting_time
            current_time += job.duration
            job.completion_time = current_time

    def sjf(self):
        current_time = 0
        remaining_jobs = sorted(self.jobs, key=lambda x: (x.start_time, x.duration))
        
        while remaining_jobs:
            # Filtra i job che possono essere eseguiti
            available_jobs = [job for job in remaining_jobs if job.start_time <= current_time]
            if available_jobs:
                # Scegli il job con la durata più breve
                job = min(available_jobs, key=lambda x: x.duration)
                remaining_jobs.remove(job)
                
                if current_time < job.start_time:
                    current_time = job.start_time
                current_time += self.dispatch_latency  # Aggiungi latenza di dispatch
                job.waiting_time = current_time - job.start_time
                job.response_time = job.waiting_time
                current_time += job.duration
                job.completion_time = current_time
            else:
                # Se non ci sono job disponibili, avanza il tempo
                current_time += 1

    def display_results(self):
        for job in self.jobs:
            print(f"{job.name}: Completion Time: {job.completion_time}, "
                  f"Response Time: {job.response_time}, Waiting Time: {job.waiting_time}")


# Esempio di utilizzo
data = {
    'Job': ['P1', 'P2', 'P3', 'P4'],
    'Duration': [15, 21, 5, 8],
    'Start Time': [0, 5, 9, 10],
    'Priority': [2, 1, 3, 1]
}

df = pd.DataFrame(data)
jobs = [Job(row['Job'], row['Duration'], row['Start Time'], row['Priority']) for index, row in df.iterrows()]

scheduler = Scheduler(jobs, dispatch_latency=2)

print("FCFS Scheduling:")
scheduler.fcfs()
scheduler.display_results()

# Resettare i job per il SJF
jobs = [Job(row['Job'], row['Duration'], row['Start Time'], row['Priority']) for index, row in df.iterrows()]
scheduler = Scheduler(jobs, dispatch_latency=2)

print("\nSJF Scheduling:")
scheduler.sjf()
scheduler.display_results()
