class History(object):
    def __init__(self):
        self._commands = list()

    def execute(self, command):
        self._commands.append(command)
        command.execute()

    def undo(self):
        self._commands.pop().undo()

class MoveUnit(object):
    def __init__(self, data):
        # data: list{'Map':PandasDataframe, 'MoveCommand':String } 
        # // MoveCommand format: "A1(GFP:12)-B2", "A1-B2"
        self.data = data

    def execute(self):
        self.data['Map'][1][1] += self.data['MoveCommand']

    def undo(self):
        self.data['Map'][1][1] -= self.data['MoveCommand']



# history = History()
# history.execute(RenameFileCommand('docs/cv.doc', 'docs/cv-en.doc'))
# history.execute(RenameFileCommand('docs/cv1.doc', 'docs/cv-bg.doc'))
# history.undo()
# history.undo()