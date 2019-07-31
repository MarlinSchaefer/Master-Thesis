import os

def images_path():
    path = os.path.split(os.path.abspath(__file__))[0]
    path = os.path.split(path)[0]
    path = os.path.join(path, 'images')
    return path
    
