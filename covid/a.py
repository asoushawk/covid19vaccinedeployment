from datetime import datetime, timedelta


yesterday = datetime.now() - timedelta(1)



yesterday = datetime.strftime(yesterday, '%Y-%m-%d')

print(yesterday)

