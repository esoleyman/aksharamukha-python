# -*- coding: utf-8 -*-

# Script Mapping for Devanagari

VowelMap =  [
                '\U00011712',
                '\U00011712\U00011721',
                '\U00011712\U00011722',
                '\U00011712\U00011723',
                '\U00011712\U00011724',
                '\U00011712\U00011725',
                '\U0001170D\U00011724\u02BD',
                '\U0001170D\U00011725\u02BD',
                '\U0001170E\U00011724\u02BD',
                '\U0001170E\U00011725\u02BD',
                '\U00011712\U00011726\U00011727',
                '\U00011712\U00011729',
                '\U00011712\U00011726\U00011721',
                '\U00011712\U00011727\U00011728',
            ]

SouthVowelMap = [
                '\U00011712\U00011726\U00011727\u02BD',
                '\U00011712\U00011726\U00011721\u02BD',
                ]

ModernVowelMap = [
                '\U00011712\U00011720',
                '\U00011712\U00011721\u02BD'
                 ]

SinhalaVowelMap = [
                '\U00011712\U00011726\u02BD'
                  ]

VowelSignMap =  [
                '\U00011721',
                '\U00011722',
                '\U00011723',
                '\U00011724',
                '\U00011725',
                '\U0001171E\U00011724\u02BD',
                '\U0001171E\U00011725\u02BD',
                '\U0001171D\U00011724\u02BD',
                '\U0001171D\U00011725\u02BD',
                '\U00011726\U00011727',
                '\U00011729',
                '\U00011726\U00011721',
                '\U00011727\U00011728',
                ]

SouthVowelSignMap = [
                    '\U00011726\U00011727\u02BD',
                    '\U00011726\U00011721\u02BD',
                    ]

ModernVowelSignMap =[
                    '\U00011720',
                    '\U00011721\u02BD'
                    ]

SinhalaVowelSignMap = [
                      '\U00011726\u02BD'
                      ]

AyogavahaMap = [
               '\U0001172A\u02BD',
               '\U0001172A',
               '\U00011711\U0001172B\u02BD'
               ]

ViramaMap =  [
             '\U0001172B'
             ]

ConsonantMap =  [
                '\U00011700',
                '\U00011701',
                '\U00011715',
                '\U00011717',
                '\U00011702',

                '\U0001170B\u02BD',
                '\U0001170B',
                '\U0001170A',
                '\U00011719',
                '\U00011710',

                '\U00011704\u02BD',
                '\U0001170C\u02BD',
                '\U00011713\u02BD',
                '\U00011714\u02BD',
                '\U00011703\u02BD',

                '\U00011704',
                '\U0001170C',
                '\U00011713',
                '\U00011714',
                '\U00011703',

                '\U00011706',
                '\U00011707',
                '\U00011708',
                '\U00011718',
                '\U00011709',

                '\U0001170A\u02BD',
                '\U0001170D',
                '\U0001170E',
                '\U00011708\u02BD',

                '\U0001170F\u02BD',
                '\U0001170F\u02BD',
                '\U0001170F',
                '\U00011711'
                ]

SouthConsonantMap = [
                    '\U0001170E\u02BD',
                    '\U0001170E\u02BD',
                    '\U0001170D\u02BD',
                    '\U00011703\u02BD'
                    ]

NuktaConsonantMap =  [
                     '\U00011700\u02BD',
                     '\U00011701\u02BD',
                     '\U00011715\u02BD',
                     '\U0001170A\u02BD',
                     '\U00011713\u02BD',
                     '\U00011714\u02BD',
                     '\U00011707\u02BD',
                     '\U0001170A\u02BD'
                     ]

SinhalaConsonantMap =[
                     '\U0001172A\U00011715\u02BD',
                     '\U0001172A\U0001170A\u02BD',
                     '\U0001172A\U00011713\u02BD',
                     '\U0001172A\U00011713\u02BD',
                     '\U0001172A\U00011708\u02BD',
                      ]

NuktaMap = [
           '\u02BD\u02BD\u02BD\u02BD'
           ]

OmMap = [
        '\U00011712\U0001172A\U00011728'
        ]

SignMap =[
         '\'',
         '\U0001173C',
         '\U0001173D'
         ]

Aytham =[AyogavahaMap[2]+'\u02BD']

NumeralMap = [
             '\U00011730',
             '\U00011731',
             '\U00011732',
             '\U00011733',
             '\U00011734',
             '\U00011735',
             '\U00011736',
             '\U00011737',
             '\U00011738',
             '\U00011739',
             ]

from ... import GeneralMap as GM

GM.add_additional_chars(dict([(charlist, globals()[charlist]) for charlist in GM.CharmapLists]),
                        __file__.split('.')[0].split('\\')[-1])
