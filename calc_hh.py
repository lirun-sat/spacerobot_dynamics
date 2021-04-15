import numpy as np
from Get_global_value import num_q
from Get_global_value import J_type
from Get_global_value import Ez
from Get_global_value import BB
from Get_global_value import m0
from Get_global_value import m
from Get_global_value import mass
from Get_global_value import inertia0
from Get_global_value import inertia
from Get_global_value import cc
from calc_jr import calc_jr
from calc_jt import calc_jt
from skew_sym import skew_sym


def calc_hh(R0, RR, A0, AA):
    JJ_t = calc_jt(RR, AA)
    JJ_r = calc_jr(AA)

    wE = mass * np.eye(3)

    JJ_tg = np.zeros((num_q, 3))
    HH_w = np.zeros((3, 3))
    HH_wq = np.zeros((num_q, 3))
    HH_q = np.zeros((num_q, num_q))
    HH = np.zeros((num_q+6, num_q+6))
    wr0g = np.zeros(3)

    if num_q == 0:
        HH_w = np.dot(np.dot(A0, inertia0), A0.T)
        HH[0:3, 0:3] = wE
        HH[0:3, 3:6] = np.zeros((3, 3))
        HH[3:6, 0:3] = np.zeros((3, 3))
        HH[3:6, 3:6] = HH_w
    else:
        Rm = np.zeros(3)
        for i in range(num_q):
            Rm = Rm + np.dot(m[i], RR[i, :])
        Rm += np.dot(m0, R0)
        Rg = Rm/mass
        wr0g = np.dot((Rg - R0), mass)

    for i in range(num_q):
        r0i = RR[i, :] - R0
        A_I_i = AA[i, :, :]
        JJ_tg += + np.dot(m[i], JJ_t[i, :, :])
        inertia_I_i = np.dot(np.dot(A_I_i, inertia[i, :, :]), A_I_i.T)
        HH_w += inertia_I_i + np.dot(m[i], np.dot(skew_sym(r0i).T, skew_sym(r0i)))

        HH_wq += np.dot(inertia_I_i, JJ_r[i, :, :]) + \
            np.dot(np.dot(m[i], skew_sym(r0i)), JJ_t[i, :, :])

        HH_q += np.dot(np.dot(JJ_r[i, :, :].T, inertia_I_i), JJ_r[i, :, :]) + \
            np.dot(np.dot(m[i], JJ_t[i, :, :].T), JJ_t[i, :, :])

    HH_w += np.dot(np.dot(A0, inertia0), A0.T)
    HH[0:3, 0:3] = wE
    HH[0:3, 3:6] = skew_sym(wr0g).T
    HH[0:3, 6:6+num_q] = JJ_tg
    HH[3:6, 0:3] = skew_sym(wr0g)
    HH[3:6, 3:6] = HH_w
    HH[3:6, 6:6+num_q] = HH_wq
    HH[6:6+num_q, 0:3] = JJ_tg.T
    HH[6:6+num_q, 3:6] = HH_wq.T
    HH[6:6+num_q, 6:6+num_q] = HH_q

    return HH



































