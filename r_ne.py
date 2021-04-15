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
from Get_global_value import c0
from calc_jr import calc_jr
from calc_jt import calc_jt
from skew_sym import skew_sym
from calc_vel import calc_vel
from calc_acc import calc_acc
from Get_global_value import Gravity
from Get_global_value import SS
from Get_global_value import SE
from Get_global_value import ce
from Get_global_value import S0
from cross import cross


def r_ne(R0, RR, A0, AA, v0, w0, vd0, wd0, q, qd, qdd, Fe, Te):
    A_I_0 = A0
    vv, ww = calc_vel(A0, AA, v0, w0, q, qd)
    vd, wd = calc_acc(A0, AA, w0, ww, vd0, wd0, q, qd, qdd)
    FF0 = m0 * (vd0 - Gravity)
    inertia_I_0 = np.dot(np.dot(A_I_0, inertia0), A_I_0.T)
    TT0 = np.dot(inertia_I_0, wd0[0:3]) + cross(w0[0:3], np.dot(inertia_I_0, w0[0:3]))

    FF = np.zeros((num_q, 3))
    TT = np.zeros((num_q, 3))

    if num_q == 0:
        print('Single body, there is no link')
    else:
        for i in range(num_q):
            A_I_i = AA[i, :, :]
            in_i = inertia[i, :, :]
            FF[i, :] = m[i] * (vd[i, :] - Gravity)
            inertia_I_i = np.dot(np.dot(A_I_i, in_i), A_I_i.T)
            TT[i, :] = np.dot(inertia_I_i, wd[i, :]) + cross(ww[i, :], np.dot(inertia_I_i, ww[i, :]))

    Fj = np.zeros((num_q, 3))
    Tj = np.zeros((num_q, 3))

    if num_q != 0:
        for i in range(num_q-1, -1, -1):
            F = np.zeros(3)
            T = np.zeros(3)
            for j in range(i+1, num_q, 1):
                F = F + SS[i, j] * Fj[j, :]
            Fj[i, :] = FF[i, :] + F - SE[i] * Fe[i, :]

            for j in range(i+1, num_q, 1):
                A_I_i = AA[i, :, :]
                T = T + SS[i, j] * (cross(np.dot(A_I_i, (cc[i, j, :] - cc[i, i, :] + np.dot(np.dot((J_type[i] == 'P'),
                                                                                                   Ez), q[i]))),
                                          Fj[j, :]) + Tj[j, :])
            if J_type[i] == 'R':
                A_I_i = AA[i, :, :]
                Tj[i, :] = TT[i, :] + T - cross(np.dot(A_I_i, cc[i, i, :]), FF[i, :])
            else:
                A_I_i = AA[i, :, :]
                Tj[i, :] = TT[i, :] + T + cross(np.dot(A_I_i, np.dot(Ez, q[i])) - np.dot(A_I_i, cc[i, i, :]), FF[i, :])
            Tj[i, :] = Tj[i, :] - SE[i] * (cross(np.dot(A_I_i, (ce[i, :] - cc[i, i, :]
                                                                + np.dot(np.dot((J_type[i] == 'P'), Ez), q[i]))),
                                                 Fe[i, :]) + Te[i, :])

        F = np.zeros(3)
        T = np.zeros(3)
        for i in range(num_q):
            if S0[i] != 0:
                F = F + S0[i] * Fj[i, :]
        FF0 = FF0 + F

        for i in range(num_q):
            if S0[i] != 0:
                T = T + S0[i] * (cross(np.dot(A_I_0, c0[i, :]), Fj[i, :]) + Tj[i, :])
            TT0 = TT0 + T

    tau = np.zeros(num_q)
    if num_q == 0:
        tau = np.zeros(num_q)
    else:
        for i in range(num_q):
            A_I_i = AA[i, :, :]
            if J_type == 'R':
                tau[i] = np.dot(Tj[i, :].T, np.dot(A_I_i, Ez))
            else:
                tau[i] = np.dot(Fj[i, :].T, np.dot(A_I_i, Ez))

    Force = np.zeros(num_q+6)
    if num_q == 0:
        Force[0:3] = FF0
        Force[3:6] = TT0
    else:
        Force[0:3] = FF0
        Force[3:6] = TT0
        Force[6:num_q+6] = tau

    return Force










    
























