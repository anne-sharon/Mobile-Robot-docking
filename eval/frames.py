import math
from src.world import DOCK_FACE_X, DOCK_Y

MARKER_X, MARKER_Y = DOCK_FACE_X - 0.001, DOCK_Y        # marker centre in the world frame
MARKER_YAW = math.pi                                     # marker normal points west (-x) into the room


def wrap(a):
    return (a + math.pi) % (2 * math.pi) - math.pi


def world_to_frame(x, y, th, ox, oy, oth):
    """Express a world pose in a frame whose origin is (ox, oy, oth) in the world."""
    c, s = math.cos(-oth), math.sin(-oth)
    dx, dy = x - ox, y - oy
    return dx * c - dy * s, dx * s + dy * c, wrap(th - oth)


def world_to_dock(x, y, th):
    return world_to_frame(x, y, th, MARKER_X, MARKER_Y, MARKER_YAW)
