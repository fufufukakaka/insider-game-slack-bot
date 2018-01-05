
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
from slackbot import slackclient

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from insider_game import Game

this_insider_game = Game()

@respond_to('インサイダーゲームを始めたい')
def init_game(message):
    this_insider_game = Game()
    message.reply('了解しました。参加者は私にメンションをしてください。')     # メンション
    message.react('+1')     # リアクション

@respond_to('参加します')
def accept_member(message):
    user_name = message.channel._client.users[message.body['user']]['name']
    this_insider_game.add_member(user_name)
    message.reply('{}の参加を受け付けました。'.format(user_name))     # メンション
    message.send("現在の参加人数は{}人です。".format(this_insider_game.return_count_members()))
    message.react('nerd_face')     # リアクション
