from engine.db.json_save_load.game_database import GameDatabase


class GameSave(GameDatabase):
    def __init__(self, cities=None, countries=None, leagues=None, league_classes=None, persons=None, riders=None,
                 stadiums=None, teams=None, tracks=None, game_state=None):
        self.game_state = game_state
        GameDatabase.__init__(self, cities, countries, leagues, league_classes, persons, riders, stadiums, teams,
                              tracks)
