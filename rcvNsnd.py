import hexdump
from pytun import TunTapDevice, IFF_TAP

tun = TunTapDevice(name='rfc6214')

with open ("captured_in.hex", "r") as the_file:
	hex=the_file.readline()

buf = hexdump.dehex(hex)

tun.write(buf)

buf = tun.read(tun.mtu)
hex = hexdump.dump(buf,2,'')

print(hex)

with open('captured_out.hex', 'w') as the_file:
        the_file.write(hex)
