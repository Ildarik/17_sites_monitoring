# Sites Monitoring Utility

Load from text file urls list and check status_code and expiration_date


# How to Install
```bash
pip install -r requirements.txt
```

# How to Run
```bash
python3 check_sites_health.py urls.txt
```

# Example output
```bash

http://sports.ru
Отвечает на запрос статусом HTTP 200:  True
Доменное имя проплачено как минимум на 1 месяц вперед:  True

http://yandex.ru
Отвечает на запрос статусом HTTP 200:  True
Доменное имя проплачено как минимум на 1 месяц вперед:  True

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
