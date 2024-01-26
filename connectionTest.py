import logging
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.exceptions import ConnectionException

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger()

PLC_IP = 'PLC_IP_ADDRESS'  # Replace with your PLC's IP address
PLC_PORT = 502  # Replace with your PLC's port if different
client = ModbusClient(PLC_IP, port=PLC_PORT)

try:
    connection = client.connect()
    if connection:
        logger.info("Connected to PLC at IP: %s", PLC_IP)
    else:
        logger.error("Failed to connect to PLC at IP: %s", PLC_IP)
except ConnectionException as ce:
    logger.error("Connection error: %s", ce)

try:
    START_ADDRESS = 0  # Replace with your start address
    COUNT = 10  # Number of registers to read
    result = client.read_holding_registers(START_ADDRESS, COUNT)
    if result.isError():
        logger.error("Error reading registers: %s", result)
    else:
        logger.info("Register values: %s", result.registers)
except Exception as e:
    logger.error("Modbus operation error: %s", e)

client.close()
logger.info("Connection closed")