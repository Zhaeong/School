import media

def same_dimensions():
    filename = media.choose_file()
    pic = media.load_picture(filename)
    filename2 = media.choose_file()
    pic2 = media.load_picture(filename2)
    
    h1=media.get_height(pic)
    w1=media.get_width(pic)
    h2=media.get_height(pic2)
    w2=media.get_width(pic2)
    if h1==h2 and w1==w2:
        print "true"
    else:
        print "false"

def copyright():
    pic=media.create_picture(20,20)
    black=media.black
    media.add_oval(pic,0,0,16,16,black)
    media.add_text(pic, 6,3,"C",black)
    media.show(pic)
    return pic

def moderate_blue(pic):
    new_pic=media.copy(pic)
    for pix in new_pic:
        red=media.get_red(pix)
        green=media.get_green(pix)
        red1=int(red)
        green1=int(green)
        modblue=(red1+green1)/2
        media.set_blue(pix, modblue)
        media.show(new_pic)
    return new_pic
    
