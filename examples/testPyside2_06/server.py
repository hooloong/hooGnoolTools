import win32file
import win32pipe
import os
PIPE_NAME = r'\\.\pipe\test_pipe'
PIPE_BUFFER_SIZE = 65535
stop = False
while True:
    named_pipe = win32pipe.CreateNamedPipe(PIPE_NAME,
                                           win32pipe.PIPE_ACCESS_DUPLEX,
                                           win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_WAIT | win32pipe.PIPE_READMODE_MESSAGE,
                                           win32pipe.PIPE_UNLIMITED_INSTANCES,
                                           PIPE_BUFFER_SIZE,
                                           PIPE_BUFFER_SIZE, 500, None)
    if stop is False:
        os.popen(r"python client.py")
        stop = True
    try:
        while True:
            try:
                win32pipe.ConnectNamedPipe(named_pipe, None)
                data = win32file.ReadFile(named_pipe, PIPE_BUFFER_SIZE, None)

                if data is None or len(data) < 1:
                    continue

                print( 'receive msg:', data)
            except BaseException as e:
                print ( "exception:", e)
                break
    finally:
        try:
            win32pipe.DisconnectNamedPipe(named_pipe)
        except:
            pass