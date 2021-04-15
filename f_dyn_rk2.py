import numpy as np
from Get_global_value import BB
from Get_global_value import S0
from Get_global_value import SS
from Get_global_value import SE
from Get_global_value import J_type
from Get_global_value import Qi
from Get_global_value import Qe
from Get_global_value import c0
from Get_global_value import cc
from Get_global_value import ce
from Get_global_value import m0
from Get_global_value import m
from Get_global_value import mass
from Get_global_value import inertia0
from Get_global_value import inertia
from Get_global_value import num_q, Ez, Gravity, d_time


def f_dyn_rk2(R0, A0, v0, w0, q, qd, F0, T0, Fe, Te, tau):
    [tmp_vd0, tmp_wd0, tmp_qdd] = f_dyn(R0, A0, v0, w0, q, qd, F0, T0, Fe, Te, tau)
