import pygame


class PygameController:
    """This class defines a private method.

    The controllers inherit from this class, which allows them to run
    a Pygame loop by just calling this method.

    It returns when the user clicks the "close" button in the window,
    or press the Escape key, or clicks the mouse.

    WARNING: this method has bugs, or let's say, a less-than-optimal
    implementation. Try to close the window when in the shop: it will return
    to the main screen instead of quitting the game.

    You should definitely improve it.
    """

    def _run_loop(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            clock.tick(30)
            for event in pygame.event.get():
                # Invoked close from the OS
                if event.type == pygame.locals.QUIT:
                    return False
                # Pressed a key - is it Escape?
                elif event.type == pygame.locals.KEYDOWN:
                    if event.key == pygame.locals.K_ESCAPE:
                        return False
                # Clicked the mouse
                elif event.type == pygame.locals.MOUSEBUTTONDOWN:
                    return event.pos
