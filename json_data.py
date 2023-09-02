from json import load, dump

def calculate_circle_properties(radius):
    area = 3.14159 * (radius ** 2)
    circumference = 2 * 3.14159 * radius
    return area, circumference

def update_json_file(file_path):
    with open(file_path, 'r+') as file:
        data = load(file)  
        circles = data['circles']
        for circle in circles:
            radius = circle['radius']
            area, circumference = calculate_circle_properties(radius)
            circle['area'] = area
            circle['circumference'] = circumference
        file.seek(0)
        dump(data, file, indent=4)
        file.truncate()
    with open(file_path, 'r') as file:
        n_data = load(file)
        return n_data