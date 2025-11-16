import json
import pathlib
import typing


def get_mountain(country: str)-> typing.Optional[list[dict]]:
    BASE_PATH = '/home/surister/PycharmProjects/mcp-copenhagen/mountains/data'

    for mountain_raw in pathlib.Path(BASE_PATH).iterdir():
        name, extension = mountain_raw.name.split('.')
        if country.lower() == name and extension == 'json':
            return json.loads(mountain_raw.read_bytes())
    return None
