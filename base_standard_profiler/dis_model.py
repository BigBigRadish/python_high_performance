# -*- coding: utf-8 -*-
'''
Created on 2019年4月9日 下午3:57:29
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#使用反汇编模块
import dis
from app import ParticleSimulator
dis.dis(ParticleSimulator.evolve)
'''
 20           0 LOAD_CONST               1 (0.0001)
              3 STORE_FAST               2 (timestep)

 21           6 LOAD_GLOBAL              0 (int)
              9 LOAD_FAST                1 (dt)
             12 LOAD_FAST                2 (timestep)
             15 BINARY_DIVIDE       
             16 CALL_FUNCTION            1
             19 STORE_FAST               3 (nsteps)

 23          22 SETUP_LOOP             160 (to 185)
             25 LOAD_GLOBAL              1 (range)
             28 LOAD_FAST                3 (nsteps)
             31 CALL_FUNCTION            1
             34 GET_ITER            
        >>   35 FOR_ITER               146 (to 184)
             38 STORE_FAST               4 (i)

 24          41 SETUP_LOOP             137 (to 181)
             44 LOAD_FAST                0 (self)
             47 LOAD_ATTR                2 (particle)
             50 GET_ITER            
        >>   51 FOR_ITER               126 (to 180)
             54 STORE_FAST               5 (p)

 26          57 LOAD_FAST                5 (p)
             60 LOAD_ATTR                3 (x)
             63 LOAD_CONST               2 (2)
             66 BINARY_POWER        
             67 LOAD_FAST                5 (p)
             70 LOAD_ATTR                4 (y)
             73 LOAD_CONST               2 (2)
             76 BINARY_POWER        
             77 BINARY_ADD          
             78 LOAD_CONST               3 (0.5)
             81 BINARY_POWER        
             82 STORE_FAST               6 (norm)

 27          85 LOAD_FAST                5 (p)
             88 LOAD_ATTR                4 (y)
             91 UNARY_NEGATIVE      
             92 LOAD_FAST                6 (norm)
             95 BINARY_DIVIDE       
             96 STORE_FAST               7 (v_x)

 28          99 LOAD_FAST                5 (p)
            102 LOAD_ATTR                3 (x)
            105 UNARY_NEGATIVE      
            106 LOAD_FAST                6 (norm)
            109 BINARY_DIVIDE       
            110 STORE_FAST               8 (v_y)

 30         113 LOAD_FAST                2 (timestep)
            116 LOAD_FAST                5 (p)
            119 LOAD_ATTR                5 (ang_vel)
            122 BINARY_MULTIPLY     
            123 LOAD_FAST                7 (v_x)
            126 BINARY_MULTIPLY     
            127 STORE_FAST               9 (d_x)

 31         130 LOAD_FAST                2 (timestep)
            133 LOAD_FAST                5 (p)
            136 LOAD_ATTR                5 (ang_vel)
            139 BINARY_MULTIPLY     
            140 LOAD_FAST                8 (v_y)
            143 BINARY_MULTIPLY     
            144 STORE_FAST              10 (d_y)

 33         147 LOAD_FAST                5 (p)
            150 DUP_TOP             
            151 LOAD_ATTR                3 (x)
            154 LOAD_FAST                9 (d_x)
            157 INPLACE_ADD         
            158 ROT_TWO             
            159 STORE_ATTR               3 (x)

 34         162 LOAD_FAST                5 (p)
            165 DUP_TOP             
            166 LOAD_ATTR                4 (y)
            169 LOAD_FAST               10 (d_y)
            172 INPLACE_ADD         
            173 ROT_TWO             
            174 STORE_ATTR               4 (y)
            177 JUMP_ABSOLUTE           51
        >>  180 POP_BLOCK           
        >>  181 JUMP_ABSOLUTE           35
        >>  184 POP_BLOCK           
        >>  185 LOAD_CONST               0 (None)
            188 RETURN_VALUE        
'''