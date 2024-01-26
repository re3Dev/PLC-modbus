from pymodbus.client.sync import ModbusTcpClient as ModbusClient

PLC_IP = 'PLC_IP_ADDRESS'  # Replace with the actual IP address of the PLC
COIL_START_ADDRESS = 10  # Starting address in the PLC
NUMBER_OF_COILS = 43035 - 43008 + 1  # Number of coils you want to read

client = ModbusClient(PLC_IP, port=502)
client.connect()

# Reading coils using function code 01
result = client.read_coils(COIL_START_ADDRESS, NUMBER_OF_COILS)

if not result.isError():
    print("Coil Statuses:", result.bits)
else:
    print("Error reading coils")

client.close()