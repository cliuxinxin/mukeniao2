from orator import DatabaseManager

# 连接数据库
config = {
    'sqlite': {
        'driver': 'sqlite',
        'database': 'fox.db',
    }
}

db = DatabaseManager(config)