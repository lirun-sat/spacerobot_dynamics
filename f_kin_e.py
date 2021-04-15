import numpy as np
from Get_global_value import Qe
from Get_global_value import ce
from rpy2dc import rpy2dc


def f_kin_e(RR, AA, joints):
    n = len(joints)
    k = joints[-1]
    A_I_i = AA[k, :, :]
    A_i_EE = rpy2dc(Qe[k, :], 0, 0)
    ORI_e = np.dot(A_I_i, A_i_EE)
    POS_e = RR[k, :] + np.dot(A_I_i, ce[k, :])

    return POS_e, ORI_e




