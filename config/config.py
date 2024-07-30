import os
import configparser

config = configparser.ConfigParser()
config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
config.read(config_file_path)


def get_server_config():
    return {
        'host': config.get('server', 'host'),
        'port': config.getint('server', 'port')
    }


def get_database_config():
    return {
        'user': config.get('database', 'user'),
        'password': config.get('database', 'password'),
        'host': config.get('database', 'host'),
        'port': config.getint('database', 'port'),
        'database': config.get('database', 'database')
    }


def get_kafka_config():
    return {
        'host': config.get('kafka', 'bootstrap_host'),
        'port': config.get('kafka', 'bootstrap_port'),
        'topic': config.get('kafka', 'topic')
    }
    
    
def get_email_config():
    return {
        'service_email': config.get('email', 'service_email'),
        'service_password': config.get('email', 'service_password'),
        'smtp_host': config.get('email', 'smtp_host'),
        'smtp_port': config.getint('email', 'smtp_port')
    }