class Action:
    pass

# When hitting the esc key to exit the game
class EscapeAction(Action):
    pass

# Describe our player moving around
class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy