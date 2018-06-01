import hexdump
from pytun import TunTapDevice, IFF_TAP

tun = TunTapDevice(name='rfc6214')

with open ("captured_in.hex", "r") as the_file:
	hex=the_file.readline()

buf = hexdump.dehex(hex)

tun.write(buf)
