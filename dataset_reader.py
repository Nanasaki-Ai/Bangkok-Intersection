# -*- coding: utf-8 -*-
import os
import torch
import pickle
import cv2
import numpy as np
from PIL import Image
from torchvision import transforms
from torch.utils.data import Dataset


class DataSetReader(Dataset):
    def __init__(self, args, mode='train'):
        self.exp_dir = args.exp_dir
        if mode == 'train':
            self.label_path = os.path.join(args.label_path, args.benchmark, 'train_labels.pkl')
        else:
            self.label_path = os.path.join(args.label_path, args.benchmark, 'test_labels.pkl')
            
        self.feature_path = args.feature_path
        self.modality = args.modality
        if self.modality == 'rgb':
            self.data_path = os.path.join(self.feature_path, 'rgb_volumes_region')   #  stage 2
            # self.data_path = os.path.join(self.feature_path, 'rgb_features')       #  stage 1
        else:
            self.data_path = os.path.join(self.feature_path, 'tra_att_volumes_region')   #  stage 5
            # self.data_path = os.path.join(self.feature_path, 'tra_volumes_region')     #  stage 4
            # self.data_path = os.path.join(self.feature_path, 'tra_features')           #  stage 3
            
        self.number = args.frame_number
        if self.number == 32:
            self.interval = 1
        elif self.number == 16:
            self.interval = 2
        elif self.number == 8:
            self.interval = 4
        elif self.number == 4:
            self.interval = 8
            
        self.load_data()


    def load_data(self):
        # label
        with open(self.label_path, 'rb') as f:
            self.sample_name, self.label = pickle.load(f)
        strr = 'Load {} samples from {}'.format(len(self.label), self.label_path)
        print(strr)
        with open('{}/log.txt'.format(self.exp_dir), 'a') as f:
            print(strr, file=f)


    def __len__(self):
        return len(self.label)


    def __getitem__(self, index):
        label = self.label[index]
        # label = torch.from_numpy(np.fromstring(label, dtype=int, sep=' '))
        
        sample_number = self.sample_name[index]
        folder = os.path.join(self.data_path, sample_number)
        images = []
        interval = self.interval
        
        for i, filename in enumerate(sorted(os.listdir(folder))):
            if i % interval == 0: 
                if self.modality == 'tra':
                    img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
                else:
                    img = cv2.imread(os.path.join(folder, filename))
                img = cv2.resize(img, (256, 256))
                images.append(img)
        if self.modality == 'rgb':
            feature_input = np.stack(images, axis=3)
            feature_input = torch.from_numpy(feature_input).float()
            feature_input = feature_input.permute(2, 3, 0, 1).contiguous()            
        else:
            feature_input = np.stack(images, axis=2)  
            feature_input = torch.from_numpy(feature_input).float()
            feature_input = feature_input.permute(2, 0, 1).contiguous()
            feature_input = feature_input.unsqueeze(0)
        
        return feature_input, label