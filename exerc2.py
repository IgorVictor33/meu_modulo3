import qrcode
telefone = input('qual o seu telefone')
img = qrcode.make(f'api.whatsapp.com/send/?phone={telefone}')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")