class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):

        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stat()

        #Start Alien Invasion in an active state.
        self.game_active = False


    def reset_stat(self):
        """Initialize statistics that can change during the game."""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        