class FiniteStateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []

    def add_state(self, name, action, end_state=0):
        name = name.upper()
        self.handlers[name.upper()] = action
        if end_state:
            self.endStates.append(name)

    def set_start(self, name):
        self.startState = name.upper()

    def run(self, task):
        handler = self.handlers[self.startState]
        while True:
            (newState, task) = handler(task)
            if newState.upper() in self.endStates:
                print("reached ", newState)
                break
            else:
                handler = self.handlers[newState.upper()]
