from PIL import Image
afbeelding = Image.open("skipper.png")

afbeelding.show()

breedte = afbeelding.width
hoogte = afbeelding.height

helft_breedte = breedte // 2
helft_hoogte = hoogte // 2

nieuwe_afmeting = (helft_breedte, helft_hoogte)

kleinere_afbeelding = afbeelding.resize(nieuwe_afmeting)

kleinere_afbeelding.save('skipper_klein.png')
