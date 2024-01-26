from pymodbus.client.sync import ModbusTcpClient as ModbusClient

PLC_IP = 'PLC_IP_ADDRESS'  # Replace with the actual IP address of the PLC
START_REGISTER = 0  # Replace with the actual register designated for start command
START_COMMAND = 1  # The value that signifies a 'start' command

client = ModbusClient(PLC_IP, port=502)
client.connect()

client.write_register(START_REGISTER, START_COMMAND)

client.close()