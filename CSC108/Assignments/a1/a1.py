import media

def guess_captcha(str1, str2):
    '''(str1, str2) -> bool.
    Returns True if two strings are the same and False otherwise.'''
    
    return str1 == str2
    

def get_picture_width(string):
    '''(string) -> int
    Returns width of picture in pixels that will be used to display str.'''
    
    return len(string) * 10

    
def word_to_pic(pic_word):
    '''(pic_word) -> Picture
    Return a picture that contains a string.'''
    
    p = media.create_picture(get_picture_width(pic_word), 20)
    p.add_text(media.black, 0, 0, pic_word)
    return p


def count_black(pic):
    '''(Pic) -> int
    Returns the quantity of pixels in pic that are black as an integer.'''
    
    black_pixels=0
    for pix in pic:
        if media.get_color(pix) == media.black:
            black_pixels += 1
    return black_pixels
    

    
def strikethrough(pic):
    '''(Pic) -> Picture
    Return a copy of the picture with a black line added horizontally through 
    the middle of the picture. The line's thickness is 10% of the height of the picture. '''
    
    p = media.copy(pic)
    height_rect = p.get_height() / 10
    width_rect  = p.get_width()
    y_upper_left = p.get_height() / 2
    x_upper_left = 0
    media.add_rect_filled(p, x_upper_left, y_upper_left, width_rect, height_rect, media.black)
    return p
    
    
    
def widen(original):
    '''(original) -> Picture 
    Return a new picture that is twice as wide as the given picture.'''
    
    new_pic = media.create_picture(original.get_width() * 2, original.get_height())
    
    for pix in original:
        original_x = pix.get_x()
        original_y = pix.get_y()
        new_pic.get_pixel(2 * original_x, original_y).set_color(pix.get_color())
        new_pic.get_pixel(2 * original_x + 1, original_y).set_color(pix.get_color())
    return new_pic 
        
    

def overlay_color(pix1, pix2):
    '''(Pix1, Pix2) -> Color
    Return a new color made up of 80% of the color values of the first pixel 
    and 20% of the color values of the second pixel.'''
    
    r1 = int(media.get_red(pix1))
    r2 = int(media.get_red(pix2))
    g1 = int(media.get_green(pix1))
    g2 = int(media.get_green(pix2))
    b1 = int(media.get_blue(pix1))
    b2 = int(media.get_blue(pix2))

    red   = (r1 * 0.8) + (r2 * 0.2)
    green = (g1 * 0.8) + (g2 * 0.2)
    blue  = (b1 * 0.8) + (b2 * 0.2)
    return media.create_color(red, green, blue)
    
    
    


def overlay_picture(pic, pic2):
    '''(Pic, Pic2) -> Picture Return a new picture with each pixel's 
    color values made up of 80% of the color values of the corresponding pixel 
    in the first picture and 20% of the color values of the corresponding pixel 
    in the second picture'''
    
    new_pic=media.copy(pic)

    for pix in new_pic:
        x = media.get_x(pix)
        y = media.get_y(pix)
        p1 = media.get_pixel(pic, x,y)
        p2 = media.get_pixel(pic2,x,y)
        red   = (int(p1.get_red()) * 0.8) + (int(p2.get_red()) * 0.2)
        green = (int(p1.get_green()) * 0.8) + (int(p2.get_green()) * 0.2)
        blue  = (int(p1.get_blue()) * 0.8) + (int(p2.get_blue()) * 0.2)        
        new_color = media.create_color(red, green, blue)
        media.set_color(pix, new_color)
    return new_pic
    
    

def flip(pic):
    '''(Pic) -> Picture 
    Return a new picture that contains the pixels of the original picture flipped across the vertical axis.'''
    
    copy  = media.copy(pic)
    max_x = media.get_width(pic)
    max_y = media.get_height(pic)
    
    for x in range(max_x/2):
        for y in range(max_y):
            originalpix = copy.get_pixel(x,y)
            reversepix  = copy.get_pixel((max_x - x - 1), y)
            color = media.get_color(originalpix)
            reversecolor = media.get_color(reversepix)
            media.set_color(originalpix,reversecolor)
            media.set_color(reversepix,color)
    return copy
    

        

    

if __name__ == "__main__":
    pic = media.create_picture(50, 50, media.red)
    pic.inspect()
    pic2 = media.create_picture(50, 50, media.blue)
    pic2.inspect()
    str1 = 'redundancy'
    str2 = 'redundancy'
    filename = media.choose_file()
    mypic = media.load_picture(filename)