import unittest
import nlu
import pandas as pd
import numpy as np

class TestComponentInfo(unittest.TestCase):
    def test_bad_r(self):
        r1 = 'en.ner.onto.sm'
        r2 = 'en.ner.dl.bert'
        df = nlu.load(r1).predict('Hello world')

        print(df)
        print(df.columns)

        nlu.load(r2).predict('Hello world')
        print(df)
        print(df.columns)
    #
    # def test_component_stack(self):
    #     # pos
    #
    #     pipe = nlu.load('sentiment bert', verbose = True ) #  bert
    #     preds = pipe.predict('Helo world!')
    #
    #     # sentim ent + bert bad
    #     # bert + sentim OK!>!>?!?!?
    #     # pos + sentiment OK!?
    #     #  sentiment+ pos NOT OK!!?!?!?!?
    #     # pos bert sent OK but whenevers ent not last we have troublz
    #     # pipe = nlu.load('sentiment emotion') #  bert
    #     # preds = pipe.predict('Helo world!')
    #     #
    #     # pipe = nlu.load('pos emotion') #  bert
    #     # preds = pipe.predict('Helo world!')
    #     #
    #     # pipe = nlu.load('emotion pos sentiment') #  bert
    #     # preds = pipe.predict('Helo world!')
    #     #
    #     # pipe = nlu.load('emotion pos sentiment bert') #  bert
    #     # preds = pipe.predict('Helo world!')
    #
    #     print(preds.columns)
    #     print(preds)
    #
