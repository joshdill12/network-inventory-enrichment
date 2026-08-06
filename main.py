import logging
from logger import setup_logger

setup_logger()
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    main()

def main():
    print("placeholder")