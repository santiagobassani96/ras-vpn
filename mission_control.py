from ras_vpn.vpn_tools import connect
import logging
logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="log.txt",
)


if __name__ == "__main__":
    connect()
