# Ben-Ryder 2019

import code.game.model as model
import code.data as data
import paths


def make(game_name, map_name,  players):
    """ where players = [[name, colour], [name,colour]...]"""
    game = model.Model(game_name, map_name, players)  # creates "blank" game
    data.save(game, paths.gamePath + game_name)
