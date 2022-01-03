import json

file = open("./dhd_campus/dhd_pedestrian_campus_train.json")

train_labels = json.load(file)


image_info = train_labels["images"]
labels_data = train_labels["annotations"]

for i in range(0, len(image_info)):
    image = image_info[i]
    width = image["width"]
    height = image["height"]
    id = image["id"]
    filename = image["file_name"]
    labels = []
    filename_without_ext = filename.split(".")[0]
    with open("./dhd_campus/train/labels/" + filename_without_ext + ".txt", "x") as label_file:
        for annotation in labels_data:
            if annotation["image_id"] == id:
                bbox = annotation["bbox"]
                ann_width = bbox[2] / width
                ann_height = bbox[3] / height
                x = bbox[0] / width + ann_width / 2
                y = bbox[1] / height + ann_height / 2
                
                line = "0 " + str(x) + " " + str(y) + " " + str(ann_width) + " " + str(ann_height) + "\n"
                label_file.write(line)
    print("Created file:" + filename_without_ext + ".txt " + str(i + 1) + "/" + str(len(image_info)))

file = open("dhd_campus/dhd_pedestrian_campus_val.json")

train_labels = json.load(file)


image_info = train_labels["images"]
labels_data = train_labels["annotations"]

for i in range(0, len(image_info)):
    image = image_info[i]
    width = image["width"]
    height = image["height"]
    id = image["id"]
    filename = image["file_name"]
    labels = []
    filename_without_ext = filename.split(".")[0]
    with open("./dhd_campus/val/labels/" + filename_without_ext + ".txt", "x") as label_file:
        for annotation in labels_data:
            if annotation["image_id"] == id:
                bbox = annotation["bbox"]
                ann_width = bbox[2] / width
                ann_height = bbox[3] / height
                x = bbox[0] / width + ann_width / 2
                y = bbox[1] / height + ann_height / 2
                line = "0 " + str(x) + " " + str(y) + " " + str(ann_width) + " " + str(ann_height) + "\n"
                label_file.write(line)
    print("Created file:" + filename_without_ext + ".txt " + str(i + 1) + "/" + str(len(image_info)))
