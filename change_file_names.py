import os
import sys

#just update this global array to add whatever extensions you are woring with
#yes global variables bad - blah blah blah
image_file_extension_array = ["jpg", "png", "exif", "tiff", "gif"]


def main():
    """ use: change_file_names.py directory_where_images_are name_files_to
    """

    if len(sys.argv) < 3:
        print("error: usage: change_file_names.py directory_where_images_are name_files_to")
        print("ex. change_file_names.py /desktop/images new_image_name")
        return

    directory = sys.argv[1]
    name_files_to = sys.argv[2]

    print("\n************************ CHANGE IMAGE NAMES ************************\n")

    print("\nAccessing directory: '{}'\n".format(directory))

    if check_if_valid_directory(directory):
        changeFileNames(directory, name_files_to)
    else:
        print("Directory doesnt exist. Double Check the location and run again")

    # for arg in sys.argv[:]:
    #     print(arg)

def check_if_valid_directory(directory):
    return (os.path.isdir(directory)) #is this a valid directory

def changeFileNames(images_directory, name_files_to):
    #cur_dir = os.getcwd()'

    # image_file_extension_array = ["jpg", "png", "exif", "tiff", "gif"]

    #get files in curent directory
    file_list = os.listdir(images_directory)

    file_changed_counter = 0

    #print("file list = {}".format(file_list))

    for i, filename in enumerate(file_list):
        #print("file {} : {}".format(i, filename))
        #os.rename(filename, filename[7:])

        if not os.path.isfile(os.path.join(images_directory, filename)):
            print("")
            print("Filename '{}' not a file -> skipping".format(filename))
            continue

        filename = filename.lower()
        file_split = filename.split(".")
        #print("img format = {}".format(file_split[-1]))
        file_extension = file_split[-1] #take last element of array (should be img format)

        if file_split[-1] in image_file_extension_array:

            image_number = str(file_changed_counter).zfill(4) #counting file names we want to change

            new_image_name = "{} {}.{}".format(name_files_to, image_number, file_extension)

            #make sure we have the directory and the name now
            filename = "{}/{}".format(images_directory, filename)
            new_image_name = "{}/{}".format(images_directory, new_image_name)

            print("\nTrying to Change...")
            print("     --> current filename and location = {}".format(filename))
            print("     --> new filename and location = {}".format(new_image_name))

            try:
                exists = os.path.isfile(new_image_name)
                if exists:
                    print("     Error: File exists : NOT changing the name")
                else:
                    os.rename(filename, new_image_name)
                    file_changed_counter += 1
            except:
                print("     Error: File name exists already: {}".format(new_image_name))

    print("\nChanged {0} files.\n".format(file_changed_counter))

if __name__== "__main__":
    main()