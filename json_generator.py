import os, json

OUTPUTS_DIR   = "outputs"
AIRFOIL_IDS   = [72, 1248]
METHODS       = ["PARSEC", "NURBS", "HicksHenne", "CST", "DBM"]
STEP_INTERVAL = 25
MAX_STEP      = 10000

site_data = {}
for aid in AIRFOIL_IDS:
    # locate the folder e.g. "72_Ah93-W-480B"
    for name in os.listdir(OUTPUTS_DIR):
        if name.startswith(f"{aid}_"):
            base = os.path.join(OUTPUTS_DIR, name)
            site_data[str(aid)] = {}
            for method in METHODS:
                method_dir = os.path.join(base, method)
                if os.path.isdir(method_dir):
                    frames = []
                    for step in range(0, MAX_STEP+1, STEP_INTERVAL):
                        fname = f"{method}_Step_{step}.png"
                        path  = os.path.join(method_dir, fname)
                        if os.path.isfile(path):
                            # use web-relative paths for GitHub Pages
                            frames.append(path.replace("\\", "/"))
                    if method == 'HicksHenne':
                        method = 'Hicks-Henne'
                    if method == 'DBM':
                        method = 'Design-by-Morphing'
                    if method == 'CST':
                        method = 'Kulfan (CST)'
                    site_data[str(aid)][method] = frames
            break

with open("site_data.json", "w") as f:
    json.dump(site_data, f, indent=2)

