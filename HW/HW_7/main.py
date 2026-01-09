import Im_PIL

def package_image_main_def():
    file_name_start = 'Image.jpg'
    file_name_stop = "stop.jpg"
    file_name_filter = "stop_filter.jpg"

    print('оберіть тип перетворення!')
    print('0 - відтінки сірого')
    print('1 - серпія')
    print('2 - негатив')
    print('3 - зашумлення')
    print('4 - зміна яскравості')
    print('5 - монохромне зображення')
    print('6 - фільтр-векторизатор')
    mode = int(input('mode:'))
    if (mode == 0): Im_PIL.shades_of_gray(file_name_start, file_name_stop)
    if (mode == 1): Im_PIL.serpia(file_name_start, file_name_stop)
    if (mode == 2): Im_PIL.negative(file_name_start, file_name_stop)
    if (mode == 3): Im_PIL.noise(file_name_start, file_name_stop)
    if (mode == 4): Im_PIL.brightness_change(file_name_start, file_name_stop)
    if (mode == 5): Im_PIL.monochrome(file_name_start, file_name_stop)
    if (mode == 6): Im_PIL.contour_im(file_name_stop, file_name_filter)

    return


if __name__ == '__main__':
    package_image_main_def()
