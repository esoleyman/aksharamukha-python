# -*- coding: utf-8 -*-

# Script Mapping for Devanagari

VowelMap =  [
            '\U00011680',
            '\U00011681',
            '\U00011682',
            '\U00011683',
            '\U00011684',
            '\U00011685',
            '𑚤𑚮\u02BD',
            '𑚤𑚯\u02BD',
            '𑚥𑚮\u02BD',
            '𑚥𑚯\u02BD',
            '\U00011686',
            '\U00011687',
            '\U00011688',
            '\U00011689',
            ]

SouthVowelMap = [
                '\U00011686',
                '\U00011688',
                ]

ModernVowelMap = [
                 '\U00011686\u02BD',
                 '\U00011681\u02BD',
                 ]

SinhalaVowelMap = [
                  '\U00011686\u02BD'
                  ]

VowelSignMap =  [
                '\U000116AD',
                '\U000116AE',
                '\U000116AF',
                '\U000116B0',
                '\U000116B1',
                '𑚶𑚤𑚮\u02BD',
                '𑚶𑚤𑚯\u02BD',
                '𑚶𑚥𑚮\u02BD',
                '𑚶𑚥𑚯\u02BD',
                '\U000116B2',
                '\U000116B3',
                '\U000116B4',
                '\U000116B5',
                ]

SouthVowelSignMap = [
                    '\U000116B3\u02BD',
                    '\U000116B4\u02BD',
                    ]

ModernVowelSignMap =[
                    '\U000116B3\u02BD',
                    '\U000116AD\u02BD'
                    ]

SinhalaVowelSignMap = [
                      '\U000116B3\u02BD'
                      ]

AyogavahaMap = [
               '\U000116AB\u02BD',
               '\U000116AB',
               '\U000116AC'
               ]

ViramaMap =  [
             '\U000116B6'
             ]

ConsonantMap =  [
                '\U0001168A',
                '\U000116B8',
                '\U0001168C',
                '\U0001168D',
                '\U0001168E',

                '\U0001168F',
                '\U00011690',
                '\U00011691',
                '\U00011692',
                '\U00011693',

                '\U00011694',
                '\U00011695',
                '\U00011696',
                '\U00011697',
                '\U00011698',

                '\U00011699',
                '\U0001169A',
                '\U0001169B',
                '\U0001169C',
                '\U0001169D',

                '\U0001169E',
                '\U0001169F',
                '\U000116A0',
                '\U000116A1',
                '\U000116A2',

                '\U000116A3',
                '\U000116A4',
                '\U000116A5',
                '\U000116A6',

                '\U000116A7',
                '\U0001168B',
                '\U000116A8',
                '\U000116A9'
                ]

SouthConsonantMap = [
                    '𑚥𑚷',
                    '𑚥𑚷\u02BD',
                    '𑚤𑚷',
                    '𑚝𑚷'
                    ]

NuktaConsonantMap =  [
                     '𑚊\U000116B7',
                     '𑚋\U000116B7',
                     '𑚌\U000116B7',
                     '𑚑\U000116B7',
                     '𑚪',
                     '𑚗\U000116B7',
                     '𑚟\U000116B7',
                     '𑚣\U000116B7'
                     ]

SinhalaConsonantMap =[
                     '\U000116AB𑚌\u02BD',
                     '\U000116AB𑚑\u02BD',
                     '\U000116AB𑚖\u02BD',
                     '\U000116AB𑚛\u02BD',
                     '\U000116AB𑚠\u02BD',
                      ]

NuktaMap = [
           '\U000116B7'
           ]

OmMap = [
        '𑚈𑚫'
        ]

SignMap =[
         'ऽ',
         '।',
         '॥'
         ]

Aytham =[AyogavahaMap[2]+'\u02BD']

NumeralMap = [
             '\U000116C0',
             '\U000116C1',
             '\U000116C2',
             '\U000116C3',
             '\U000116C4',
             '\U000116C5',
             '\U000116C6',
             '\U000116C7',
             '\U000116C8',
             '\U000116C9'
             ]

from ... import GeneralMap as GM

GM.add_additional_chars(dict([(charlist, globals()[charlist]) for charlist in GM.CharmapLists]),
                        __file__.split('.')[0].split('\\')[-1])
