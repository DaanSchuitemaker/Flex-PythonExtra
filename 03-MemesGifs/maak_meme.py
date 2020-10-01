from PIL import Image, ImageFont, ImageDraw
achtergrond = Image.open("meme_background.jpg")

breedte = achtergrond.width
hoogte = achtergrond.height

print("De afbeelding is " + str(breedte) + " pixels breed en " + str(hoogte) + " pixels hoog")

print(achtergrond.format, achtergrond.size, achtergrond.mode)

lettertype = ImageFont.truetype("impact.ttf", 40)

tekengebied = ImageDraw.Draw(achtergrond)
tekst1 = "C H E E S E "
tekst2 = "Bottom Text"
tekengebied.multiline_text((138,10), tekst1, font=lettertype, fill=(1000,1000,1000))
tekengebied.multiline_text((131,285), tekst2, font=lettertype, fill=(1000,1000,1000))

achtergrond.show()
achtergrond.save("meme_met_tekst.jpg")

