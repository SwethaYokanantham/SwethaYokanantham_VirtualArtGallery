import configparser

class PropertyUtil:
    @staticmethod
    def getPropertyString(property_file_path: str) -> str:
        config = configparser.ConfigParser()
        config.read(property_file_path)

        hostname = config.get('DATABASE', 'hostname')
        dbname = config.get('DATABASE', 'dbname')
        username = config.get('DATABASE', 'username')
        password = config.get('DATABASE', 'password')

        connection_string = f"host={hostname} dbname={dbname} user={username} password={password} port={port}"

        return connection_string
