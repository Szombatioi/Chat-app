class Manager:
    def __init__(self):
        self.run = True
    def getRun(self):
        print(f"get run with {self.run}")
        return self.run
    def stop(event, self):
        self.run = False
        print(f"run set to {self.run}")
