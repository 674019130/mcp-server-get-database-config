import json
from schema.database import DatabaseConfig
from mcp.server.fastmcp import FastMCP

mcp = FastMCP()


@mcp.tool()
def get_all_database_config() -> list[DatabaseConfig]:
    """
    return all database config
    Returns:
        all database config
    """
    with open("database.json", "r") as f:
        database_config = json.load(f)
    return [DatabaseConfig(**config) for config in database_config.values()]


@mcp.tool()
def get_all_database_name() -> list[str]:
    """
    return all database name
    Returns:
        all database name
    """
    database_config = get_all_database_config()
    return [database_config.name for database_config in database_config]


@mcp.tool()
def get_database_config_by_name(database_name: str) -> DatabaseConfig:
    """
    return database config by database name
    Args:
        database_name: database name
    Returns:
        database config
    """
    database_config = get_all_database_config()
    return database_config[database_name]


def main():
    mcp.run(transport='stdio')


if __name__ == "__main__":
    main()
