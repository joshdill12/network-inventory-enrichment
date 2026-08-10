import logging
import os
from multiprocessing import connection
from netmiko import ConnectHandler
from netmiko.exceptions import (NetmikoAuthenticationException, NetmikoTimeoutException)

#environment variable names
USERNAME_ENV= "USERNAME"
PASSWORD_ENV="PASSWORD"

#instantiate's logger
logger = logging.getLogger(__name__)

#establishes SSH connection.
def connect(device):
    logger.info("connecting to %s (%s)", device.hostname, device.ip)

    try:
        connection = ConnectHandler(
                device_type=device.vendor,
                host= device.ip,
                username=os.getenv("USERNAME_ENV"),
                password=os.getenv("PASSWORD_ENV")
            )
        logger.info("successfully connected to %s", device.hostname,)

        return connection


    except NetmikoAuthenticationException:
        logger.error("Authentication failed for %s", device.hostname,)
        raise

    except NetmikoTimeoutException:
        logger.error("Connection timed out for %s", device.hostname)
        raise

#to close SSH session.
def disconnect(device):
    logger.info("Closing SSH connection to %s", device.hostname,)

    connection.disconnect()

    logger.info("SSH connection closed")