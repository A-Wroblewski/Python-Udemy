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
print(camera.fotografar())
