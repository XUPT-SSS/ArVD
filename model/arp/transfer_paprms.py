def huggingface_csv_file():
    file_name='d2a'
    data_files=choose_file(file_name)
    return data_files

def chooice_few_shot_number():
    number = None
    number = 10
    #number = 50
    #number = 100
    #number = 500
    #number = 1000
    return number


def choose_model():
    # model= 'TextCNN'
    model= 'init_model'
    return model

def choose_loss():
    #loss = 'focal_loss'
    loss = 'CrossEntropyLoss'
    return loss


def choose_file(datasets):
    if datasets =='d2a':
        data_files = {
            'train': '/home/yons/person/zc/ArVD/model/xsbt_process/data/train_xsbt.csv',
            'validation': '/home/yons/person/zc/ArVD/model/xsbt_process/data/val_xsbt.csv',
            'test': '/home/yons/person/zc/ArVD/model/xsbt_process/data/test_xsbt.csv',
        }
        return data_files



