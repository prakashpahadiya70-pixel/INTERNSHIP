class SharedState:
    def __init__(self, topic):
        self.topic = topic
        self.research = []
        self.analysis = []
        self.criticism = []
        self.final_report = ""