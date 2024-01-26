from pymodbus.client.sync import ModbusTcpClient as ModbusClient

PLC_IP = 'PLC_IP_ADDRESS'  # Replace with the actual IP address of the PLC
REGISTER_ADDRESS = 43132  # The register address to write to
VALUE_TO_WRITE = 1  # The value to write to the register, often 1 or 0 to trigger an action

client = ModbusClient(PLC_IP, port=502)
client.connect()

# Write to the register
client.write_register(REGISTER_ADDRESS - 40001, VALUE_TO_WRITE)  # Adjust the address as per Modbus standard

client.close()