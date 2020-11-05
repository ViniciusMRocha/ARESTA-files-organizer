from PIL import Image
from typing import Counter
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
from pdf2image import convert_from_path
import os
import csv
import cv2
import json
import glob
import time
import datetime
import imagehash


def convert_csv_to_json(csv_file_path):
    # csv_file_path = '../data/csv_input.csv'
    json_file_path = '{}.json'.format(csv_file_path[:-4])

    data = {}
    with open(csv_file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for rows in csv_reader:
            id = rows['ID']
            data[id] = rows['Name']

    with open(json_file_path, 'w') as json_file:
        json_file.write(json.dumps(data, indent=4))

    return json_file_path


def compare_images_hash(flag_img_path, page_img_path):
    # hash0 = imagehash.average_hash(Image.open('../data/Flag-Page.jpg'))
    # hash1 = imagehash.average_hash(Image.open('../data/Flag-Page2.jpg'))
    hash0 = imagehash.average_hash(Image.open(flag_img_path))
    hash1 = imagehash.average_hash(Image.open(page_img_path))

    cutoff = 5

    if hash0 - hash1 < cutoff:
        # print('images are similar')
        return True
    else:
        # print('images are not similar')
        return False


def convert_single_page(input_pdf, page, path):
    # Set the file writer
    file_writer = PdfFileWriter()
    # Add the page to the file writer
    file_writer.addPage(input_pdf.getPage(page))
    # Create a new PDF with that one single file
    with open(path, "wb") as output_file:
        file_writer.write(output_file)

    # Converts PDF to image
    images = convert_from_path(path)

    # Saves the image so it can be compared
    images[0].save('{}.jpg'.format(path[:-4]))


def compare_images(flag_img_path, compared_img_path):
    # Set flag and other path to CV2 images
    flag_img = cv2.imread(flag_img_path)
    compared_img = cv2.imread(compared_img_path)

    # compares the shape of the files
    if flag_img.shape == compared_img.shape:
        # Given the images have the same size and channel
        # Check for any differences pixel per pixel
        difference = cv2.subtract(flag_img, compared_img)
        # Save the difference for each color in each variable
        blue, read, green = cv2.split(difference)

        # If each color is 0, there is no difference between the files
        if cv2.countNonZero(blue) == 0 and cv2.countNonZero(read) == 0 and cv2.countNonZero(green) == 0:
            # Files are the same
            return True
        # files are not equal
        return False


def load_map(path_to_map):
    with open(path_to_map) as json_file:
        json_content = json.load(json_file)
        return json_content


def app(file_prefix, pdf_path, output_folder, counter=1, order='asc', map=None):
    startTime = time.time()
    out_temp_path = 'temp'
    input_pdf = PdfFileReader(str(pdf_path))
    input_length = input_pdf.getNumPages()
    pdf_merger = PdfFileMerger()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    print('OUTPUT:', output_folder)
    output_folder = '{}/{}-{}'.format(output_folder, file_prefix, timestamp)
    os.mkdir(output_folder)

    # Loop page by page
    for page in range(input_length):
        # Flag is the first file
        flag_path = '{}/flag.pdf'.format(out_temp_path)
        flag_img_path = '{}/flag.jpg'.format(out_temp_path)

        if page == 0:
            convert_single_page(input_pdf, page, flag_path)
        # Page is not a cover or a flag
        else:
            page_pdf_path = '{}/page-{}.pdf'.format(out_temp_path, page)
            page_img_path = '{}/page-{}.jpg'.format(out_temp_path, page)

            # Convert each page to image
            convert_single_page(input_pdf, page, page_pdf_path)

            # Compares the image to the flag image
            # compare_result = compare_images(flag_img_path, page_img_path)
            compare_result = compare_images_hash(flag_img_path, page_img_path)

            # Prints as reads the file
            print('Page {} is {}'.format(page, compare_result))  # * Logic Check

            # True for when the page matches the flag, false otherwise
            if compare_result:
                # Create new pdf with to save the pages that are not equal to the flag
                with open('{}/{}-{}.pdf'.format(output_folder, file_prefix, counter), "wb") as output_file:
                    pdf_merger.write(output_file)
                # Update the output counter
                if order == 'asc':
                    counter += 1
                elif order == 'desc':
                    counter -= 1

                    # Create a Merger object that will combine the files
                pdf_merger = PdfFileMerger()
            else:
                # Append page to the correspondent pdf
                pdf_merger.append('{}/page-{}.pdf'.format(out_temp_path, page))

            # Remove Page Temp Fies
            os.remove('{}/page-{}.pdf'.format(out_temp_path, page))
            os.remove('{}/page-{}.jpg'.format(out_temp_path, page))

    # Remove Flag File
    os.remove('{}/flag.pdf'.format(out_temp_path))
    os.remove('{}/flag.jpg'.format(out_temp_path))

    # Rename files if map is present
    if map is not None:
        map = convert_csv_to_json(map)
        # Load the map
        map_dict = load_map(map)
        # Get the path to the files to be renamed
        file_list = glob.glob('{}/{}*.pdf'.format(output_folder, file_prefix))
        # Iterate over each file
        for count, file_path in enumerate(file_list, 1):
            # Get the value for each key
            map_value = map_dict["{}".format(count)]
            # Set up new variable name
            new_file_name = '{}/{}-{}-{}.pdf'.format(
                output_folder, file_prefix, count, map_value)
            # Rename the original files
            os.rename(file_path, new_file_name)

    print("\n======= Elapsed Time ==================================")
    endTime = time.time() - startTime
    print(time.strftime("%H:%M:%S", time.gmtime(endTime)))


if __name__ == "__main__":
    # Running APP - Test Large File
    file_prefix = 'Green_Card'
    pdf_path = '../data/Application_Test.pdf'  # 400+ pages
    output_folder = '/Users/viniciusrocha/development/ARESTA-files-organizer/out'
    # app(file_prefix, pdf_path, output_folder)

    # Running APP - Testing Map
    file_prefix = 'Test_File'
    pdf_path = '../data/sample.pdf'
    output_folder = '/Users/viniciusrocha/development/ARESTA-files-organizer/out'
    map = '../data/sample_map.csv'
    app(file_prefix, pdf_path, output_folder, map=map)

    # Running APP - Test Order desc
    file_prefix = 'Test_Order_Desc'
    pdf_path = '../data/sample.pdf'
    counter = 2020
    order = 'desc'
    map = '../data/sample_map.csv'
    output_folder = '/Users/viniciusrocha/development/ARESTA-files-organizer/out'
    app(file_prefix, pdf_path, output_folder, counter, order)

    # Running APP - Test Order Asc
    file_prefix = 'Test_Order_Asc'
    pdf_path = '../data/sample.pdf'
    counter = 2000
    output_folder = '/Users/viniciusrocha/development/ARESTA-files-organizer/out'
    app(file_prefix, pdf_path, output_folder, counter)
