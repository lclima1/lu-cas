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

Only pitches beginning at the same onset are considered. Sustained pitches
from previous events are excluded from the triadic evaluation.

Accepted triad types:
- Major
- Minor
- Diminished
- Augmented

Output
------
For each analysed score the script reports:

- Total triads
- Triad-event share (%)
- Triads (% of noteheads)
- Root-position triads (% of noteheads)
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

import streamlit as st
import pandas as pd
import tempfile
from collections import Counter

from music21 import converter, chord, note, stream, meter
