

class ReadingCompPrompt():

    def __init__(self, prompt: str, answer: str, distractors: List[str]) -> None:
        self.prompt: str = prompt
        self.answer: str = answer
        self.distractors: List[str] = distractors