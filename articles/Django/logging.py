"""Полезные настройки логирования"""

# Логирование медленных запросов в БД
LOGGING = {
    'filters': {
        'slow_queries': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': lambda record: record.duration > 0.1  # ms
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'filters': ['slow_queries'],
        }
    }
}
