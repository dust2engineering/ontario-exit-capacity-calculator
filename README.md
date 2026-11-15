# Ontario Exit Capacity Calculator

Calculates the minimum aggregate width of exits from the occupant load, tests whether a floor area qualifies for a single exit, and checks the travel distance, using Ontario Building Code Subsection 3.4.2 and Article 3.4.3.2.

**Live web tool:** https://dust2engineering.github.io/ontario-exit-capacity-calculator/web/

## How it works

- Aggregate exit width = occupant load x 6.1 mm/person (doorways, corridors, passageways), x 8 mm/person (stairs with rise <= 180 mm and run >= 280 mm), or x 9.2 mm/person (other stairs and steep ramps).
- One-exit test against Table 3.4.2.1.A (not sprinklered) or 3.4.2.1.B (sprinklered), with the standing conditions: building <= 2 storeys, occupant load <= 60, sprinklered travel <= 25 m.
- Maximum travel distance from Table 3.4.2.2 by occupancy group and sprinkler status.

## Data in this repository

- exit-data.json — every factor and table used, in machine-readable form.

## Command line

```bash
python3 exit_capacity.py --occupants 120 --occupancy A --area 450 --travel 22 --sprinklered
```

## Worked examples

- [restaurant-two-exits.md](examples/restaurant-two-exits.md)
- [small-office-one-exit.md](examples/small-office-one-exit.md)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: Fire and life safety. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
