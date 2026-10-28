# MOBCAL-2018

The two MOBCAL programs, helium and nitrogen, that describe the van der Waals interaction between
an ion and the buffer gas with the exp-6 potential of MM3 and per-atom parameters from the Merck
molecular force field (MMFF94), as reported by Lee, Davidson, Bush and Kim for helium [1] and by
Lee, Lee, Davidson, Bush and Kim for nitrogen [2], together with the script that writes their
input files, the two parameter tables it reads, and a slide deck that walks through the workflow.
This repository keeps the release exactly as Hugh Kim's group distributed it, for the record and
for anyone who needs to reproduce a number that was calculated with it. It is a branch of the
MOBCAL lineage rather than an ancestor of [bushgroup/MOBCAL](https://github.com/bushgroup/MOBCAL),
which is where the trajectory method is maintained and developed now and which keeps the 12-6
Lennard-Jones potential of the 2012 programs. Nothing here is developed further.

### Any research that uses this code should reference [1] for calculations in helium and [2] for calculations in nitrogen.

### References

1. Lee, J. W.; Davidson, K. L.; Bush, M. F.; Kim, H. I. Collision Cross Sections and Ion
   Structures: Development of a General Calculation Method via High-Quality Ion Mobility
   Measurements and Theoretical Modeling. *Analyst* 2017, 142, 4289-4298.
   https://doi.org/10.1039/c7an01276d
2. Lee, J. W.; Lee, H. H. L.; Davidson, K. L.; Bush, M. F.; Kim, H. I. Structural
   Characterization of Small Molecular Ions by Ion Mobility Mass Spectrometry in Nitrogen Drift
   Gas: Improving the Accuracy of Trajectory Method Calculations. *Analyst* 2018, 143,
   1786-1796. https://doi.org/10.1039/c8an00270c
3. Mesleh, M. F.; Hunter, J. M.; Shvartsburg, A. A.; Schatz, G. C.; Jarrold, M. F. Structural
   Information from Ion Mobility Measurements: Effects of the Long Range Potential. *J. Phys.
   Chem.* 1996, 100, 16082-16086. https://doi.org/10.1021/jp961623v
4. Kim, H.; Kim, H. I.; Johnson, P. V.; Beegle, L. W.; Beauchamp, J. L.; Goddard, W. A.; Kanik,
   I. Experimental and Theoretical Investigation into the Correlation between Mass and Ion
   Mobility for Choline and Other Ammonium Cations in N2. *Anal. Chem.* 2008, 80, 1928-1936.
   https://doi.org/10.1021/ac701888e
5. Campuzano, I. D. G.; Bush, M. F.; Robinson, C. V.; Beaumont, C.; Richardson, K.; Kim, H.;
   Kim, H. I. Structural Characterization of Drug-like Compounds by Ion Mobility Mass
   Spectrometry: Comparison of Theoretical and Experimentally Derived Nitrogen Collision
   Cross-sections. *Anal. Chem.* 2012, 84, 1026-1033. https://doi.org/10.1021/ac202625t
6. Halgren, T. A. Merck Molecular Force Field. I. Basis, Form, Scope, Parameterization, and
   Performance of MMFF94. *J. Comput. Chem.* 1996, 17, 490-519.
   https://doi.org/10.1002/(SICI)1096-987X(199604)17:5/6%3C490::AID-JCC1%3E3.0.CO;2-P

## Files

| File | What it is | SHA-256 |
|---|---|---|
| `mobcal_MMFF_Exp6_helium.f` | The helium program, fixed-form Fortran | `49a1a905593f2f0ac1e9806cf37ec306dc6493aa3b4c6b254d253fccb04659fe` |
| `mobcal_MMFF_Exp6_nitrogen.f` | The nitrogen program, fixed-form Fortran | `21e5660ade03bd2f116fa296cd9931af271c66e6b963c62fc578b6c10aa2996a` |
| `xyztomfj_mmff_mmffcharge.py` | The Python script that writes an input file from the MMFF94 atom types and charges that `sdf2tinkerxyz` assigns | `598e6e7ee20b99f75bc66934672e6718d78eeadb20ddb22152badbbba5d26501` |
| `mass.prm` | The MMFF94 atom types with their masses, 212 lines taken from Tinker's `mmff.prm` | `b9d1711efa8592eb3c594c4d6e25d111f9867d9db77302fd95e9a91ca431b2ff` |
| `vdw.prm` | The MMFF94 van der Waals parameters α, N, A and G for 95 atom classes, from Appendix B of [6] | `0b963e3089abb2f628d1a13a723a9b20cf1f29f5c9d9d41b805dd5d6d29f0d6d` |
| `CCS_Modifiedmobcal_20180315.pptx` | Ten slides by Jong Wha Lee, dated 15 March 2018, on preparing an input file and running the programs | `0408688b9ea0cf30409319a285bce876dbdf700a9ad006cc33f8725cebc30401` |

The six files are byte for byte the archive `Mobcal_20180315` as downloaded from
https://www.hughkimlab.com/codes on 27 October 2026. The file dates in that archive run from
29 September 2016 for `vdw.prm` to 15 March 2018 for the nitrogen program and the slides; the
helium program and the script are dated 14 April 2017. Line endings are kept as distributed,
CRLF in the helium program and the two parameter files and LF in the nitrogen program and the
script. The archive also held two empty folders, `openbabel(not included)` and
`sdf2tinkerxyz(not included)`, that mark the two external programs the workflow needs; git does
not store empty folders, so they are recorded here instead. The release contains no example
input and no reference output.

## Preparing an input file

To calculate a cross section with these programs, each atom of the ion needs its MMFF94 atom
type and partial charge, which the slides obtain in three steps:

1. Convert the structure to an `.sdf` file with [Open Babel](https://openbabel.org).
2. Assign MMFF94 atom types and charges with
   [sdf2tinkerxyz](http://sdf2xyz2sdf.sourceforge.net), which writes a Tinker `.xyz` file and a
   `.key` file.
3. Run `python xyztomfj_mmff_mmffcharge.py ion.xyz ion.key ion.mfj` in a directory that holds
   `mass.prm` and `vdw.prm`.

The input file is the `.mfj` format of the 2000 release, described in the `mobcal.txt` of
[bushgroup/MOBCAL-2000](https://github.com/bushgroup/MOBCAL-2000), with nine columns per atom
instead of five: x, y and z, the mass, the partial charge, and the van der Waals parameters α,
N, A and G of the atom's MMFF94 type. The charge column is read for every atom whichever charge
keyword the file gives. The slides recommend checking the atom types and the sum of the charges
that the script prints, because `sdf2tinkerxyz` does not always assign charges correctly to an
ion protonated at an uncommon site; in their example, protonation at an oxygen atom gives a
total charge of zero, and charges calculated otherwise must be supplied instead. The slides
also caution that inputs with more than one coordinate set have not been verified extensively.

## Building and running

The programs keep the routines of the 2000 code that rely on local variables keeping their
values between calls, so a gfortran build needs `-fno-automatic`, for the reason the MOBCAL-2000
README gives:

```
gfortran -O3 -fno-automatic -std=legacy -o mobcal_He mobcal_MMFF_Exp6_helium.f
gfortran -O3 -fno-automatic -std=legacy -o mobcal_N2 mobcal_MMFF_Exp6_nitrogen.f
```

Built that way with gfortran 16.2.0 on Windows on 27 October 2026, both programs compiled
without an edit and without a warning. Neither has been run on an input here.

Each program takes five arguments: the input file, the output file, the random number seed, and
two factors that scale the pair distance r\* and the well depth ε of every atom, in that order.
For example:

```
./mobcal_He ion.mfj ion_He.out 1000 0.98 0.81
./mobcal_N2 ion.mfj ion_N2.out 1000 0.76 0.86
```

The factors in these two lines are the ones the slides give, 0.98 and 0.81 in helium from Table
S9 of [1] and 0.76 and 0.86 in nitrogen from Table S2 of [2]. The slides recommend averaging at
least three calculations made with different seeds. Started without arguments, each program
stops with `provide input file name`. Note that, given the name of an input file that does not
exist, each program creates that file empty and stops on a Fortran end-of-file error.

## Where these programs come from

The helium program is the Jarrold group's 2000 release
([bushgroup/MOBCAL-2000](https://github.com/bushgroup/MOBCAL-2000)) with the changes below and
none of those made for the 2012 helium program: it keeps the 2000 temperature of 298 K, the
2000 Lennard-Jones table (as comments) and the 2000 run file `mobcal.run` (also as comments).
Four of its eighteen program units change. The main program reads its five arguments from the command
line, defines the MMFF94 parameters of helium, sets the number of trajectories per velocity point
per cycle, `imp`, to 100 from 25, and no longer calls the routine for the exact hard-sphere
scattering and projection approximation methods, so the programs report trajectory-method cross
sections only. The two routines that read coordinates read the nine columns, take the mass from
the file instead of rounding it to find the element, combine each atom's parameters with those of
the gas by the MMFF94 combining rules [6], and multiply the pair distance and the well depth by
the two factors. The keyword `equal` now spreads the sum of the charge column evenly over the
atoms, whereas the 2000 code spread a total charge of +1. The potential routine replaces the 12-6
Lennard-Jones term with the exp-6 term of MM3, ε[1.84 × 10⁵ exp(−12r/r\*) − 2.25(r\*/r)⁶], its
well depth normalized to ε by a factor of 1/1.1195, and keeps the ion-induced dipole term. Eleven
other routines differ only in the common blocks that carry the new parameters, and the three
random-number routines are unchanged.

The nitrogen program is the helium program with the ion-nitrogen interaction of the 2012 nitrogen
program ([bushgroup/MOBCAL-2012](https://github.com/bushgroup/MOBCAL-2012)), which extended the
trajectory method to nitrogen [4, 5]. That interaction, i.e., two nitrogen sites 1.0976 Å apart,
partial charges that give the molecule its quadrupole moment, an ion-induced dipole term, and an
average over three orientations of the molecule weighted by their Boltzmann factors at 500 K, is
carried over unchanged, except that each nitrogen site interacts with every atom of the ion
through the exp-6 term, with MMFF94-form parameters for nitrogen in place of the helium ones. The
program also carries over from the 2012 nitrogen program the 0.553 Å it adds to the largest pair
distance and its omission of the energy-conservation check, and keeps the 2012 nitrogen element
table as comments. It raises from 500 to 2,500 the number of steps in impact parameter allowed
when the trajectory method searches for the largest impact parameter at each velocity, and it
runs at 298 K with `imp` = 50.

## As found, not corrected

The files are kept as distributed, so two slips in the slides are recorded here rather than
corrected. The compile line on slides 6 and 10 names `mobcal_MMFF_Exp6.f`, whereas the release
holds the two programs named for their gases. And slide 6 recommends repeating a calculation
"using different scaling factors (1000 in the example above)"; the 1000 in that example is the
random seed, and the recommendation is to repeat with different seeds.

## License and permission

GNU General Public License v3.0; see [`LICENSE`](LICENSE). Copyright (C) 2017–2018 Hugh I.
Kim. The release as distributed carried no license statement. Hugh Kim gave his permission for
it to be made public on 28 October 2026 and left the choice of license to Matthew Bush, who
applied the license that its two ancestors, the 2000 and 2012 releases, carry. The files
themselves are not modified: no license header was added to either program.
