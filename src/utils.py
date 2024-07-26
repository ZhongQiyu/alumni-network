# utils.py

import yaml

def load_config(file_path):
    """
    Load configuration from a YAML file.
    """
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def connect_to_database(config):
    """
    Connect to the database using the configuration provided.
    """
    import psycopg2
    conn = psycopg2.connect(
        host=config['database']['host'],
        port=config['database']['port'],
        user=config['database']['user'],
        password=config['database']['password'],
        dbname=config['database']['name']
    )
    return conn

def get_api_key(service_name, config):
    """
    Retrieve the API key for a given service.
    """
    return config['api_keys'].get(service_name)

# Example usage
if __name__ == "__main__":
    config = load_config('config.yaml')
    db_connection = connect_to_database(config)
    api_key = get_api_key('service_1', config)
    print(f"API Key for service_1: {api_key}")
