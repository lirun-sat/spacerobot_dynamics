
"""
    global num_q
    global BB
    global J_type
    global Qi, S0, SS, SE, c0, cc, ce, Qe, m0, m
    global mass, inertia0, inertia, Ez, Gravity
    global delta_t
"""


def _init():
    global _global_dict
    _global_dict = {}


def set_value(name, value):
    _global_dict[name] = value


def get_value(name, defValue=None):
    try:
        return _global_dict[name]
    except KeyError:
        return defValue









