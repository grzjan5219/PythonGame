import pygame

class Settings():
    def __init__(self):
        #inicjalizacja
        self.clock = pygame.time.Clock()
        self.speed = 3
        self.tps = 60.0
        self.deltaTime = 0.0
        self.snake = Snake(self)
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.gameBoard = Board(30, 17, self) #narazie druga liczba musi być nieparzysta

        pygame.display.set_caption('Menu ')

    def rozpoczecie(self):
        currentKey = "q"
        #self.gameBoard.draw()

        while True:
            # obługa zdarzeń
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
