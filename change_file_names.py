import os
import sys


def main():
    """ use: change_file_names.py [directory_where_images_are] [name_files_to] [match_ext]
    """

    if len(sys.argv) < 3:
        print("error: usage: change_file_names.py [directory_where_images_are] [name_files_to]")
        return

    directory = sys.argv[1]
    name_files_to = sys.argv[2]

    print("looking for directory: '{}'".format(directory))
    if check_if_valid_directory(directory):
        changeFileNames(directory, name_files_to)
        print("Accessing Directory")
    else:
        print("Directory doesnt exist. Double Check the location and run again")

    # for arg in sys.argv[:]:
    #     print(arg)

def check_if_valid_directory(directory):
    return True

def changeFileNames(images_directory, name_files_to):
    #cur_dir = os.getcwd()

    # images_directory = "{}/{}".format(cur_dir, "images")
    print(images_directory)
    #get files in curent directory
    file_list = os.listdir(images_directory)

    file_changed_counter = 0

    for i, filename in enumerate(file_list):
        #print("file {} : {}".format(i, filename))
        #os.rename(filename, filename[7:])
        if filename.endswith(".jpg") or filename.endswith(".png"):
            print("")

            file_extension = "jpg"
            image_number = str(file_changed_counter).zfill(4) #counting file names we want to change
            if filename.endswith("jpg"):
                file_extension = "jpg"
            elif filename.endswith("png"):
                file_extension = "png"

            new_image_name = "{} {}.{}".format(name_files_to, image_number, file_extension)

            #make sure we have the directory and the name now
            filename = "{}/{}".format(images_directory, filename)
            new_image_name = "{}/{}".format(images_directory, new_image_name)
            print("--> current filename and location = {}".format(filename))
            print("--> new filename and location = {}".format(new_image_name))

            try:
                exists = os.path.isfile(new_image_name)
                if exists:
                    print("file exists not changing the name")
                else:
                    os.rename(filename, new_image_name)
                    file_changed_counter += 1
            except:
                print("file name exists already: {}".format(new_image_name))

    print("Changed {0} files.".format(file_changed_counter))

if __name__== "__main__":
    main()