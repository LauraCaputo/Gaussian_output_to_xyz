import os
import glob

periodic_table = {
    1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N', 8: 'O', 9: 'F', 10: 'Ne',
    11: 'Na', 12: 'Mg', 13: 'Al', 14: 'Si', 15: 'P', 16: 'S', 17: 'Cl', 18: 'Ar', 19: 'K', 20: 'Ca',
    21: 'Sc', 22: 'Ti', 23: 'V', 24: 'Cr', 25: 'Mn', 26: 'Fe', 27: 'Co', 28: 'Ni', 29: 'Cu', 30: 'Zn',
    31: 'Ga', 32: 'Ge', 33: 'As', 34: 'Se', 35: 'Br', 36: 'Kr', 37: 'Rb', 38: 'Sr', 39: 'Y', 40: 'Zr',
    41: 'Nb', 42: 'Mo', 43: 'Tc', 44: 'Ru', 45: 'Rh', 46: 'Pd', 47: 'Ag', 48: 'Cd', 49: 'In', 50: 'Sn',
    51: 'Sb', 52: 'Te', 53: 'I', 54: 'Xe', 55: 'Cs', 56: 'Ba', 57: 'La', 58: 'Ce', 59: 'Pr', 60: 'Nd',
    61: 'Pm', 62: 'Sm', 63: 'Eu', 64: 'Gd', 65: 'Tb', 66: 'Dy', 67: 'Ho', 68: 'Er', 69: 'Tm', 70: 'Yb',
    71: 'Lu', 72: 'Hf', 73: 'Ta', 74: 'W', 75: 'Re', 76: 'Os', 77: 'Ir', 78: 'Pt', 79: 'Au', 80: 'Hg',
    81: 'Tl', 82: 'Pb', 83: 'Bi', 84: 'Po', 85: 'At', 86: 'Rn', 87: 'Fr', 88: 'Ra', 89: 'Ac', 90: 'Th',
    91: 'Pa', 92: 'U', 93: 'Np', 94: 'Pu', 95: 'Am', 96: 'Cm', 97: 'Bk', 98: 'Cf', 99: 'Es', 100: 'Fm',
    101: 'Md', 102: 'No', 103: 'Lr', 104: 'Rf', 105: 'Db', 106: 'Sg', 107: 'Bh', 108: 'Hs', 109: 'Mt',
    110: 'Ds', 111: 'Rg', 112: 'Cn', 113: 'Nh', 114: 'Fl', 115: 'Mc', 116: 'Lv', 117: 'Ts', 118: 'Og'
}

def read_gaussian_output(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    indices = [i for i, line in enumerate(lines) if "Standard orientation" in line]
    if not indices:
        raise ValueError("Standard orientation section not found.")

    start_index = indices[-1]
    while "-----" not in lines[start_index]:
        start_index += 1
    start_index += 4

    end_index = start_index
    while "-----" not in lines[end_index].strip():
        end_index += 1

    atoms = []
    for line in lines[start_index:end_index]:
        parts = line.split()
        if len(parts) >= 6:
            atomic_number = int(parts[1])
            x, y, z = float(parts[3]), float(parts[4]), float(parts[5])
            atoms.append((atomic_number, x, y, z))

    return atoms

def write_xyz_file(atoms, output_filename):
    with open(output_filename, 'w') as file:
        file.write(f"{len(atoms)}\n")
        file.write("Optimized structure from Gaussian output\n")
        for atomic_number, x, y, z in atoms:
            element = periodic_table[atomic_number]
            file.write(f"{element} {x} {y} {z}\n")

log_files = glob.glob('*.log')
if not log_files:
    raise FileNotFoundError("No Gaussian log files found in the current directory.")
log_file = log_files[0]  # Process the first found log file

atoms = read_gaussian_output(log_file)
write_xyz_file(atoms, 'output.xyz')
