from pyfirmata2 import Arduino

port = 'COM5'
board = Arduino(port)
print(board)

def Control_Arduino(device_pin: dict, device_state: list):
    # 要輸出的裝置
    board.digital[device_pin["Fan"]].write(device_state[0])
    board.digital[device_pin["Heat"]].write(device_state[1])
    board.digital[device_pin["Water"]].write(device_state[2])
    board.digital[device_pin["Shock"]].write(device_state[3])


def Reset_Arduino(device_pin: dict):
    # 重置所有輸出
    board.digital[device_pin["Fan"]].write(0)
    board.digital[device_pin["Heat"]].write(0)
    board.digital[device_pin["Water"]].write(0)
    board.digital[device_pin["Shock"]].write(0)