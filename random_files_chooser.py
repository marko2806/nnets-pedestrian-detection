import  random
import shutil
import os, errno
from os import path
from os import listdir

# Put do direktorija u kojem se nalaze direktoriji images i labels
start_path = 'C:\\nnets\\dhd_campus\\val'
#start_path = 'C:/Users/Berislav/Desktop/4.GODINA/7.semestar/Neuronske mreze/projekt/test'

# Ciljni direktorij
destination_path = 'C:\\nnets\\dhd_campus_new\\val'
#destination_path = 'C:/Users/Berislav/Desktop/4.GODINA/7.semesta/Neuronske mreze/projekt/test_destination'

# Postotak slika kopiranih u destination_path
p = 0.25

# Diretkorij gdje se nalaze slike
images = 'images'

# Direktorij gdje se nalaze 
labels = 'labels'

# Stvaranje direktorija images i labels
start_path_images = os.path.join(start_path, images)
start_path_labels = os.path.join(start_path, labels)

destination_path_images = os.path.join(destination_path, images)
destination_path_labels = os.path.join(destination_path, labels)

if not os.path.exists(destination_path_images):
    try:
        os.makedirs(destination_path_images)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    print('Direktorij images je stvoren, put: ' + destination_path_images)

if not os.path.exists(destination_path_labels):
    try:
        os.makedirs(destination_path_labels)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    print('Direktorij labels je stvoren, put: ' + destination_path_labels)


# Uzorkovanje
list_of_images = listdir(start_path_images)
random_list_of_images = random.sample(list_of_images, int(p * len(list_of_images)))

list_of_labels = []
for image in random_list_of_images:
    label = os.path.join(start_path_labels, image[:-4] + '.txt')
    if os.path.exists(label):
        list_of_labels.append(label[:])

# Prebacivanje slika i datoteka
for image in random_list_of_images:
    shutil.copyfile(os.path.join(start_path_images, image), os.path.join(destination_path_images, image))

for label in list_of_labels:
    shutil.copyfile(label, os.path.join(destination_path_labels, str(label)[str(label).rfind('\\')+1:]))