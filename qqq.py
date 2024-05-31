import zipfile
import os

def extract_zip(zip_path, extract_to):
    """
    Extract a zip file to the specified directory.

    :param zip_path: The path to the zip file
    :param extract_to: The directory where the files should be extracted
    """
    # Ensure the output directory exists
    os.makedirs(extract_to, exist_ok=True)
    
    # Open the zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Extract all the contents to the specified directory
        zip_ref.extractall(extract_to)
        print(f'Files extracted to {extract_to}')

if __name__ == "__main__":
    zip_path = '/workspaces/Beds-wards-V1/map.zip'  # Cambia esto por la ruta de tu archivo zip
    extract_to = '/workspaces/Beds-wards-V1/servidor_minecraft'  # Cambia esto por el directorio donde quieres extraer los archivos
    
    extract_zip(zip_path, extract_to)
