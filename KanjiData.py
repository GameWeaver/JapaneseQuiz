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

kanjis = [
{"kanji": u"日", "meanings": u"Sun, Day", "kunyomi": u"ひ", "onyomi": u"ニチ"},
{"kanji": u"月", "meanings": u"Moon, Month", "kunyomi": u"つき", "onyomi": u"ゲツ"},
{"kanji": u"木", "meanings": u"Tree", "kunyomi": u"き", "onyomi": u"モク"},
{"kanji": u"山", "meanings": u"Mountain", "kunyomi": u"やま", "onyomi": u"サン"},
{"kanji": u"川", "meanings": u"River", "kunyomi": u"かわ", "onyomi": u"セン"},
{"kanji": u"田", "meanings": u"Rice Field", "kunyomi": u"た", "onyomi": u"デン"},
{"kanji": u"人", "meanings": u"Person, People", "kunyomi": u"ひと", "onyomi": u"ジン"},
{"kanji": u"口", "meanings": u"Mouth, Entrance", "kunyomi": u"くち", "onyomi": u"コー"},
{"kanji": u"車", "meanings": u"Car", "kunyomi": u"くるま", "onyomi": u"シャ"},
{"kanji": u"門", "meanings": u"Gate", "kunyomi": u"かど", "onyomi": u"モン"},
{"kanji": u"火", "meanings": u"Fire", "kunyomi": u"ひ", "onyomi": u"カ"},
{"kanji": u"水", "meanings": u"Water", "kunyomi": u"みず", "onyomi": u"スイ"},
{"kanji": u"金", "meanings": u"Metal, Money", "kunyomi": u"かなえ", "onyomi": u"キン"},
{"kanji": u"土", "meanings": u"Earth, Ground", "kunyomi": u"つち", "onyomi": u"ドー"},
{"kanji": u"子", "meanings": u"Child", "kunyomi": u"こ", "onyomi": u"シ"},
{"kanji": u"女", "meanings": u"Woman", "kunyomi": u"おんな", "onyomi": u"ジョ"},
{"kanji": u"学", "meanings": u"School, Study", "kunyomi": u"まなぶ", "onyomi": u"ガク"},
{"kanji": u"生", "meanings": u"Life, Born", "kunyomi": u"いきる", "onyomi": u"セン"},
{"kanji": u"先", "meanings": u"Previous", "kunyomi": u"さき", "onyomi": u"セイ"},
{"kanji": u"私", "meanings": u"Me (I), Private", "kunyomi": u"わたし", "onyomi": u"シ"},
{"kanji": u"一", "meanings": u"One", "kunyomi": u"ひとつ", "onyomi": u"イチ"},
{"kanji": u"二", "meanings": u"Two", "kunyomi": u"ふたつ", "onyomi": u"ニ"},
{"kanji": u"三", "meanings": u"Three", "kunyomi": u"みつ", "onyomi": u"サン"},
{"kanji": u"四", "meanings": u"Four", "kunyomi": u"よっつ", "onyomi": u"シ"},
{"kanji": u"五", "meanings": u"Five", "kunyomi": u"いっつ", "onyomi": u"ゴ"},
{"kanji": u"六", "meanings": u"Six", "kunyomi": u"むっつ", "onyomi": u"ロク"},
{"kanji": u"七", "meanings": u"Seven", "kunyomi": u"ななつ", "onyomi": u"シチ"},
{"kanji": u"八", "meanings": u"Eight", "kunyomi": u"やっつ", "onyomi": u"ハチ"},
{"kanji": u"九", "meanings": u"Nine", "kunyomi": u"ここのつ", "onyomi": u"キュウ"},
{"kanji": u"十", "meanings": u"Ten", "kunyomi": u"とお", "onyomi": u"ジュウ"},
{"kanji": u"百", "meanings": u"Hundred", "kunyomi": u"ひゃく", "onyomi": u"ヒャク"},
{"kanji": u"千", "meanings": u"Thousand", "kunyomi": u"せん", "onyomi": u"セン"},
{"kanji": u"万", "meanings": u"Ten Thousand", "kunyomi": u"まん", "onyomi": u"マン"},
{"kanji": u"円", "meanings": u"Yen", "kunyomi": u"えん", "onyomi": u"エン"},
{"kanji": u"年", "meanings": u"Year", "kunyomi": u"とし", "onyomi": u"ネン"},
{"kanji": u"上", "meanings": u"Above", "kunyomi": u"うえ", "onyomi": u"ジョー"},
{"kanji": u"下", "meanings": u"Under", "kunyomi": u"した", "onyomi": u"ゲ"},
{"kanji": u"中", "meanings": u"Inside, Middle", "kunyomi": u"なか", "onyomi": u"チュー"},
{"kanji": u"大", "meanings": u"Big", "kunyomi": u"おお（きい", "onyomi": u"ダイ"},
{"kanji": u"小", "meanings": u"Small", "kunyomi": u"ち(さい)", "onyomi": u"ショー"},
{"kanji": u"本", "meanings": u"Book, Root", "kunyomi": u"もと", "onyomi": u"ホン"},
{"kanji": u"半", "meanings": u"Half", "kunyomi": u"んかば", "onyomi": u"ハン"},
{"kanji": u"分", "meanings": u"Divide", "kunyomi": u"わける", "onyomi": u"フン、ブン"},
{"kanji": u"力", "meanings": u"Power", "kunyomi": u"ちから", "onyomi": u"リョク"},
{"kanji": u"何", "meanings": u"What", "kunyomi": u"なに", "onyomi": u"カ"},
{"kanji": u"明", "meanings": u"Bright", "kunyomi": u"あかるい", "onyomi": u"ミョウ"},
{"kanji": u"休", "meanings": u"Rest", "kunyomi": u"やすみ", "onyomi": u"キュウ"},
{"kanji": u"体", "meanings": u"Body", "kunyomi": u"からだ", "onyomi": u"タイ"},
{"kanji": u"好", "meanings": u"Like/Love", "kunyomi": u"すき", "onyomi": u"コウ"},
{"kanji": u"男", "meanings": u"Man", "kunyomi": u"おとこ", "onyomi": u"ダン"},
{"kanji": u"林", "meanings": u"Wood", "kunyomi": u"はやし", "onyomi": u"リン"},
{"kanji": u"森", "meanings": u"Forest", "kunyomi": u"もり", "onyomi": u"シン"},
{"kanji": u"間", "meanings": u"Duration", "kunyomi": u"あいだ", "onyomi": u"カン"},
{"kanji": u"畑", "meanings": u"Cultivated Land", "kunyomi": u"はたけ", "onyomi": u"―"},
{"kanji": u"岩", "meanings": u"Boulder", "kunyomi": u"いわ", "onyomi": u"ガン"},
{"kanji": u"目", "meanings": u"Eye", "kunyomi": u"め", "onyomi": u"ボケ"},
{"kanji": u"耳", "meanings": u"Ear", "kunyomi": u"みみ", "onyomi": u"ジ"},
{"kanji": u"手", "meanings": u"Hand", "kunyomi": u"て", "onyomi": u"シュ"},
{"kanji": u"足", "meanings": u"Legs/Pair", "kunyomi": u"あし", "onyomi": u"ソク"},
{"kanji": u"雨", "meanings": u"Rain", "kunyomi": u"あめ", "onyomi": u"ウ"},
{"kanji": u"竹", "meanings": u"Bamboo", "kunyomi": u"たけ", "onyomi": u"チク"},
{"kanji": u"米", "meanings": u"Rice/America", "kunyomi": u"こめ", "onyomi": u"ベイ"},
{"kanji": u"貝", "meanings": u"Shellfish", "kunyomi": u"かい", "onyomi": u"バイ"},
{"kanji": u"石", "meanings": u"Rock", "kunyomi": u"いし", "onyomi": u"セキ"},
{"kanji": u"糸", "meanings": u"Thread", "kunyomi": u"いと", "onyomi": u"シ"},
{"kanji": u"花", "meanings": u"Flower", "kunyomi": u"はな", "onyomi": u"カ, ケ"},
{"kanji": u"茶", "meanings": u"Tea", "kunyomi": u"ちゃ", "onyomi": u"[TODO]"},
{"kanji": u"肉", "meanings": u"Meat", "kunyomi": u"にく", "onyomi": u"[TODO]"},
{"kanji": u"文", "meanings": u"Sentences", "kunyomi": u"ぶん", "onyomi": u"[TODO]"},
{"kanji": u"字", "meanings": u"Letter", "kunyomi": u"じ", "onyomi": u"[TODO]"},
{"kanji": u"物", "meanings": u"Thing", "kunyomi": u"もの", "onyomi": u"[TODO]"},
{"kanji": u"牛", "meanings": u"Cow", "kunyomi": u"ぎゅ", "onyomi": u"[TODO]"},
{"kanji": u"馬", "meanings": u"Horse", "kunyomi": u"うま", "onyomi": u"[TODO]"},
{"kanji": u"鳥", "meanings": u"Bird", "kunyomi": u"とり", "onyomi": u"[TODO]"},
{"kanji": u"魚", "meanings": u"Fish", "kunyomi": u"さかな", "onyomi": u"[TODO]"},
{"kanji": u"新", "meanings": u"New", "kunyomi": u"あたらし", "onyomi": u"[TODO]"},
{"kanji": u"古", "meanings": u"Old", "kunyomi": u"ふるい", "onyomi": u"[TODO]"},
{"kanji": u"長", "meanings": u"Long", "kunyomi": u"ながい", "onyomi": u"[TODO]"},
{"kanji": u"短", "meanings": u"Short", "kunyomi": u"みじかい", "onyomi": u"[TODO]"},
{"kanji": u"高", "meanings": u"Expensive/Tall", "kunyomi": u"たかい", "onyomi": u"[TODO]"},
{"kanji": u"安", "meanings": u"Cheap/Safe", "kunyomi": u"やすい", "onyomi": u"[TODO]"},
{"kanji": u"低", "meanings": u"Low", "kunyomi": u"ひくい", "onyomi": u"[TODO]"},
{"kanji": u"暗", "meanings": u"Dark/Dim", "kunyomi": u"くらい", "onyomi": u"[TODO]"},
{"kanji": u"多", "meanings": u"Many", "kunyomi": u"おおい", "onyomi": u"[TODO]"},
{"kanji": u"少", "meanings": u"Few", "kunyomi": u"すこし", "onyomi": u"[TODO]"},
{"kanji": u"行", "meanings": u"To Go", "kunyomi": u"いきます", "onyomi": u"コウ"},
{"kanji": u"来", "meanings": u"To Come", "kunyomi": u"きます", "onyomi": u"ライ"},
{"kanji": u"帰", "meanings": u"To Return", "kunyomi": u"かえります", "onyomi": u"キ"},
{"kanji": u"食", "meanings": u"Eat", "kunyomi": u"たべます", "onyomi": u"ショク"},
{"kanji": u"飲", "meanings": u"Drink", "kunyomi": u"のみます", "onyomi": u"イン"},
{"kanji": u"見", "meanings": u"See/Look", "kunyomi": u"みます", "onyomi": u"ケン"},
{"kanji": u"聞", "meanings": u"Hear/Listen", "kunyomi": u"ききます", "onyomi": u"ブン"},
{"kanji": u"読", "meanings": u"Read", "kunyomi": u"よみます", "onyomi": u"ドク"},
{"kanji": u"書", "meanings": u"Write", "kunyomi": u"かきます", "onyomi": u"ショ"},
{"kanji": u"話", "meanings": u"Talk", "kunyomi": u"はなし", "onyomi": u"ワ"},
{"kanji": u"買", "meanings": u"Buy", "kunyomi": u"かいます", "onyomi": u"バイ"},
{"kanji": u"教", "meanings": u"Educate/Teach", "kunyomi": u"おしえます", "onyomi": u"オンヨミ"},
{"kanji": u"朝", "meanings": u"Morning", "kunyomi": u"あさ", "onyomi": u"チョウ"},
{"kanji": u"昼", "meanings": u"Noon", "kunyomi": u"ひる", "onyomi": u"チュウ"},
{"kanji": u"夜", "meanings": u"Night", "kunyomi": u"よる", "onyomi": u"ヤ"},
{"kanji": u"晩", "meanings": u"Night-", "kunyomi": u"-", "onyomi": u"バン"},
{"kanji": u"夕", "meanings": u"Evening", "kunyomi": u"ゆう", "onyomi": u"セキ"},
{"kanji": u"方", "meanings": u"Direction", "kunyomi": u"かた", "onyomi": u"ホウ"}
]