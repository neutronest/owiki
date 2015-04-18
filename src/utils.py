#-*- coding:utf-8 -*-
import sys, os
import wiki_config

def folder_travel(folder_path):
    """ travel the folder and get all the dirs and filenames

    Parameters:
    -----------
    folder_path: a folder location
                 type: str

    Return:
    -------
    category_dict: the dict that return all the information.
                   type: dict {"cur_folder": (dirs, files)}
                   format: math ([type-theory,..], [hott.md, ..])

    """
    category_dict = {}

    for (cur, dirs, files) in os.walk(folder_path):
        if cur == wiki_config.wiki_root:
            continue

        # filter, and parse the file_name
        files = [file_item for file_item in files if file_item != ".DS_Store"]

        files = map(lambda x:x.replace(".md", ""), files)
        category_dict[cur.replace(wiki_config.wiki_root, "")] = (dirs, files)
    return category_dict

if __name__ == "__main__":
    file_dict = folder_travel(wiki_config.wiki_root)
    for (k, v) in file_dict.items():
        print k, v
