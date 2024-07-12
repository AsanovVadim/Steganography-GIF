from PIL import Image
from re import findall


def stega_decrypt(txtfile):

    a = []
    keys = []
    img = Image.open('./Result/newimage.gif')
    f = txtfile
    y = str([line.strip() for line in f])

    for i in range(len(findall(r'\d+\s\((\d+)\,', y))):
        coords = (
            (
                int(findall(r'\((\d+)\,', y)[i]),
                int(findall(r'\,\s(\d+)\)', y)[i])
            )
        )
        frame = int(findall(r'(\d+)\s\(', y)[i])
        keys.append((frame, coords))

    for key in keys:
        frame, coords = key
        img.seek(frame)
        pix = img.load()
        a.append(pix[coords][0])

    return ''.join([chr(elem) for elem in a])