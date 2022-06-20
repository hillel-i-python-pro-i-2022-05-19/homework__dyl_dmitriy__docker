from app.init__logging import init_logging
from app.main import generate_massege


def main():
    print(generate_massege())


if __name__ == '__main__':
    init_logging()
    main()
