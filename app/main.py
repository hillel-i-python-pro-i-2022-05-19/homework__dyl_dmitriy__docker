import logging
import pathlib
from typing import Final

import ulid
from faker import Faker

faker = Faker()

ROOT_PATH: Final[pathlib.Path] = pathlib.Path(__file__).parents[1]
OUTPUT_PATH: Final[pathlib.Path] = ROOT_PATH.joinpath('output')


def generate_massege() -> str:
    return f"Hi!, {faker.unique.first_name()}"


def generate_file():
    temp_path = OUTPUT_PATH.joinpath(f'{ulid.new()}.txt')
    temp_path.write_text(generate_message())

    logging.info(f'File generated at path: "{temp_path}"')
