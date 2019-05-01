# -*- coding: utf-8 -*-
'''
Created on 2019年5月1日 下午8:18:09
Zhukun Luo
Jiangxi University of Finance and Economics
'''
import numpy as np
from libc.math cimport sqrt

#@cython.boundscheck(False)
#@cython.cdivision(True)
def c_evolve(double[:, :] r_i,double[:] ang_speed_i,
             double timestep,int nsteps):
    cdef int i
    cdef int j
    cdef int nparticles = r_i.shape[0]
    cdef double norm, x, y, vx, vy, dx, dy, ang_speed


    for i in range(nsteps):
        for j in range(nparticles):
            x = r_i[j, 0]
            y = r_i[j, 1]
            ang_speed = ang_speed_i[j]

            norm = sqrt(x ** 2 + y ** 2)

            vx = (-y)/norm
            vy = x/norm

            dx = timestep * ang_speed * vx
            dy = timestep * ang_speed * vy

            r_i[j, 0] += dx
            r_i[j, 1] += dy