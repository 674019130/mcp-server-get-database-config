class DatabaseConfig:
    def __init__(self, name, host, port, username, password, database, db_system = "postgresql"):
        self.name = name
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.db_system = db_system

    def parse_from_json(self, json_data):
        self.name = json_data["name"]
        self.host = json_data["host"]
        self.port = json_data["port"]
        self.username = json_data["username"]
        self.password = json_data["password"]
        self.database = json_data["database"]
        self.db_system = json_data["db_system"] if "db_system" in json_data else "postgresql"

    def __str__(self):
        return f"DatabaseConfig(name={self.name}, host={self.host}, port={self.port}, username={self.username}, password={self.password}, database={self.database}, db_system={self.db_system})"

    def __repr__(self):
        return self.__str__()
