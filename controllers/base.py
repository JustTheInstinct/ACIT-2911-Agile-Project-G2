import pygame


class PygameController:
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
