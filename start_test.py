from pymodbus.client.sync import ModbusTcpClient as ModbusClient

client = ModbusClient('PLC_IP_ADDRESS', port=502)
client.connect()

START_REGISTER = 40001  # Modbus register to start the program
START_COMMAND = 1  # The value that signifies a 'start' command
client.write_register(START_REGISTER - 40001, START_COMMAND)  # Adjust register address as needed

client.close()