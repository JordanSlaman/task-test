import hashlib, datetime
from task_manager import  Task, TaskManager

class CustomTaskManager(TaskManager):

    def __init__(self):
        self._tasks = dict()

    def generate_key(self,task):
        m = hashlib.md5()
        m.update(task.name + task.created)
        return m.hexdigest()

    def import_task(self,task):
        self._tasks[self.generate_key(task)] = task
        print('task {name} created'.format(name=task.name))

    def complete_tasks(self):
        for task in self._tasks.items():
            if not task[1].is_completed:
                task[1].complete()
                print('task {name} completed, ccn: {value}'.format(name=task[1].name,value=task[1].value))

    def remove_task(self,key):
        tmp_name = self._tasks[key].name
        del self._tasks[key]
        print('task {name} removed'.format(name=tmp_name))

    def remove_tasks(self):
        self._tasks.clear()
        print('all tasks removed')

    def lookup_tasks(self,name):
        results_subset = dict()
        for task in self._tasks.items():
            if task[1].name is name:
                results_subset[task[0]] = task[1]
        return results_subset

    def killall(self, name):
        for task in self.lookup_tasks(name).items():
            self.remove_task(task[0])

class CustomTask(Task):

    def __init__(self, name):
        self._created = unicode(datetime.datetime.now())
        self._name = name
        self._value = None
        self._completed = False

    def complete(self):
        self._completed = True
        self._value = self.name.lower().count('ccn')

    @property
    def created(self):
        return self._created


if __name__ == "__main__":
    task_manager = CustomTaskManager()

    new_tasks = ['!!nZ@xr>492CCN;SDRC2#6CcN_$5UcCNq]*m44AhW`',
                'g}~x?C*n9K|LccN_YEL@<=44jkc.dB-v{!#;7*[[',
                'ekCcN,h9=!B46)j6acCN;`n68M+2ZR2CCn^:CUw']
    for task in new_tasks:
        task_manager.import_task(CustomTask(task))

    task_manager.complete_tasks()

    #invokes the remove_task method by name as opposed to it's key (which is time-sensitive to avoid conflict)
    task_manager.killall('g}~x?C*n9K|LccN_YEL@<=44jkc.dB-v{!#;7*[[')

    task_manager.import_task(CustomTask('>.`8tCcn{xsS3sa!G@{cCn(w},U+s)**sACc]NAn#'))
    task_manager.complete_tasks()

    task_manager.remove_tasks()