import sys

#%%
def info_sys():
    str = f'Version: {sys.version} Platform: {sys.platform}'
    print(str)
    return str

def getsizeof(obj):
    print(sys.getsizeof(obj))
# %%
