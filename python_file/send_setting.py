import struct
import sys

if sys.platform == "win32":
    import os
    import msvcrt

    msvcrt.setmode(sys.stdin.fileno(), os.O_BINARY)
    msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)


def read_thread_func(queue):
    while 1:
        # Read the message length (first 4 bytes).
        # Python 3 compatibility
        if sys.version_info[0] < 3:
            text_length_bytes = sys.stdin.read(4)
        else:
            text_length_bytes = sys.stdin.buffer.read(4)

        if len(text_length_bytes) == 0:
            if queue:
                queue.put(None)
            sys.exit(0)

        # Unpack message length as 4 byte integer.
        text_length = struct.unpack("i", text_length_bytes)[0]

        # Read the text (JSON object) of the message.
        # Python 3 compatibility
        if sys.version_info[0] < 3:
            text = sys.stdin.read(text_length).decode("utf-8")
        else:
            text = sys.stdin.buffer.read(text_length).decode("utf-8")

        f = open('./setting/user_setting.txt', 'w')
        f.write(text)
        f.close()


def main():
    read_thread_func(None)
    sys.exit(0)


if __name__ == '__main__':
    main()
