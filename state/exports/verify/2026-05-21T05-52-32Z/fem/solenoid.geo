// solenoid_axisym.geo — parametric axisymmetric finite solenoid for
// getdp_hts.py. Placeholders ($NAME) are substituted by the Python
// producer before invoking gmsh. Domain layout:
//
//   r=0 (axis)              r=R_out
//   +------+----+-----+------+   <- z=+H_out
//   |      |    |     |      |
//   | air  | -- |coil | air  |
//   |      | -- |     |      |
//   |      | -- |     |      |
//   +------+----+-----+------+   <- z=-H_out
//   ↑axis  r=r_in r=r_out
//
// Coordinate convention: getdp axisym pairs x→r, y→z; OpenCASCADE not
// needed (built-in kernel keeps things deterministic on Apple Silicon).

R_OUT  = 0.25;
H_OUT  = 0.6;
R_IN   = 0.03;
R_OUTC = 0.25C;
H_COIL = 0.2;
LC_AIR  = 0.025;
LC_COIL = 0.00625;

// Air outer box corners
Point(1) = {0,     -H_OUT, 0, LC_AIR};
Point(2) = {R_OUT, -H_OUT, 0, LC_AIR};
Point(3) = {R_OUT,  H_OUT, 0, LC_AIR};
Point(4) = {0,      H_OUT, 0, LC_AIR};

// Coil rectangle corners
Point(5) = {R_IN,   -H_COIL/2, 0, LC_COIL};
Point(6) = {R_OUTC, -H_COIL/2, 0, LC_COIL};
Point(7) = {R_OUTC,  H_COIL/2, 0, LC_COIL};
Point(8) = {R_IN,    H_COIL/2, 0, LC_COIL};

// Outer box edges (clockwise from bottom-left axis)
Line(1) = {1, 2};   // bottom (z=-H_OUT)
Line(2) = {2, 3};   // right (r=R_OUT)
Line(3) = {3, 4};   // top (z=+H_OUT)
Line(4) = {4, 1};   // axis (r=0)

// Coil edges
Line(5) = {5, 6};
Line(6) = {6, 7};
Line(7) = {7, 8};
Line(8) = {8, 5};

Curve Loop(1) = {1, 2, 3, 4};
Curve Loop(2) = {5, 6, 7, 8};
Plane Surface(1) = {1, 2};   // air (with coil hole)
Plane Surface(2) = {2};      // coil

Physical Surface("AIR",  1000) = {1};
Physical Surface("COIL", 2000) = {2};
Physical Curve("AXIS", 3000) = {4};
Physical Curve("FAR_BND", 4000) = {1, 2, 3};

Mesh.Algorithm = 6;   // Frontal-Delaunay
Mesh.ElementOrder = 1;
