#!/usr/bin/env python3
"""Ontario exit capacity calculator (OBC 3.4). See README.md for sources."""
import argparse, json, os, sys
D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "exit-data.json")))

def main():
    p = argparse.ArgumentParser(description="Ontario exit width, one-exit and travel distance check")
    p.add_argument("--occupants", type=float, required=True)
    p.add_argument("--occupancy", default="D", choices=["A", "B", "C", "D", "E", "F1", "F2", "F3"])
    p.add_argument("--area", type=float, default=0, help="floor area served, m2")
    p.add_argument("--travel", type=float, default=0, help="longest travel distance to an exit, m")
    p.add_argument("--sprinklered", action="store_true")
    a = p.parse_args()
    f = D["width_factors_mm_per_person"]
    print(f"Occupant load: {a.occupants:g} persons, Group {a.occupancy}")
    print(f"Minimum aggregate exit width through doorways/corridors: {a.occupants * f['doorways_corridors_passageways_ramps_1_in_8_or_less']:.0f} mm")
    print(f"Minimum aggregate width of exit stairs (rise <=180, run >=280): {a.occupants * f['stairs_rise_max_180mm_run_min_280mm']:.0f} mm")
    print(f"Minimum aggregate width of other stairs / steep ramps: {a.occupants * f['other_stairs_and_ramps_steeper_than_1_in_8']:.0f} mm")
    td = D["max_travel_distance_m_table_3.4.2.2"].get(a.occupancy)
    if td:
        lim = td[1] if a.sprinklered else td[0]
        print(f"Maximum travel distance (Table 3.4.2.2): {lim} m" + (f" -> travel {a.travel:g} m {'OK' if a.travel <= lim else 'EXCEEDS'}" if a.travel else ""))
    key = a.occupancy
    one = None
    if a.sprinklered:
        mx = D["one_exit_sprinklered_table_3.4.2.1B_max_area_m2"].get(key)
        one = mx is not None and a.area <= mx and a.travel <= 25 and a.occupants <= 60
        print(f"One exit (sprinklered, Table 3.4.2.1.B): max floor area {mx} m2, travel <= 25 m, load <= 60, building <= 2 storeys -> {'MAY BE PERMITTED - verify all conditions' if one else 'NOT permitted on area/travel/load alone' if mx else 'not applicable'}")
    else:
        row = D["one_exit_not_sprinklered_table_3.4.2.1A"].get(key)
        if row:
            one = a.area <= row["max_area_m2"] and a.travel <= row["max_travel_m"] and a.occupants <= 60
            print(f"One exit (not sprinklered, Table 3.4.2.1.A): max floor area {row['max_area_m2']} m2, max travel {row['max_travel_m']} m, load <= 60, building <= 2 storeys -> {'MAY BE PERMITTED - verify all conditions' if one else 'NOT permitted'}")
    print("Preliminary only - verify against the OBC in force.")

if __name__ == "__main__":
    main()
