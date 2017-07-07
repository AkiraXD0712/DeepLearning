# -*- coding: utf-8 -*-
from PIL import Image
import qrcode
import argparse


class Conversion2Str:

    def __init__(self, load_dir, resize):
        self.load_dir = load_dir
        self.width = None
        self.height = None
        self.resize = resize

    def read_image(self):
        image = Image.open(self.load_dir).convert('L')
        self.width, self.height = image.size
        self.height /= 2
        self.width = int(self.width * self.resize)
        self.height = int(self.height * self.resize)
        image = image.resize((self.width, self.height), Image.ANTIALIAS)
        return image

    def transform2str(self, image):
        txt = ''
        unit = 256 / 8
        transform_list = (' ', ',', '+', '1', 'n', 'D', '&', 'M')
        save_dir = self.load_dir[:-3] + 'txt'

        for i in range(self.height-1):
            for j in range(self.width-1):
                val_gray = image.getpixel((j, i))
                val = int(val_gray / unit)
                txt += transform_list[7 - val]
            txt += '\n'

        with open(save_dir, "w") as f:
            f.write(txt)
        return txt

    def create_qrcode(self, txt):
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(txt)
        qr.make(fit=True)
        image = qr.make_image()
        with open(self.load_dir[:-3] + 'png', 'wb') as f:
            image.save(f)
        qr.clear()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
		'--image_dir', 
		type=str, 
		help='location of the image'
	)
    parser.add_argument(
		'--resize', 
		type=float, 
		default=0.06,
		help='rate od resize'
	)
    parser.add_argument(
		'--qrcode', 
		type=bool, 
		help='create QRcode'
	)

    args = parser.parse_args()

    if args.image_dir:
        print('<--------------------Start conversion------------------->')
        convert = Conversion2Str(args.image_dir, resize=args.resize)
        img = convert.read_image()
        result = convert.transform2str(img)
        print(result) 
        print('<--------------------Conversion done-------------------->')
        if args.qrcode:
            convert.create_qrcode(result)
            print('<--------------------QRcode created-------------------->')
    else:
        print('<--------------------Image no found-------------------->')
        pass
