from PIL import Image, ImageDraw
from rich.tree import Tree
from rich import print


class learn:
    def __init__(self, name='', children={}):
        self.name = name
        self.children = children
##whayyyy


fortune = learn('Fortune', {'vast': 'YES', 'medium': 'YES', 'little': 'NO'})

tution = learn('tution', {'tution': 'YES', 'noTution': 'NO'})

edu = learn('edu', {'CSE': tution, 'EEE': 'NO', 'Mecha': tution})

marital = learn('marital', {'married': 'NO', 'bachelor': edu, 'super': 'NO'})

age = learn('age', {'<18': 'YES', '18-36': marital, '>55': fortune})


strappend = ''
postures = []


def linePrinter(lst):
    prevpos = 0
    global strappend
    for pos in postures:
        strappend += ' '*(pos-prevpos+1)+'|'
        print(' '*(pos-prevpos+1), end='|')
        prevpos = pos

    return prevpos


def treebuild(root, space):
    global strappend
    if type(root) != type(age):
        return

    mline = len(root.name)
    prevpos = linePrinter(postures)
    spc = ' '*(space-prevpos)
    strappend += spc+'-' + root.name+'\n'

    print(spc+'-', root.name)
    for i, child in enumerate(root.children):
        spc = ' '*(space-prevpos+2)
        charlen = len(child)
        ysn = root.children[child]
        prevpos = linePrinter(postures)

        if ysn == 'YES' or ysn == 'NO':
            strappend += spc+' +'+'-' * mline + \
                '-{}=>({})'.format(child, ysn) + '\n'
            print(spc, '+', '-' *
#                   mline, '-{}=>({})'.format(child, ysn))
                    mline, '-{}=>({})'.format(child, ysn))

        else:
            strappend += spc + ' |+' + '-' * \
                mline + '-{}'.format(child)+'\n'
            print(spc, '|+', '-'*mline, '-{}'.format(child))
            postures.append(space)
            if i == len(root.children)-1:
                postures.remove(space)
            treebuild(ysn,  mline+len(spc)+charlen)
            if postures:
                postures.pop(-1)


treebuild(age, 0)
# strappend

print(strappend)
image = Image.new("RGB", (800, 700), "white")
d1 = ImageDraw.Draw(image)
# font = ImageFont.truetype(size=42)
d1.text((28, 36), strappend, fill='green')
image.show()
image.save("tree.jpg")
