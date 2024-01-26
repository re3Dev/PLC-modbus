from pymodbus.client.sync import ModbusTcpClient as ModbusClient

client = ModbusClient('PLC_IP_ADDRESS', port=502)
connection = client.connect()
if connection:
    print("Connected to PLC")
else:
    print("Failed to connect")

result = client.read_holding_registers(START_ADDRESS, COUNT)
if result.isError():
    print("Error reading")
else:
    print("Register values:", result.registers)

client.close()