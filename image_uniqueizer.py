import uuid
import random
import os

from tkinter import *
from PIL import Image


class Window(Frame):

    def __init__(self, master=None, size='400x300'):
        Frame.__init__(self, master)
        self.master = master
        self.master.geometry(size)
        self.e1 = Entry(self.master)
        self.e2 = Entry(self.master)
        self.init_window()

    def init_window(self):
        self.master.title('Image uniqueizer')
        Label(self.master,
              text="Input path").grid(row=0)
        Label(self.master,
              text="Output path").grid(row=1)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)

        Button(self.master,
               text='Bye',
               command=self.master.quit).grid(row=3,
                                              column=0,
                                              sticky=W,
                                              pady=4)
        Button(self.master,
               text='Randomize',
               command=self.random_image_generator).grid(row=3,
                                                         column=1,
                                                         sticky=W,
                                                         pady=4)

    def random_image_generator(self):
        path_input = self.e1.get()
        path_output = self.e2.get()
        if path_input == '' or path_output == '':
            w = Message(self.master, text='Please, insert input and output',
                        width=100)
            w.grid(row=2)
        else:
            try:
                for file in os.listdir(path_input):
                    if file.endswith('.png') or file.endswith('.jpg') \
                            or file.endswith('.jpeg'):
                        with open(path_input + '/' + file, 'rb') as image_file:
                            image = Image.open(image_file)
                            image_without_exif = Image.new(image.mode, image.size)
                            image_without_exif.putdata(image.getdata())
                            pixels = image_without_exif.load()
                            for pixel in range(100):
                                pixels[random.randint(0, image.size[0] - 1),
                                       random.randint(0, image.size[1]) - 1] = (
                                    255, 255, 255)
                            image_without_exif.save(
                                path_output + '/' + str(uuid.uuid4()) + '.jpeg')
                w = Message(self.master, text='Success',
                            width=100)
                w.grid(row=2)
            except Exception as e:
                w = Message(self.master, text=e,
                            width=100)
                w.grid(row=2)

        # self.e1.delete(0, END)
        # self.e2.delete(0, END)


# path_input = '/home/yura/work/image_generator/input'
# path_output = '/home/yura/work/image_generator/output'


if __name__ == '__main__':
    app = Window(Tk(), '400x300')
    app.master.mainloop()
