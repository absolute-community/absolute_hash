from distutils.core import setup, Extension

dash_hash_module = Extension('absolute_hash',
                                 sources = ['absolutemodule.c',
                                            'sha3/Lyra2RE.c',
                                            'sha3/Lyra2.c',
                                            'sha3/Sponge.c',
                                            'sha3/blake.c',
                                            'sha3/bmw.c',
                                            'sha3/cubehash.c',
                                            'sha3/groestl.c',
                                            'sha3/keccak.c',
                                            'sha3/skein.c',
                                            'sha3/simd.c'],
                               include_dirs=['.', './sha3'])

setup (name = 'absolute_hash',
       version = '1.3.1',
       description = 'Binding for Lyre2 proof of work hashing.',
       ext_modules = [absolute_hash_module])
