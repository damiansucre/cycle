from turtle import color
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle2(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _cycle_color : Color of the cycle.
    """
    def __init__(self, color):
        super().__init__()
        self._cycle_color = color
        self._segments2 = []
        self._prepare_body()

    def get_segments(self):
        return self._segments2

    def move_next(self):
        # move all segments
        for segment in self._segments2:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments2) - 1, 0, -1):
            trailing = self._segments2[i]
            previous = self._segments2[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments2[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments2[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            #segment.set_color(constants.GREEN)
            segment.set_color(self._cycle_color)
            self._segments2.append(segment)

    def turn_head(self, velocity):
        self._segments2[0].set_velocity(velocity)
    
    def _prepare_body(self):
        x = 0.0
        y = 0.0

        if self._cycle_color == constants.GREEN:
            x = int(constants.MAX_X /20)
            y = int(constants.MAX_Y /20)
        elif self._cycle_color == constants.GREEN:
            x = int(constants.MAX_X /2)
            y = int(constants.MAX_Y /2)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "@" if i == 0 else "#"
            #color = constants.YELLOW if i == 0 else constants.GREEN
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(self._cycle_color)
            self._segments2.append(segment)