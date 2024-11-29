import platform
import socket
from pathlib import Path

"""
PROGRAMA PARA GUARDAR DATOS DE UNA PC
"""


class InfoPC:
    @staticmethod
    def save_info_pc():
        try:
            path = Path('info.txt')
            pc_data = f'''INFORMACIÓN DEL COMPUTADOR:
            SISTEMA OPERATIVO: {platform.system()} {platform.version()}
            ARQUITECTURA: {platform.machine()}
            PROCESADOR: {platform.processor()}
            HOSTNAME: {socket.gethostname()}
            IP: {socket.gethostbyname(socket.gethostname())}
            '''

            with open(path, 'w') as file_pc:
                file_pc.write(pc_data)
                print('El archivo se ha guardado con éxito.')

        except Exception as e:
            print(f'Error: {e}')

    @staticmethod
    def read_file():
        try:
            print('Abriendo el Archivo')

            with open('info.txt', 'r') as file:
                file_pc = file.read()
                print(file_pc)

        except Exception as e:
            print(f'Ocurrio un error: {e}')


if __name__ == '__main__':
    pc_info = InfoPC()
    pc_info.save_info_pc()
    pc_info.read_file()
