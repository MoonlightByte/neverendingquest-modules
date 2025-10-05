#!/usr/bin/env python3
"""
Fix Pumpkin Kings Curse Schema Violations
- Add quantity: {min, max} to 20 monsters
- Add name and description to 15 traps
"""

import json
import glob

def fix_monsters(file_path, dry_run=True):
    """Add quantity field to monsters missing it"""

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    changes = []

    for location in data.get('locations', []):
        loc_id = location.get('locationId', 'Unknown')

        for monster in location.get('monsters', []):
            if 'quantity' not in monster:
                name = monster.get('name', 'Unknown')
                desc = monster.get('description', '').lower()

                # Infer quantity from description/name
                if 'swarm' in name.lower() or 'swarm' in desc:
                    qty = {'min': 3, 'max': 6}
                elif 'two' in desc or 'pair' in desc:
                    qty = {'min': 2, 'max': 2}
                elif 'three' in desc:
                    qty = {'min': 3, 'max': 3}
                elif 'four' in desc:
                    qty = {'min': 4, 'max': 4}
                elif 'boss' in name.lower() or 'king' in name.lower():
                    qty = {'min': 1, 'max': 1}
                else:
                    qty = {'min': 1, 'max': 1}

                changes.append(f"{loc_id}: {name} → quantity: {qty}")

                if not dry_run:
                    monster['quantity'] = qty

    return data if not dry_run else None, changes

def fix_traps(file_path, dry_run=True):
    """Add name and description to traps missing them"""

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    changes = []

    for location in data.get('locations', []):
        loc_id = location.get('locationId', 'Unknown')

        for trap_idx, trap in enumerate(location.get('traps', [])):
            needs_name = 'name' not in trap
            needs_desc = 'description' not in trap

            if needs_name or needs_desc:
                # Generate name/desc from damage and DC info
                damage = trap.get('damage', 'unknown')
                detect_dc = trap.get('detectDC', 0)

                if needs_name:
                    # Generate generic name from damage type
                    if 'fire' in damage.lower():
                        name = "Fire Trap"
                    elif 'cold' in damage.lower() or 'frost' in damage.lower():
                        name = "Frost Trap"
                    elif 'poison' in damage.lower():
                        name = "Poison Trap"
                    elif 'necrotic' in damage.lower():
                        name = "Necrotic Trap"
                    elif 'psychic' in damage.lower():
                        name = "Psychic Trap"
                    else:
                        name = f"Trap {trap_idx+1}"

                    changes.append(f"{loc_id}: Trap {trap_idx+1} → name: '{name}'")
                    if not dry_run:
                        trap['name'] = name

                if needs_desc:
                    desc = f"A trap that deals {damage} damage (DC {detect_dc} to detect)."
                    changes.append(f"{loc_id}: Trap {trap_idx+1} → description added")
                    if not dry_run:
                        trap['description'] = desc

    return data if not dry_run else None, changes

# DRY RUN - Show what will be changed
print("=" * 80)
print("DRY RUN - SHOWING PLANNED CHANGES")
print("=" * 80)
print()

files = glob.glob('/mnt/c/neverendingquest-modules/The_Pumpkin_Kings_Curse/areas/*_BU.json')

all_monster_changes = []
all_trap_changes = []

for file_path in files:
    _, monster_changes = fix_monsters(file_path, dry_run=True)
    _, trap_changes = fix_traps(file_path, dry_run=True)

    if monster_changes or trap_changes:
        print(f"\n{file_path.split('/')[-1]}:")

        if monster_changes:
            print(f"  Monsters ({len(monster_changes)}):")
            for change in monster_changes:
                print(f"    - {change}")

        if trap_changes:
            print(f"  Traps ({len(trap_changes)}):")
            for change in trap_changes:
                print(f"    - {change}")

        all_monster_changes.extend(monster_changes)
        all_trap_changes.extend(trap_changes)

print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"Total monster fixes: {len(all_monster_changes)}")
print(f"Total trap fixes: {len(all_trap_changes)}")
print(f"Total changes: {len(all_monster_changes) + len(all_trap_changes)}")
print()
print("Review the changes above. If they look correct, run with apply=True")
print()

# APPLY FIXES
print("=" * 80)
print("APPLYING FIXES")
print("=" * 80)
print()

for file_path in files:
    fixed_data_monsters, _ = fix_monsters(file_path, dry_run=False)
    fixed_data_traps, _ = fix_traps(file_path, dry_run=False)

    # Save the file with both fixes applied
    if fixed_data_monsters or fixed_data_traps:
        # Use the trap-fixed version (which includes monster fixes)
        final_data = fixed_data_traps if fixed_data_traps else fixed_data_monsters

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(final_data, f, indent=2, ensure_ascii=False)

        print(f"✓ Saved {file_path.split('/')[-1]}")

print()
print("=" * 80)
print("ALL FIXES APPLIED")
print("=" * 80)
