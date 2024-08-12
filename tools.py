# Part 1: Functions to read trajectory data and preprocessed trajectory data into dictionaries, includes:
# read_trajectory_txt
# read_filtering_trajectory_txt

# Part 2: Functions to determine whether the vehicle bounding box intersects with the upper or lower ends of a predefined crosswalk, includes:
# on_segment
# orientation
# do_intersect
# is_intersection

# Part 3: Functions to determine whether the pedestrian bounding box intersects with the predefined crosswalk area, includes:
# is_in_poly

# Part 4: Functions to read label data and detection data, and perform matching, includes:
# read_label_txt
# calculate_tiou
# calculate_siou

# Part 5: Functions to crop image features and save them
# crop_images
# crop_att_images


from PIL import Image, ImageDraw
import math
import os
import numpy as np

image_size=(1200, 1100)


# --------Part 1--------

def read_trajectory_txt(file_path):
    data_dict = {}
    frame_id = None

    with open(file_path, 'r') as file:
        lines = file.readlines()

    i = 0
    while i < len(lines):
        frame_id = int(lines[i].strip())
        i += 1

        num_boxes = int(lines[i].strip())
        i += 1

        frame_data = []

        for j in range(num_boxes):
            box_data = list(map(float, lines[i].strip().split()))
            frame_data.append({
                'id': int(box_data[0]),
                'label': int(box_data[1]),
                'left': box_data[2],
                'top': box_data[3],
                'right': box_data[4],
                'bottom': box_data[5]
            })
            i += 1

        data_dict[frame_id] = frame_data

    return data_dict

def read_filtering_trajectory_txt(file_path):
    data_dict = {}
    frame_id = None

    with open(file_path, 'r') as file:
        lines = file.readlines()

    i = 0
    while i < len(lines):
        frame_id = int(lines[i].strip())
        i += 1

        num_boxes = int(lines[i].strip())
        i += 1

        frame_data = []

        for j in range(num_boxes):
            box_data = list(map(float, lines[i].strip().split()))
            frame_data.append({
                'id': int(box_data[0]),
                'left': box_data[1],
                'top': box_data[2],
                'right': box_data[3],
                'bottom': box_data[4]
            })
            i += 1

        data_dict[frame_id] = frame_data

    return data_dict


# --------Part 2--------
        
def on_segment(p, q, r):
    return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))


def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2


def do_intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and on_segment(p1, p2, q1):
        return True
    if o2 == 0 and on_segment(p1, q2, q1):
        return True
    if o3 == 0 and on_segment(p2, p1, q2):
        return True
    if o4 == 0 and on_segment(p2, q1, q2):
        return True

    return False


def is_intersection(line_segment, rect_top_left, rect_bottom_right):
    p1, p2 = line_segment
    rect_top_right = (rect_bottom_right[0], rect_top_left[1])
    rect_bottom_left = (rect_top_left[0], rect_bottom_right[1])

    if (on_segment(rect_top_left, p1, rect_bottom_right) or
            on_segment(rect_top_left, p2, rect_bottom_right)):
        return True

    if do_intersect(p1, p2, rect_top_left, rect_top_right) or \
            do_intersect(p1, p2, rect_top_right, rect_bottom_right) or \
            do_intersect(p1, p2, rect_bottom_right, rect_bottom_left) or \
            do_intersect(p1, p2, rect_bottom_left, rect_top_left):
        return True

    return False


# --------Part 3--------
    
def is_in_poly(p, poly):
    """
    :param p: [x, y]
    :param poly: [[], [], [], [], ...]
    :return:
    """
    px, py = p
    is_in = False
    for i, corner in enumerate(poly):
        next_i = i + 1 if i + 1 < len(poly) else 0
        x1, y1 = corner
        x2, y2 = poly[next_i]
        if (x1 == px and y1 == py) or (x2 == px and y2 == py):  # if point is on vertex
            is_in = True
            break
        if y1 == 0 and y2 == 0:
            if min(x1, x2) < px < max(x1, x2):
                is_in = True
                break
        if min(y1, y2) < py <= max(y1, y2):  # find horizontal edges of polygon
            x = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
            if x == px:  # if point is on edge
                is_in = True
                break
            elif x > px:  # if point is on left-side of line
                is_in = not is_in
    return is_in
 

# --------Part 4--------

def read_label_txt(file_path):
    data_dict = {}

    with open(file_path, 'r') as file:
        lines = file.readlines()

    i = 0
    while i < len(lines):
        # Read the bounding box id
        box_id = int(lines[i].strip())
        i += 1

        # Read the number of occurrences of this bounding box id
        num_occurrences = int(lines[i].strip())
        i += 1

        # Initialize the list for the current bounding box id
        box_data_list = []

        # Read the bounding box data
        for j in range(num_occurrences):
            box_data = list(map(float, lines[i].strip().split()))
            box_data_list.append({
                'occurrence': int(box_data[0]),
                'frame': int(box_data[1]),
                'cls': int(box_data[2]),
                'left': box_data[3],
                'top': box_data[4],
                'right': box_data[5],
                'bottom': box_data[6]
            })
            i += 1

        # Add the bounding box id data to the dictionary
        data_dict[box_id] = box_data_list

    return data_dict    

# Spatio-temporal matching  
# Function to calculate temporal Intersection over Union (tIoU)
def calculate_tiou(det_start, det_end, label_start, label_end):
    # Calculate intersection
    intersect_start = max(det_start, label_start)
    intersect_end = min(det_end, label_end)
    intersection = max(0, intersect_end - intersect_start)
    # Calculate union
    union = (det_end - det_start) + (label_end - label_start) - intersection
    return intersection / union if union > 0 else 0

# Function to calculate spatial Intersection over Union (sIoU)
def calculate_siou(det_box, label_box):
    # Calculate intersection
    x_left = max(det_box['left'], label_box['left'])
    y_top = max(det_box['top'], label_box['top'])
    x_right = min(det_box['right'], label_box['right'])
    y_bottom = min(det_box['bottom'], label_box['bottom'])
    intersect_area = max(0, x_right - x_left) * max(0, y_bottom - y_top)
    # Calculate union
    det_area = (det_box['right'] - det_box['left']) * (det_box['bottom'] - det_box['top'])
    label_area = (label_box['right'] - label_box['left']) * (label_box['bottom'] - label_box['top'])
    union_area = det_area + label_area - intersect_area
    return intersect_area / union_area if union_area > 0 else 0


# --------Part 5--------

def crop_images(source_folder, target_folder, crop_rectangle, start_frame, end_frame, frame=32):
    # Create the target folder if it does not exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    # Get all image filenames and filter out .jpg files
    image_files = sorted([f for f in os.listdir(source_folder) if f.lower().endswith('.jpg')])
    
    # Calculate the frame sampling interval
    total_frames = end_frame - start_frame + 1
    step = math.floor(total_frames / frame)
    
    # Downsample frame numbers
    sampled_frames = [start_frame + i * step for i in range(frame) if start_frame + i * step <= end_frame]
    
    # Crop the corresponding jpg files in the folder using the downsampled frame numbers
    for i, frame_number in enumerate(sampled_frames):
        file_name = image_files[frame_number-1]  # The file list starts from 0, but the frame numbers start from 1
        file_path = os.path.join(source_folder, file_name)

        with Image.open(file_path) as img:
            # Crop the image
            cropped_img = img.crop(crop_rectangle)
            # Construct the output file path, output files are named sequentially from 1 to frame
            output_file_name = f"{i+1:03d}.jpg"  # Generate formatted filenames like 001.jpg, 032.jpg
            output_file_path = os.path.join(target_folder, output_file_name)
            # Save the cropped image
            cropped_img.save(output_file_path)

def crop_att_images(source_folder, target_folder, vehicle_id, data_dict, crop_rectangle, start_frame, end_frame, frame=32):
    # Create the target folder if it does not exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    # Get all image filenames and filter out .jpg files
    image_files = sorted([f for f in os.listdir(source_folder) if f.lower().endswith('.jpg')])
    
    # Calculate the frame sampling interval
    total_frames = end_frame - start_frame + 1
    step = math.floor(total_frames / frame)
    
    # Downsample frame numbers
    sampled_frames = [start_frame + i * step for i in range(frame) if start_frame + i * step <= end_frame]
    
    # Crop the corresponding jpg files in the folder using the downsampled frame numbers
    for i, frame_number in enumerate(sampled_frames):
        file_name = image_files[frame_number-1]  # The file list starts from 0, but the frame numbers start from 1
        file_path = os.path.join(source_folder, file_name)

        vehicle_image = Image.new('L', image_size, 0)
        draw = ImageDraw.Draw(vehicle_image)    
        
        # Crop the image
        # Ensure frame_id is in data_dict
        if (frame_number+1) in data_dict:
            # Iterate through all bounding boxes in the frame
            for box in data_dict[frame_number + 1]:
                # Find the bounding box with the matching vehicle id
                if box['id'] == vehicle_id:
                    # Get and print the details
                    left = box['left']
                    top = box['top']
                    right = box['right']
                    bottom = box['bottom']
                    break
                else:
                    left, top, right, bottom = 0, 0, 0, 0                   
        
        draw.rectangle([left, top, right, bottom], fill=255)  
        
        pedestrian_image = Image.open(file_path)
        # .convert('L')
        
        vehicle_array = np.array(vehicle_image)
        pedestrian_array = np.array(pedestrian_image)

        # Increase brightness
        result_array = np.clip(vehicle_array + pedestrian_array, 0, 255).astype(np.uint8)

        # Convert the result array back to a PIL image
        result_image = Image.fromarray(result_array)
        result_image = result_image.crop(crop_rectangle)           
        # Construct the output file path, output files are named sequentially from 1 to frame
        output_file_name = f"{i+1:03d}.jpg"  # Generate formatted filenames like 001.jpg, 032.jpg
        output_file_path = os.path.join(target_folder, output_file_name)
        
        # Save or display the result image
        result_image.save(output_file_path)

        