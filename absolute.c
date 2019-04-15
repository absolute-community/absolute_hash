#include "dash.h"
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <stdio.h>

#include "sha3/sph_blake.h"
#include "sha3/sph_bmw.h"
#include "sha3/sph_groestl.h"
#include "sha3/sph_jh.h"
#include "sha3/sph_keccak.h"
#include "sha3/sph_skein.h"
#include "sha3/sph_luffa.h"
#include "sha3/sph_cubehash.h"
#include "sha3/sph_shavite.h"
#include "sha3/sph_simd.h"
#include "sha3/sph_echo.h"
#include "sha3/Lyra2.h"


void absolute_hash(const char* input, char* output)

{
	sph_blake256_context ctx_blake;
	sph_cubehash256_context ctx_cubehash;
	sph_keccak256_context ctx_keccak;
	sph_skein256_context ctx_skein;
	sph_bmw256_context ctx_bmw;
	
	uint32_t hashA[8], hashB[8];
	
    sph_blake256_init(&ctx_blake);
    sph_blake256(&ctx_blake, input, 80);
    sph_blake256_close (&ctx_blake, hashA);	
	
    sph_keccak256_init(&ctx_keccak);
    sph_keccak256(&ctx_keccak, hashA, 32); 
    sph_keccak256_close(&ctx_keccak, hashB);
    
    sph_cubehash256_init(&ctx_cubehash);
    sph_cubehash256(&ctx_cubehash, hashB, 32);
    sph_cubehash256_close(&ctx_cubehash, hashA);
    
    LYRA2(hashB, 32, hashA, 32, hashA, 32, 1, 4, 4);
    
    sph_skein256_init(&ctx_skein);
    sph_skein256(&ctx_skein, hashB, 32); 
    sph_skein256_close(&ctx_skein, hashA);
    
    sph_cubehash256_init(&ctx_cubehash);
    sph_cubehash256(&ctx_cubehash, hashA, 32);
    sph_cubehash256_close(&ctx_cubehash, hashB);
    
    sph_bmw256_init(&ctx_bmw);
    sph_bmw256(&ctx_bmw, hashB, 32);
    sph_bmw256_close(&ctx_bmw, hashA);
    
    memcpy(output, hashA, 32);
}
