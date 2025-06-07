module.exports = {
    apps: [
        {
            name: 'main_service',
            script: '/home/srv6/elitteradio/.venv/bin/gunicorn -c config/gunicorn.py config.wsgi:application',
            cron_restart: '0',
            merge_logs: true,
            autorestart: false,
            log_file: "logs/top.log",
            log_date_format: "DD-MM-YYYY HH:mm Z",
            append_env_to_name: true,
            watch: false,
            max_memory_restart: '5G',
        },
        {
            name: 'radios_listeners',
            script: '/home/srv6/elitteradio/.venv/bin/python radios_listeners_engine.py',
            cron_restart: '0',
            log_file: "logs/radio_listeners.log",
            log_date_format: "DD-MM-YYYY HH:mm Z",
            max_memory_restart: '5G',
        },
    ]
};