

def custom_slugify(value):
    az_list = [
        'Ç', 'Ə', 'Ğ', 'I', 'Ö', 'Ş', 'Ü','ç', 'ə', 'ğ', 'ı', 'ö', 'ş', 'ü', ' '
    ]
    en_list = [
        'C', 'E', 'G', 'I', 'O', 'S', 'U','c', 'e', 'g', 'i', 'o', 's', 'u', '-'
    ]
    for az, en in zip(az_list, en_list):
        value = value.replace(az, en)
    return value