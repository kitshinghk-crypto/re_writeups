#!/usr/bin/python3
secret=[0x54, 0x48, 0x4d, 0x63, 0x74, 0x66, 0x2d, 0x4c, 0x34, 0x7]
print("".join([chr(i) for i in secret]))
secret=[i^0x7 for i in secret]
print("".join([chr(i) for i in secret]))
