#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may not
#  use this file except in compliance with the License. You may obtain a copy of
#  the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations under
#  the License.
#
#  KanjiData.py
#  Japanese Quiz Data
#
#  Created by Chris Davis on 17/06/2011.
#  Copyright (c) 2012 GameWeaver LTD. All rights reserved.
#

from collections import namedtuple

DataItem = namedtuple('DataItem', ['kanji', 'meaning', 'kunyomi', 'onyomi'], verbose=False)

kanjis = [
	DataItem(u"日",  u"Sun, Day",  u"ひ",  u"ニチ"),
	DataItem(u"月",  u"Moon, Month",  u"つき",  u"ゲツ"),
	DataItem(u"木",  u"Tree",  u"き",  u"モク"),
	DataItem(u"山",  u"Mountain",  u"やま",  u"サン"),
	DataItem(u"川",  u"River",  u"かわ",  u"セン"),
	DataItem(u"田",  u"Rice Field",  u"た",  u"デン"),
	DataItem(u"人",  u"Person, People",  u"ひと",  u"ジン"),
	DataItem(u"口",  u"Mouth, Entrance",  u"くち",  u"コー"),
	DataItem(u"車",  u"Car",  u"くるま",  u"シャ"),
	DataItem(u"門",  u"Gate",  u"かど",  u"モン"),
	DataItem(u"火",  u"Fire",  u"ひ",  u"カ"),
	DataItem(u"水",  u"Water",  u"みず",  u"スイ"),
	DataItem(u"金",  u"Metal, Money",  u"かなえ",  u"キン"),
	DataItem(u"土",  u"Earth, Ground",  u"つち",  u"ドー"),
	DataItem(u"子",  u"Child",  u"こ",  u"シ"),
	DataItem(u"女",  u"Woman",  u"おんな",  u"ジョ"),
	DataItem(u"学",  u"School, Study",  u"まなぶ",  u"ガク"),
	DataItem(u"生",  u"Life, Born",  u"いきる",  u"セン"),
	DataItem(u"先",  u"Previous",  u"さき",  u"セイ"),
	DataItem(u"私",  u"Me (I), Private",  u"わたし",  u"シ"),
	DataItem(u"一",  u"One",  u"ひとつ",  u"イチ"),
	DataItem(u"二",  u"Two",  u"ふたつ",  u"ニ"),
	DataItem(u"三",  u"Three",  u"みつ",  u"サン"),
	DataItem(u"四",  u"Four",  u"よっつ",  u"シ"),
	DataItem(u"五",  u"Five",  u"いっつ",  u"ゴ"),
	DataItem(u"六",  u"Six",  u"むっつ",  u"ロク"),
	DataItem(u"七",  u"Seven",  u"ななつ",  u"シチ"),
	DataItem(u"八",  u"Eight",  u"やっつ",  u"ハチ"),
	DataItem(u"九",  u"Nine",  u"ここのつ",  u"キュウ"),
	DataItem(u"十",  u"Ten",  u"とお",  u"ジュウ"),
	DataItem(u"百",  u"Hundred",  u"ひゃく",  u"ヒャク"),
	DataItem(u"千",  u"Thousand",  u"せん",  u"セン"),
	DataItem(u"万",  u"Ten Thousand",  u"まん",  u"マン"),
	DataItem(u"円",  u"Yen",  u"えん",  u"エン"),
	DataItem(u"年",  u"Year",  u"とし",  u"ネン"),
	DataItem(u"上",  u"Above",  u"うえ",  u"ジョー"),
	DataItem(u"下",  u"Under",  u"した",  u"ゲ"),
	DataItem(u"中",  u"Inside, Middle",  u"なか",  u"チュー"),
	DataItem(u"大",  u"Big",  u"おお（きい",  u"ダイ"),
	DataItem(u"小",  u"Small",  u"ち(さい)",  u"ショー"),
	DataItem(u"本",  u"Book, Root",  u"もと",  u"ホン"),
	DataItem(u"半",  u"Half",  u"んかば",  u"ハン"),
	DataItem(u"分",  u"Divide",  u"わける",  u"フン、ブン"),
	DataItem(u"力",  u"Power",  u"ちから",  u"リョク"),
	DataItem(u"何",  u"What",  u"なに",  u"カ"),
	DataItem(u"明",  u"Bright",  u"あかるい",  u"ミョウ"),
	DataItem(u"休",  u"Rest",  u"やすみ",  u"キュウ"),
	DataItem(u"体",  u"Body",  u"からだ",  u"タイ"),
	DataItem(u"好",  u"Like/Love",  u"すき",  u"コウ"),
	DataItem(u"男",  u"Man",  u"おとこ",  u"ダン"),
	DataItem(u"林",  u"Wood",  u"はやし",  u"リン"),
	DataItem(u"森",  u"Forest",  u"もり",  u"シン"),
	DataItem(u"間",  u"Duration",  u"あいだ",  u"カン"),
	DataItem(u"畑",  u"Cultivated Land",  u"はたけ",  u"―"),
	DataItem(u"岩",  u"Boulder",  u"いわ",  u"ガン"),
	DataItem(u"目",  u"Eye",  u"め",  u"ボケ"),
	DataItem(u"耳",  u"Ear",  u"みみ",  u"ジ"),
	DataItem(u"手",  u"Hand",  u"て",  u"シュ"),
	DataItem(u"足",  u"Legs/Pair",  u"あし",  u"ソク"),
	DataItem(u"雨",  u"Rain",  u"あめ",  u"ウ"),
	DataItem(u"竹",  u"Bamboo",  u"たけ",  u"チク"),
	DataItem(u"米",  u"Rice/America",  u"こめ",  u"ベイ"),
	DataItem(u"貝",  u"Shellfish",  u"かい",  u"バイ"),
	DataItem(u"石",  u"Rock",  u"いし",  u"セキ"),
	DataItem(u"糸",  u"Thread",  u"いと",  u"シ"),
	DataItem(u"花",  u"Flower",  u"はな",  u"カ, ケ"),
	DataItem(u"茶",  u"Tea",  u"ちゃ",  u"[TODO]"),
	DataItem(u"肉",  u"Meat",  u"にく",  u"[TODO]"),
	DataItem(u"文",  u"Sentences",  u"ぶん",  u"[TODO]"),
	DataItem(u"字",  u"Letter",  u"じ",  u"[TODO]"),
	DataItem(u"物",  u"Thing",  u"もの",  u"[TODO]"),
	DataItem(u"牛",  u"Cow",  u"ぎゅ",  u"[TODO]"),
	DataItem(u"馬",  u"Horse",  u"うま",  u"[TODO]"),
	DataItem(u"鳥",  u"Bird",  u"とり",  u"[TODO]"),
	DataItem(u"魚",  u"Fish",  u"さかな",  u"[TODO]"),
	DataItem(u"新",  u"New",  u"あたらし",  u"[TODO]"),
	DataItem(u"古",  u"Old",  u"ふるい",  u"[TODO]"),
	DataItem(u"長",  u"Long",  u"ながい",  u"[TODO]"),
	DataItem(u"短",  u"Short",  u"みじかい",  u"[TODO]"),
	DataItem(u"高",  u"Expensive/Tall",  u"たかい",  u"[TODO]"),
	DataItem(u"安",  u"Cheap/Safe",  u"やすい",  u"[TODO]"),
	DataItem(u"低",  u"Low",  u"ひくい",  u"[TODO]"),
	DataItem(u"暗",  u"Dark/Dim",  u"くらい",  u"[TODO]"),
	DataItem(u"多",  u"Many",  u"おおい",  u"[TODO]"),
	DataItem(u"少",  u"Few",  u"すこし",  u"[TODO]"),
	DataItem(u"行",  u"To Go",  u"いきます",  u"コウ"),
	DataItem(u"来",  u"To Come",  u"きます",  u"ライ"),
	DataItem(u"帰",  u"To Return",  u"かえります",  u"キ"),
	DataItem(u"食",  u"Eat",  u"たべます",  u"ショク"),
	DataItem(u"飲",  u"Drink",  u"のみます",  u"イン"),
	DataItem(u"見",  u"See/Look",  u"みます",  u"ケン"),
	DataItem(u"聞",  u"Hear/Listen",  u"ききます",  u"ブン"),
	DataItem(u"読",  u"Read",  u"よみます",  u"ドク"),
	DataItem(u"書",  u"Write",  u"かきます",  u"ショ"),
	DataItem(u"話",  u"Talk",  u"はなし",  u"ワ"),
	DataItem(u"買",  u"Buy",  u"かいます",  u"バイ"),
	DataItem(u"教",  u"Educate/Teach",  u"おしえます",  u"オンヨミ"),
	DataItem(u"朝",  u"Morning",  u"あさ",  u"チョウ"),
	DataItem(u"昼",  u"Noon",  u"ひる",  u"チュウ"),
	DataItem(u"夜",  u"Night",  u"よる",  u"ヤ"),
	DataItem(u"晩",  u"Night-",  u"-",  u"バン"),
	DataItem(u"夕",  u"Evening",  u"ゆう",  u"セキ"),
	DataItem(u"方",  u"Direction",  u"かた",  u"ホウ")
]