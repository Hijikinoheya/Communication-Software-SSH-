import paramiko
import logging.config

logging.config.fileConfig("./conf/logging.conf")
logger = logging.getLogger()

#logger.debug("")
logger.warning("This Version are Beta.")
#logger.error("")
logger.info("Hello! This app version are 0.13")

with paramiko.SSHClient() as client:
    # Server info
    HOSTNAME = ''
    USERNAME = ''
    KEY_FILENAME = ''
    PASSWORD = ''
    LINUX_COMMAND = ''

    # Start SSH
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Mode of passwd
    # If you need, comment out to use this problem.
    # client.connect(hostname=HOSTNAME, port=22, username=USERNAME, password=PASSWORD)

    # SSH keyfile
    client.connect(hostname=HOSTNAME, port=22, username=USERNAME, key_filename=KEY_FILENAME)
jkiuj
    # thrown command
    stdin, stdout, stderr = client.exec_command(LINUX_COMMAND)

    # End of connection.
    for line in stdout:
        print(line, end='')


        