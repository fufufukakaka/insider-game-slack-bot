import configparser
import os,sys

INI_FILE = "credential.ini"
ini = configparser.SafeConfigParser()
if os.path.exists(INI_FILE):
    ini.read(INI_FILE, encoding='utf8')
else:
    sys.stderr.write(INI_FILE + " が見つかりません")
    sys.exit(2)

# botアカウントのトークンを指定
API_TOKEN = ini.get('credential', 'API_TOKEN')

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "何言ってんだこいつ"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']
