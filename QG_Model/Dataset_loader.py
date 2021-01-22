class Dataset_loader(Dataset):
    def __init__(self, file_path):
        self.file_path = file_path
        with open(self.file_path, 'r') as file:
            self.data = json.loads(file.read())['data']
            self.total_data_count = len(data)
        self.idx = 0
        
    def __len__(self):
        return self.total_data_count

    def __getitem__(self, _):
        if self.idx != self.total_data_count:
            self.idx += 1
            return self.data[self.idx - 1]
        else:
            self.idx = 0
            return self.data[self.idx]