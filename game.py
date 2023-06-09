import pygame
from windows import Window


class Game:
    game: 'Game' = None

    def __init__(self):
        if Game.game is None:
            Game.game = self

        pygame.init()
        pygame.font.init()

        WIDTH = 1280
        HEIGHT = 800
        GAME_TITLE = "Футбол головой на двоих"

        # добавление возможности изменить размер окна
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

        gameIcon = pygame.image.load("./assets/images/ball.png")
        pygame.display.set_icon(gameIcon)

        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()
        self.current_view: Window = Window()



    @staticmethod
    def set_current_view(view):
        Game.game.current_view = view

    def run(self):
        MAXWIDTH, MAXHEIGHT = 1920, 1080  # нужно исходить из размера монитора
        MINWIDTH, MINHEIGHT = 1200, 800

        from windows.Menu import MenuWindow
        self.current_view = MenuWindow()
        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.VIDEORESIZE:

                    width = min(MAXWIDTH, max(MINWIDTH, event.w))
                    height = min(MAXHEIGHT, max(MINHEIGHT, event.h))

                    if (width, height) != event.size:
                        self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

            # Обновление текущего окна
            self.current_view.event_loop(events)
            self.current_view.update()
            self.current_view.draw(self.screen)

            self.current_view.event_sys(events)
            self.current_view.update_sys()
            self.current_view.draw_sys(self.screen)

            # Эти две строки должны быть в самом конце цикла
            pygame.display.flip()
            self.clock.tick(30)
            # ---------------------------

            #pygame.display.update()

        pygame.quit()
