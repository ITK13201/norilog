import json

DATA_FILE = 'noring.json'

def save_data(start, finish, memo, created_at):
    """記録データを保存する
    @param start: 乗った駅
    @type start: str
    @param finish: 降りた駅
    @type finish: str
    @param memo: 乗り降りのメモ
    @type memo: str
    @param created_at: 乗り降りの日付
    @type created_at: datetime.datetime
    @return: None 

    """
    try:
        # json モジュールでデータベースを開く
        database = json.load(open(DATA_FILE, mode='r', encoding='utf-8'))
    except FileNotFoundError:
        database = []
    
    database.insert(0, {
        'start': start,
        'finish': finish,
        'memo': memo,
        'created_at': created_at.strftime('%Y-%m-%d %H:%M')
    })

    json.dump(database, open(DATA_FILE, mode='w', encoding='utf-8'), indent=4, ensure_ascii=False)

def load_data():
    try:
        # json モジュールでデータベースを開く
        database = json.load(open(DATA_FILE, mode='r', encoding='utf-8'))
    except FileNotFoundError:
        database = []
    return database