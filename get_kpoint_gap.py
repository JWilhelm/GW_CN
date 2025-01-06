# File path
file_path = 'bandstructure_SCF_and_G0W0'

# Initialize variables
data = []
kpoint = None

# Parse the file
with open(file_path, 'r') as file:
    for line in file:
        # Check for kpoint line
        if 'kpoint' in line:
            parts = line.split()
            kpoint = int(parts[1])
            if kpoint > 1:
                data.append((kpoint, eps_occ_max, eps_vir_min, eps_vir_min - eps_occ_max))
            eps_occ_max = -1000.0
            eps_vir_min = 1000.0

        # Check for occupied states line (occ)
        elif 'occ' in line:
            parts = line.split()
            eps_g0w0 = float(parts[7])  # Assuming the 4th value is eps_g0w0
            eps_occ_max = max(eps_g0w0, eps_occ_max)

        # Check for virtual states line (vir)
        elif 'vir' in line:
            parts = line.split()
            eps_g0w0 = float(parts[7])  # Assuming the 4th value is eps_g0w0
            eps_vir_min = min(eps_g0w0, eps_vir_min)  # Use min here for virtual states

# Analyze the data
results = []
by_kpoint = {}
for entry in data:
    kpoint, eps_occ_max, eps_vir_min, gap = entry
    print(entry)

