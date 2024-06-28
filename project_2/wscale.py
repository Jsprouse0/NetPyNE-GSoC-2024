import json

def load_cell_json(file_path):
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in file {file_path}: {e}")
    return data

def process_cell_data(cell_data):
    soma_geom = cell_data.get('soma', {}).get('geom', {})
    soma_mechs = cell_data.get('soma', {}).get('mechs', {})
    dend_geom = cell_data.get('dend', {}).get('geom', {})
    dend_mechs = cell_data.get('dend', {}).get('mechs', {})

    print("Soma Geometry: ", soma_geom)
    print("Soma Mechanics: ", soma_mechs)
    print("Dendrite Geometry: ", dend_geom)
    print("Dendrite Mechanics: ", dend_mechs)
    
def update_cell_geometry(cell_data, cell_type, diameter, length):
    if (cell_type in cell_data) and ('geom' in cell_data[cell_type]):
        cell_data[cell_type]['geom']['diam'] = float(diameter)   # Updates cell diameter
        cell_data[cell_type]['geom']['L'] = float(length)        # Updates cell length 


def save_cell_data(file_path, cell_data):
    with open(file_path, 'w') as write_file:
        json.dump(cell_data, write_file)

file_path = 'cell.json'

try:
    cell_data = load_cell_json(file_path)
    process_cell_data(cell_data)
    updated_cell = update_cell_geometry(cell_data, input(f"Soma or Dendrite? Answer as ({'soma or dend'}): "
    ), input(f"New Diameter: "), input(f"New length: "))
    
    process_cell_data(cell_data)
    save_cell_data('save.json', cell_data)
except (FileNotFoundError, ValueError) as e:
    print(e)


