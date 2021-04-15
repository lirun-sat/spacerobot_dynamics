import numpy as np
from Get_global_value import Qe
from Get_global_value import ce
from Get_global_value import cc
from Get_global_value import J_type
from Get_global_value import num_q
from Get_global_value import Ez
from calc_jte import calc_jte
from calc_jre import calc_jre


def calc_je(RR, AA, q, joints):
    n = len(joints)
    # JJ_te = np.zeros((num_q, 3))
    # JJ_re = np.zeros((num_q, 3))
    JJ = np.zeros((n, 6))
    JJ_te = calc_jte(RR, AA, q, joints)
    JJ_re = calc_jre(AA, joints)
    for i in range(n):
        JJ[i, 0:3] = JJ_te[i, 0:3]
        JJ[i, 3:6] = JJ_re[i, 0:3]

    Jacobian = np.zeros((n, 6))
    for i in range(n):
        Jacobian[joints[i], :] = JJ[i, 0:6]

    return Jacobian


