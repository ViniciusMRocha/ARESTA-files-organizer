import pathlib
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import cv2
import numpy as np
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError)

# current_dir = pathlib.Path.cwd()
# home_dir = pathlib.Path.home()
# print(current_dir)
# print(home_dir)


def convert_single_page(page):
    pdf_writer = PdfFileWriter()
    pdf_writer.addPage(page)
    with open('../out/temp/temp.pdf', "wb") as output_file:
        pdf_writer.write(output_file)

    images = convert_from_path('../out/temp/temp.pdf')
    images[0].save('../out/temp/temp.pdf', 'JPEG')


def compare_images(flag_img_path, compared_img_path):

    flag_img = cv2.imread(flag_img_path)
    compared_img = cv2.imread(compared_img_path)

    if flag_img.shape == compared_img.shape:
        # Images have the same size and channel
        difference = cv2.subtract(flag_img, compared_img)
        blue, read, green = cv2.split(difference)

        if cv2.countNonZero(blue) == 0 and cv2.countNonZero(read) == 0 and cv2.countNonZero(green) == 0:
            # Files are the same
            return True
        # files are not equal
        return False


pdf_path = '../data/test-input.pdf'
input_pdf = PdfFileReader(str(pdf_path))
input_length = input_pdf.getNumPages()
pdf_merger = PdfFileMerger()
new_list = []
output_counter = 0
for page in range(input_length):
    flag_writer = PdfFileWriter()
    flag_writer.addPage(input_pdf.getPage(page))
    with open('../out/temp/temp{}.pdf'.format(page), "wb") as output_file:
        flag_writer.write(output_file)

    images = convert_from_path('../out/temp/temp{}.pdf'.format(page))
    images[0].save('../out/temp/page{}.jpeg'.format(page))

    flag_img_path = '../out/temp/page0.jpeg'
    compared_img_path = '../out/temp/page{}.jpeg'.format(page)
    compare_result = compare_images(flag_img_path, compared_img_path)
    print('Page {} is {}'.format(page, compare_result))

    if compare_result:
        print(new_list)
        with open('../out/output-{}.pdf'.format(output_counter), "wb") as output_file:
            pdf_merger.write(output_file)
        output_counter = output_counter+1
        pdf_merger = PdfFileMerger()
        new_list = []
    else:
        new_list.append(compare_images(flag_img_path, compared_img_path))
        pdf_merger.append('../out/temp/temp{}.pdf'.format(page))


# Flag in on first page
# single_file save the first page only
# flag_path = input_pdf.getPage(0)
# flag_images = convert_from_path('../data/flag.pdf')
# print(flag_path)
# flag_images[0].show()

# pdf_writer = PdfFileWriter()
# for n in range(1, 4):
#     page = input_pdf.getPage(n)
#     pdf_writer.addPage(page)

# print(pdf_writer.getNumPages())

# with open('../out/out.pdf', "wb") as output_file:
#     pdf_writer.write(output_file)
