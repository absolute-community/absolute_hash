import absolute_hash
from binascii import unhexlify, hexlify

import unittest

# absolute block #1
# moo@b1:~/.absoluted$ absoluted getblockhash 1
# 000009c40d088ddf1e84187210dc00af1c068e0511e13d9746e679785d1d213b
# moo@b1:~/.dabsoluted$ absoluted getblock 000009c40d088ddf1e84187210dc00af1c068e0511e13d9746e679785d1d213b
# {
#     "hash" : "000009c40d088ddf1e84187210dc00af1c068e0511e13d9746e679785d1d213b",
#     "confirmations" : 387898,
#     "size" : 179,
#     "height" : 1,
#     "version" : 536870912,
#     "merkleroot" : "50e40fb40039d0057f48f0a22d120ea2ea5d4bc2f625beebc8238b78446eeb92",
#     "tx" : [
#         "50e40fb40039d0057f48f0a22d120ea2ea5d4bc2f625beebc8238b78446eeb92"
#     ],
#     "time" : 1518599488,
#     "nonce" : 2009786,
#     "bits" : "1e0ffff0",
#     "difficulty" : 0.000244140625,
#     "previousblockhash" : "00000de52875a68d7bf6a5bb5ad1b89fd7df4d67a9603669327949923dc74d7e",
#     "nextblockhash" : "00000e3f18b2b2256661b497e9b47e3816f5f7ab0fb9c2386b10ffe42eaa5cb2"
# }

header_hex = ("02000000" + # reverse-hex version
    "7e4dc73d92497932693660a9674ddfd79fb8d15abba5f67b8da67528e50d0000" + # reverse-hex previous blockhash
    "92eb6e44788b23c8ebbe25f6c24b5deaa20e122da2f0487f05d03900b40fe450" + # reverse-hex merkleroot
    "40fd835a" + # reverse-hex time
    "f0ff0f1e" + # reverse-hex bits
    "00baaa1e") # reverse-hex nonce

best_hash = 'b312d1d587976e6479d31e1150e860c1fa00cd01278148e1fdd880d04c900000'

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_dash_hash(self):
        self.pow_hash = hexlify(dash_hash.getPoWHash(self.block_header))
        self.assertEqual(self.pow_hash.decode(), self.best_hash)


if __name__ == '__main__':
    unittest.main()

