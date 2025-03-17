"""
geometry.py

PEP 8–compliant geometry utilities for intersection checks and
point-in-polygon logic. Also includes sampling along a line for
robust interior checks, if needed for automated edge generation.
"""

import math


def segments_intersect(p1, q1, p2, q2):
    """
    Return True if line segments p1->q1 and p2->q2 intersect.
    Uses orientation tests and on-segment checks.
    """
    def orientation(a, b, c):
        val = (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])
        if abs(val) < 1e-9:
            return 0
        return 1 if val > 0 else 2

    def on_segment(a, b, c):
        return (min(a[0], c[0]) <= b[0] <= max(a[0], c[0]) and
                min(a[1], c[1]) <= b[1] <= max(a[1], c[1]))

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True
    if o1 == 0 and on_segment(p1, p2, q1):
        return True
    if o2 == 0 and on_segment(p1, q2, q1):
        return True
    if o3 == 0 and on_segment(p2, p1, q2):
        return True
    if o4 == 0 and on_segment(p2, q1, q2):
        return True
    return False


def point_in_polygon(point, polygon):
    """
    Ray-casting algorithm to determine if 'point' is inside 'polygon'.
    polygon is a list of (x, y) vertices. Returns True if inside.
    """
    x, y = point
    inside = False
    n = len(polygon)
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        if ((y1 > y) != (y2 > y)):
            intersect_x = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if intersect_x > x:
                inside = not inside
    return inside


def sample_line(p1, p2, num_samples=5):
    """
    Yield intermediate sample points along the line from p1->p2,
    excluding the endpoints, for robust interior checks.
    """
    for i in range(1, num_samples):
        t = i / num_samples
        x = p1[0] + t * (p2[0] - p1[0])
        y = p1[1] + t * (p2[1] - p1[1])
        yield (x, y)


def line_clear(p1, p2, polygons, num_samples=5):
    """
    Returns True if the line from p1->p2 does not intersect any polygon edges
    and none of the interior sample points lie inside a polygon.
    This is optional for automated edge generation, not required if you only
    rely on manual edges.
    """
    # 1) Check intersections with polygon edges
    for poly in polygons:
        n = len(poly)
        for i in range(n):
            v1, v2 = poly[i], poly[(i + 1) % n]
            if v1 == p1 or v1 == p2 or v2 == p1 or v2 == p2:
                continue
            if segments_intersect(p1, p2, v1, v2):
                return False

    # 2) Check sample points for interior crossing
    for pt in sample_line(p1, p2, num_samples):
        for poly in polygons:
            if point_in_polygon(pt, poly):
                return False

    return True
