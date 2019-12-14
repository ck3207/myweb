# -*- coding: utf-8 -*-
from orthogonal_array import OrthogonalArray
from config import Config
__author__ = "chenk"


if __name__ == "__main__":
    config = Config()
    factors, cols, split = config.get_config()
    orthogonal_array = OrthogonalArray(col=cols, factor=factors, split=split)
    orthogonal_array.transfer(orthogonal_array.delete_array(orthogonal_array.read_array()))
    for each in orthogonal_array.get_mapping_arr():
        print(each.replace(orthogonal_array.split, "\t"))
