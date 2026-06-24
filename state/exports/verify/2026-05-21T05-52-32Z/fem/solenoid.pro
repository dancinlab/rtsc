// solenoid_axisym.pro — 2-D axisymmetric magnetostatic solenoid
// (linear A-φ formulation). Parametric placeholders ($NAME) are
// substituted by the Python producer (`getdp_hts.py`). Honest scope
// (g3): linear μ_r=1 everywhere — HTS critical-state / quench / 3-D
// effects NOT modelled. See `RTSC.md` §4.3 caveats s1-s4.
//
// References:
//   - C. Geuzaine, "GetDP: a general finite-element solver for the
//     de Rham complex", PAMM 7(1), 2007.
//   - F. Henrotte et al., "An energy-based variational model of
//     ferromagnetic hysteresis", JCAM 209(4), 2007. (formulation
//     ancestry — we use only the linear branch here.)
//   - getdp tutorial `examples/Magnetostatics` (linear A-φ).
//
// Coordinate convention: getdp axisym pairs gmsh x → r, gmsh y → z.
// VolAxiSqu Jacobian integrates with the 2π·r measure suitable for
// the A_φ vector potential (avoids singular behaviour at r=0).

Group {
  Air     = Region[1000];
  Coil    = Region[2000];
  Axis    = Region[3000];
  FarBnd  = Region[4000];
  Domain  = Region[{Air, Coil}];
}

Function {
  mu0 = 4 * Pi * 1e-7;
  nu[Air]  = 1 / mu0;
  nu[Coil] = 1 / mu0;
  // J_phi = N·I / A_coil (azimuthal current density, A/m²). Producer
  // substitutes the numerical value at template time.
  js[Coil] = 2.4e+06;
}

Constraint {
  { Name a_BC; Type Assign;
    Case { { Region FarBnd; Value 0; } }
  }
}

Jacobian {
  { Name Vol; Case { { Region All; Jacobian VolAxiSqu; } } }
  { Name Sur; Case { { Region All; Jacobian SurAxi;    } } }
}

Integration {
  { Name I1;
    Case { { Type Gauss;
      Case {
        { GeoElement Triangle; NumberOfPoints 4; }
        { GeoElement Line;     NumberOfPoints 4; }
      } } } }
}

FunctionSpace {
  { Name H_a; Type Form1P;
    BasisFunction {
      { Name se; NameOfCoef ae; Function BF_PerpendicularEdge;
        Support Domain; Entity NodesOf[All]; }
    }
    Constraint {
      { NameOfCoef ae; EntityType NodesOf;
        NameOfConstraint a_BC; }
    }
  }
}

Formulation {
  { Name Magstat_a; Type FemEquation;
    Quantity {
      { Name a; Type Local; NameOfSpace H_a; }
    }
    Equation {
      Galerkin { [ nu[] * Dof{d a}, {d a} ];
                 In Domain; Jacobian Vol; Integration I1; }
      Galerkin { [ -js[], {a} ];
                 In Coil; Jacobian Vol; Integration I1; }
    }
  }
}

Resolution {
  { Name MagStat;
    System { { Name Sys_Mag; NameOfFormulation Magstat_a; } }
    Operation {
      Generate[Sys_Mag];
      Solve[Sys_Mag];
      SaveSolution[Sys_Mag];
      PostOperation[MagStat];
    }
  }
}

PostProcessing {
  { Name MagStat; NameOfFormulation Magstat_a;
    Quantity {
      { Name b;    Value { Local { [ {d a} ];          In Domain; Jacobian Vol; } } }
      { Name bmag; Value { Local { [ Norm[{d a}] ];    In Domain; Jacobian Vol; } } }
      { Name bz;   Value { Local { [ CompZ[{d a}] ];   In Domain; Jacobian Vol; } } }
      { Name az;   Value { Local { [ CompZ[{a}] ];     In Domain; Jacobian Vol; } } }
      { Name Wmag;
        Value { Integral { [ 0.5 * nu[] * SquNorm[{d a}] ];
                In Domain; Jacobian Vol; Integration I1; } } }
    }
  }
}

PostOperation MagStat UsingPost MagStat {
  // |B| at coil center (r=0, z=0)
  Print[ bmag, OnPoint {0, 0, 0},
         File "/Users/ghost/core/demiurge/exports/rtsc/verify/2026-05-21T05-52-32Z/fem/bmag_center.txt", Format Table ];
  // Bz component at coil center (signed)
  Print[ bz,   OnPoint {0, 0, 0},
         File "/Users/ghost/core/demiurge/exports/rtsc/verify/2026-05-21T05-52-32Z/fem/bz_center.txt", Format Table ];
  // |B| swept along axis from -H_OUT to +H_OUT (200 samples)
  Print[ bmag, OnLine { {0, -0.6, 0} {0, 0.6, 0} } {200},
         File "/Users/ghost/core/demiurge/exports/rtsc/verify/2026-05-21T05-52-32Z/fem/bmag_axis.txt", Format Table ];
  // Total magnetic energy W = 0.5 ∫ (1/μ) |B|² dV → inductance L = 2W/I²
  Print[ Wmag[Domain],
         File "/Users/ghost/core/demiurge/exports/rtsc/verify/2026-05-21T05-52-32Z/fem/stored_energy.txt", Format Table ];
}
