import glob
import pandas as pd

## parameteres
data_dir = 'E:/Data/kfood'
##

def create_metadata(data_dir):
    file_list = glob.glob(data_dir+'/*/*/*/*')
    df_meta = pd.DataFrame({'filepath':file_list})
    le_list = glob.glob(data_dir+'/*/*/*/*')
    df_meta = pd.DataFrame({'filepath':file_list})
    df_meta['class1'] = df_meta.filepath.str.extract(r'E:/Data/kfood\\([^\\]+)')
    df_meta['class2'] = df_meta.filepath.str.extract(r'E:/Data/kfood\\[^\\]+\\([^\\]+)')
    df_meta['class3'] = df_meta.filepath.str.extract(r'E:/Data/kfood\\[^\\]+\\[^\\]+\\([^\\]+)')
    df_meta['filetype'] = df_meta.filepath.str.extract(r'\.([^\.]+$)')
    df_meta = df_meta.loc[:,['filetype','class1','class2','class3','filepath']]
    df_meta.to_csv('jgryu/data/meta.csv', index=False)


def main():
    create_metadata(data_dir)


if __name__ == "__main__":
    main()