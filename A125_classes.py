class Camera:
    def __init__(self, marca, filmando=False):
        self.marca = marca
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            return f'{self.marca} já está filmando.'

        self.filmando = True

        return f'{self.marca} agora está filmando...'
    
    def parar_filmagem(self):
        if not self.filmando:
            return f'{self.marca} não está filmando nada.'

        self.filmando = False

        return f'{self.marca} parou de filmar.'

    def fotografar(self):
        if self.filmando:
            return 'Você não pode tirar fotos enquanto filma.'

        return 'Foto tirada!'

camera = Camera('Canon')

print(f'Marca -> {camera.marca}\n')
print(camera.parar_filmagem())
print(camera.fotografar())
print(camera.parar_filmagem())
print(camera.filmar())
print(camera.filmar())
print(camera.fotografar())
print(camera.parar_filmagem())
print(camera.filmar())
print(camera.fotografar())
print(camera.filmar())
print(camera.parar_filmagem())
print(camera.fotografar(), '\n')

###################################################################################################

class Camera:
    def __init__(self, name, recording=False):
        self.name = name
        self.recording = recording
    
    def record(self):
        if self.recording:
            print(f'{self.name} is already recording...')

        else:
            self.recording = True

            print(f'{self.name} is now recording...')

    def is_recording(self):
        if self.recording:
            print(f'{self.name} is recording...')
        
        else:
            print(f'{self.name} is not recording...')

    def stop_recording(self):
        if self.recording:
            self.recording = False

            print(f'{self.name} stopped recording...')

        else:
            print(f'{self.name} was not recording...')

    def take_photo(self):
        if self.recording:
            print(f'{self.name} cannot take a photo while recording...')
        
        else:
            print(f'Say cheese!')

camera = Camera('Camera')

camera.is_recording()
camera.stop_recording()
camera.take_photo()
camera.stop_recording()
camera.record()
camera.is_recording()
camera.record()
camera.take_photo()
camera.stop_recording()
camera.is_recording()
camera.record()
camera.is_recording()
camera.take_photo()
camera.record()
camera.stop_recording()
camera.take_photo()
