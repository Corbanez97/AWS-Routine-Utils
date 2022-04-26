import json
from executors.staging_exec import StagingExecutor
from executors.download_exec import DownloaderExecutor

class Orchestrator:
    
    def __init__(self, routine_config: dict) -> None:
        self.routine_config = routine_config
    
    def run_executors(self):
        for executor in self.routine_config['executors']:
            self.executor_name = executor
            klass = globals()[self.executor_name]
            self.executor = klass(**self.routine_config['executors'][self.executor_name]['params'])
            self.run_tasks()
            
    def run_tasks(self):
        for task in self.routine_config['executors'][self.executor_name]['tasks']:
            getattr(self.executor, task)()

def main():

    routine_name = input("Enter routine name: ")

    f = f'routines/{routine_name}/routine_config.json'
    print(f)
    with open(f, 'r') as j:
        routine_config = json.loads(j.read())

    orchestrator = Orchestrator(routine_config)
    orchestrator.run_executors()
    
if __name__ == '__main__':
    main()