class Run:
    def __init__(self) -> None:
        self.run = True
    def stop(self):
        self.run = False
    def getRun(self):
        return self.run