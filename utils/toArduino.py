from pyfirmata2 import Arduino

port = 'COM5'
board = Arduino(port)

device_pin = {"Fan": 8, "Heat": 9, "Water": 10, "Vibe": 11}

print(board)

def Control_Arduino(device_state: list):
    # 要輸出的裝置
    board.digital[device_pin["Fan"]].write(device_state[0])
    board.digital[device_pin["Heat"]].write(device_state[1])
    board.digital[device_pin["Water"]].write(device_state[2])
    board.digital[device_pin["Vibe"]].write(device_state[3])


def Reset_Arduino():
    # 重置所有輸出
    board.digital[device_pin["Fan"]].write(0)
    board.digital[device_pin["Heat"]].write(0)
    board.digital[device_pin["Water"]].write(0)
    board.digital[device_pin["Vibe"]].write(0)