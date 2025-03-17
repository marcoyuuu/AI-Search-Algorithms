"""
figure_3_31_env.py

PEP 8–compliant file defining the environment that replicates Figure 3.31.
Polygons are created with minimal labeling (one per shape),
and manual cross-polygon edges are asserted as specified.
"""

from shortest_path.state_space import StateSpace

def build_figure_3_31_env():
    """
    Construct and return a StateSpace object that replicates
    Figure 3.31 with polygons and manually asserted cross-polygon edges.
    """
    env = StateSpace()

    # Start
    env.set_start(0.0, 0.7, "S")

    # Rectangle
    env.add_vertex(0.5, 0.0, "rec1")
    env.add_vertex(0.5, 1.4, "rec2")
    env.add_vertex(4.6, 1.4, "rec3")
    env.add_vertex(4.6, 0.0, "rec4")
    env.connect_polygon(["rec1", "rec2", "rec3", "rec4"], shape_label="Rect1")

    # Pentagon
    env.add_vertex(1.7, 2.0, "pent1")
    env.add_vertex(0.3, 2.3, "pent2")
    env.add_vertex(0.0, 3.8, "pent3")
    env.add_vertex(1.5, 5.1, "pent4")
    env.add_vertex(2.6, 3.7, "pent5")
    env.connect_polygon(["pent1", "pent2", "pent3", "pent4", "pent5"], shape_label="Pent")

    # Triangle
    env.add_vertex(2.5, 1.8, "tri1")
    env.add_vertex(3.1, 4.0, "tri2")
    env.add_vertex(3.7, 1.8, "tri3")
    env.connect_polygon(["tri1", "tri2", "tri3"], shape_label="Tri1")

    # Quadrilateral
    env.add_vertex(3.9, 3.3, "quad1")
    env.add_vertex(3.7, 4.9, "quad2")
    env.add_vertex(4.8, 5.1, "quad3")
    env.add_vertex(5.7, 4.4, "quad4")
    env.connect_polygon(["quad1", "quad2", "quad3", "quad4"], shape_label="Quad1")

    # Triangle 2
    env.add_vertex(5.4, 0.7, "tri_2_1")
    env.add_vertex(4.9, 2.6, "tri_2_2")
    env.add_vertex(6.3, 1.5, "tri_2_3")
    env.connect_polygon(["tri_2_1", "tri_2_2", "tri_2_3"], shape_label="Tri2")

    # Rectangle 2
    env.add_vertex(5.8, 2.2, "rec_2_1")
    env.add_vertex(5.8, 5.0, "rec_2_2")
    env.add_vertex(7.5, 5.0, "rec_2_3")
    env.add_vertex(7.5, 2.2, "rec_2_4")
    env.connect_polygon(["rec_2_1", "rec_2_2", "rec_2_3", "rec_2_4"], shape_label="Rect2")

    # Hexagon
    env.add_vertex(7.7, 0.0, "hex1")
    env.add_vertex(6.8, 0.6, "hex2")
    env.add_vertex(6.8, 1.5, "hex3")
    env.add_vertex(7.7, 2.2, "hex4")
    env.add_vertex(8.5, 1.5, "hex5")
    env.add_vertex(8.5, 0.4, "hex6")
    env.connect_polygon(["hex1", "hex2", "hex3", "hex4", "hex5", "hex6"], shape_label="Hex")

    # Quadrilateral 2
    env.add_vertex(8.7, 1.8, "quad_2_1")
    env.add_vertex(7.8, 4.7, "quad_2_2")
    env.add_vertex(8.6, 5.0, "quad_2_3")
    env.add_vertex(8.9, 4.5, "quad_2_4")
    env.connect_polygon(["quad_2_1", "quad_2_2", "quad_2_3", "quad_2_4"], shape_label="Quad2")

    # Goal
    env.set_goal(9.1, 5.0, "G")

    # Manually assert cross-polygon edges
    # (Matches your snippet for Figure 3.31)
    env.assert_reachable("S", ["rec1", "rec2", "pent2", "pent3"])
    env.assert_reachable("rec1", ["pent2", "pent3"])
    env.assert_reachable("rec2", ["pent1", "pent2", "tri1", "tri3"])
    env.assert_reachable("rec3", ["pent1", "tri1", "tri2", "tri3", "quad1", "tri_2_1", "tri_2_2"])
    env.assert_reachable("rec4", ["tri_2_1", "tri_2_2", "tri_2_3", "hex1", "hex2", "hex3", "rec_2_4"])
    env.assert_reachable("pent1", ["tri1", "tri2"])
    env.assert_reachable("pent4", ["tri2", "quad2", "quad3"])
    env.assert_reachable("pent5", ["tri1", "tri2", "quad2"])
    env.assert_reachable("tri2", ["quad1", "quad2", "tri_2_1"])
    env.assert_reachable("tri3", ["quad1", "quad2", "quad4", "tri_2_2"])
    env.assert_reachable("quad1", ["tri_2_1", "tri_2_2", "rec_2_1"])
    env.assert_reachable("quad3", ["rec_2_2", "rec_2_3", "quad_2_3"])
    env.assert_reachable("quad4", ["tri_2_2", "rec_2_1", "rec_2_2"])
    env.assert_reachable("tri_2_1", ["rec_2_4", "hex1", "hex2", "hex3", "hex4"])
    env.assert_reachable("tri_2_2", ["rec_2_1", "hex3"])
    env.assert_reachable("tri_2_3", ["rec_2_1", "rec_2_4", "hex2", "hex3", "hex4"])
    env.assert_reachable("rec_2_1", ["hex3", "hex4"])
    env.assert_reachable("rec_2_2", "quad_2_3")
    env.assert_reachable("rec_2_3", ["quad_2_1", "quad_2_2", "quad_2_3", "hex4", "hex5"])
    env.assert_reachable("rec_2_4", ["hex3", "hex4", "quad_2_1", "quad_2_2"])
    env.assert_reachable("hex4", ["quad_2_1", "quad_2_2"])
    env.assert_reachable("hex5", ["quad_2_1", "quad_2_2"])
    env.assert_reachable("hex6", ["quad_2_1", "G"])
    env.assert_reachable("quad_2_1", "G")
    env.assert_reachable("quad_2_3", "G")
    env.assert_reachable("quad_2_4", "G")

    return env
