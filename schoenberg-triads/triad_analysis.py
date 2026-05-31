"""
Triad Analysis Script

This script implements the computational procedure described in:

Lucas Correia Lima da Silva,
"Triadic Structures, Mediation, and Monetary Instability:
A Computational Approach to Schoenberg's Piano Works"

Purpose
-------
The script analyses MusicXML scores and identifies explicitly articulated
triadic onset structures.

Only pitches beginning at the same onset are considered. Pitches sustained
from previous events are excluded from the triadic evaluation. The analysis
therefore measures the explicit articulation of triadic structures rather than
the complete sounding harmonic texture.

Accepted triad types
--------------------
- Major
- Minor
- Diminished
- Augmented

Notehead-based comparison
-------------------------
For notehead-based comparisons, the script uses an adjusted notehead count.

Tied continuations are excluded. If the same pitch-octave occurs simultaneously
in multiple voices, it is counted only once. Octave distinctions are preserved.

Output
------
For each analysed score the script reports:

- Total triads
- Triad-event share (%)
- Triads (% of noteheads)
- Root-position triads (% of noteheads)
- Onset events
- Adjusted notehead count
- Event-level triadic detections

The downloadable CSV contains both:
1. Summary statistics
2. Complete event-level triad data

Online Application
------------------
https://triad-analysis.streamlit.app

Author
------
Lucas Correia Lima da Silva

Website
-------
https://lu-cas.org
"""
