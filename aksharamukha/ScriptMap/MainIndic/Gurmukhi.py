# -*- coding: utf-8 -*-

# Script Mapping for Devanagari

VowelMap =  [
            '\u0A05',
            '\u0A06',
            '\u0A07',
            '\u0A08',
            '\u0A09',
            '\u0A0A',
            '\u0A30\u0A41\u02BC',
            '\u0A30\u0A42\u02BC',
            '\u0A32\u0A41\u02BC',
            '\u0A32\u0A42\u02BC',
            '\u0A0F',
            '\u0A10',
            '\u0A13',
            '\u0A14',
            ]

SouthVowelMap = [
                '\u0A0F\u02D8',
                '\u0A13\u02D8',
                ]

ModernVowelMap = [
                 '\u0A0F\u02BC',
                 '\u0A06\u02BC',
                 ]

SinhalaVowelMap = [
                  '\u0A0F\u02C7'
                  ]

VowelSignMap =  [
                '\u0A3E',
                '\u0A3F',
                '\u0A40',
                '\u0A41',
                '\u0A42',
                '\u0A4D\u0A30\u0A41\u02BC',
                '\u0A4D\u0A30\u0A42\u02BC',
                '\u0A4D\u0A32\u0A41\u02BC',
                '\u0A4D\u0A32\u0A42\u02BC',
                '\u0A47',
                '\u0A48',
                '\u0A4B',
                '\u0A4C',
                ]

SouthVowelSignMap = [
                    '\u0A47\u02D8',
                    '\u0A4B\u02D8',
                    ]

ModernVowelSignMap =[
                    '\u0A47\u02BC',
                    '\u0A3E\u02BC']

SinhalaVowelSignMap = [
                      '\u0A47\u02C7'
                      ]

AyogavahaMap = [
               '\u0A01',
               '\u0A02',
               '\u0A03'
               ]

ViramaMap =  [
             '\u0A4D'
             ]

ConsonantMap =  [
                '\u0A15',
                '\u0A16',
                '\u0A17',
                '\u0A18',
                '\u0A19',

                '\u0A1A',
                '\u0A1B',
                '\u0A1C',
                '\u0A1D',
                '\u0A1E',

                '\u0A1F',
                '\u0A20',
                '\u0A21',
                '\u0A22',
                '\u0A23',

                '\u0A24',
                '\u0A25',
                '\u0A26',
                '\u0A27',
                '\u0A28',

                '\u0A2A',
                '\u0A2B',
                '\u0A2C',
                '\u0A2D',
                '\u0A2E',

                '\u0A2F',
                '\u0A30',
                '\u0A32',
                '\u0A35',

                '\u0A36',
                '\u0A36\u0A3C',
                '\u0A38',
                '\u0A39'
                ]

SouthConsonantMap = [
                    '\u0A33',
                    '\u0A33\u0A3C',
                    '\u0A30\u0A3C',
                    '\u0A28\u0A3C'
                    ]

NuktaConsonantMap =  [
                     '\u0A15\u0A3C',
                     '\u0A59',
                     '\u0A5A',
                     '\u0A5B',
                     '\u0A5C',
                     '\u0A22\u0A3C',
                     '\u0A5E',
                     '\u0A2F\u0A3C'
                     ]

SinhalaConsonantMap =[
                     '\u0A01\u02C6\u0A17',
                     '\u0A01\u02C6\u0A1C',
                     '\u0A01\u02C6\u0A21',
                     '\u0A01\u02C6\u0A26',
                     '\u0A01\u02C6\u0A2C',
                      ]

NuktaMap = [
           '\u0A3C'
           ]

OmMap = [
        '\u0A74'
        ]

SignMap =[
         '\u0028\u0A05\u0029',
         '\u0964',
         '\u0965'
         ]

Aytham =[AyogavahaMap[2]+'\u02BC']


NumeralMap = [
             '\u0A66',
             '\u0A67',
             '\u0A68',
             '\u0A69',
             '\u0A6A',
             '\u0A6B',
             '\u0A6C',
             '\u0A6D',
             '\u0A6E',
             '\u0A6F'
             ]

from ... import GeneralMap as GM

GM.add_additional_chars(dict([(charlist, globals()[charlist]) for charlist in GM.CharmapLists]),
                        __file__.split('.')[0].split('\\')[-1])
