#!/usr/bin/env python3
import json
import random
import os
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MEMORY_DIR = os.path.join(SCRIPT_DIR, "memory")
PREFS_FILE = os.path.join(MEMORY_DIR, "recipe-prefs.json")

RECIPES = [
    {
        "name": "牛油果鸡蛋全麦三明治",
        "emoji": "🥪",
        "category": "三明治",
        "goals": ["减脂", "低卡"],
        "sub_categories": ["通勤便携", "低脂减脂餐"],
        "tags": ["减脂", "低卡", "免油炸", "高蛋白"],
        "time": "8分钟",
        "calories": "约320kcal",
        "protein": "12g",
        "fullness": "★★★★☆",
        "scene": "早午餐/通勤便携",
        "tools": ["平底锅", "砧板", "刀"],
        "allergy_tags": ["鸡蛋", "小麦"],
        "ingredients": [
            {"name": "全麦吐司", "amount": "2片（约60g）", "highlight": False},
            {"name": "牛油果", "amount": "半个（约70g）", "highlight": False},
            {"name": "鸡蛋", "amount": "1个", "highlight": False},
            {"name": "柠檬汁", "amount": "1小勺（约5ml）", "highlight": True, "note": "防氧化变黑，易遗漏！"},
            {"name": "黑胡椒碎", "amount": "1小撮（约0.5g）", "highlight": True},
            {"name": "盐", "amount": "1小撮（约0.5g）", "highlight": False},
            {"name": "橄榄油", "amount": "1小勺（约5ml）", "highlight": False},
        ],
        "substitutions": [
            "牛油果 → 奶油奶酪15g（口感更绵密）",
            "全麦吐司 → 杂粮馒头1个（对半切开，更饱腹）",
            "柠檬汁 → 白醋2-3滴（同样防氧化）",
        ],
        "steps": [
            "牛油果对半切开，取半个用勺子挖出果肉，放入碗中加柠檬汁、盐，用叉子压成泥",
            "平底锅小火加热，刷橄榄油，打入鸡蛋煎至蛋白凝固、蛋黄半熟（约2分钟）",
            "全麦吐司放入平底锅边缘，利用余温烘至微脆（约30秒/面）",
            "取一片吐司，铺满牛油果泥，放上煎蛋，撒黑胡椒碎，盖上另一片吐司",
            "对角线切开，完成！",
        ],
        "quick_steps": [
            "牛油果+柠檬汁+盐压成泥",
            "小火煎蛋2分钟至蛋白凝固",
            "吐司余温烘脆30秒/面",
            "铺牛油果泥→放煎蛋→撒黑胡椒→盖吐司→对切",
        ],
        "tips": [
            "加一片番茄增加清爽口感和层次感",
            "喜欢辣味可挤少许是拉差酱，提味不增负担",
        ],
        "warnings": [
            "牛油果选按上去微微软的，太硬无法压泥，太软发黑变质",
            "煎蛋全程小火！大火容易焦底",
            "柠檬汁一定要加，否则牛油果10分钟内变黑影响卖相",
        ],
        "morning_tip": "早晨来一份，元气满满开启新一天～",
        "evening_tip": "轻盈饱腹，晚间也不怕负担～",
    },
    {
        "name": "金枪鱼玉米沙拉三明治",
        "emoji": "🥪",
        "category": "三明治",
        "goals": ["减脂", "低卡", "增肌"],
        "sub_categories": ["通勤便携", "低脂减脂餐"],
        "tags": ["减脂", "低卡", "免油炸", "极简5分钟", "高蛋白", "增肌"],
        "time": "5分钟",
        "calories": "约280kcal",
        "protein": "22g",
        "fullness": "★★★☆☆",
        "scene": "早午餐/通勤便携",
        "tools": ["碗", "勺子", "刀"],
        "allergy_tags": ["鸡蛋", "小麦", "鱼"],
        "ingredients": [
            {"name": "全麦吐司", "amount": "2片（约60g）", "highlight": False},
            {"name": "水浸金枪鱼罐头", "amount": "半罐（约60g）", "highlight": False},
            {"name": "甜玉米粒", "amount": "2大勺（约30g）", "highlight": False},
            {"name": "低脂沙拉酱", "amount": "1大勺（约15g）", "highlight": True, "note": "易遗漏！"},
            {"name": "黑胡椒碎", "amount": "1小撮（约0.5g）", "highlight": False},
            {"name": "生菜叶", "amount": "1-2片", "highlight": False},
        ],
        "substitutions": [
            "水浸金枪鱼 → 鸡胸肉80g（撕成丝，更鲜嫩）",
            "低脂沙拉酱 → 希腊酸奶20g（更健康低卡）",
            "甜玉米粒 → 胡萝卜丁30g（焯水后使用）",
        ],
        "steps": [
            "金枪鱼罐头沥干水分，放入碗中用叉子稍微拨散",
            "加入甜玉米粒、低脂沙拉酱、黑胡椒碎，搅拌均匀",
            "生菜叶洗净沥干，铺在一片吐司上",
            "将金枪鱼玉米沙拉均匀铺在生菜上，盖上另一片吐司",
            "对角线切开，完成！",
        ],
        "quick_steps": [
            "金枪鱼沥干+玉米粒+沙拉酱+黑胡椒拌匀",
            "吐司铺生菜→铺沙拉→盖吐司→对切",
        ],
        "tips": [
            "金枪鱼一定要沥干水分，否则吐司容易变软塌",
            "可加几滴柠檬汁去腥提鲜",
        ],
        "warnings": [
            "金枪鱼罐头选水浸的，油浸的热量翻倍",
            "沙拉酱别贪多，1大勺足够，多了热量飙升",
        ],
        "morning_tip": "快手5分钟，赶早也不慌～",
        "evening_tip": "清爽无负担，晚间刚刚好～",
    },
    {
        "name": "花生酱香蕉三明治",
        "emoji": "🥪",
        "category": "三明治",
        "goals": ["增肌", "饱腹"],
        "sub_categories": ["通勤便携", "隔夜可备餐"],
        "tags": ["饱腹", "免油炸", "极简5分钟", "增肌", "高蛋白"],
        "time": "3分钟",
        "calories": "约380kcal",
        "protein": "10g",
        "fullness": "★★★★★",
        "scene": "早午餐/通勤便携/隔夜备餐",
        "tools": ["刀", "勺子"],
        "allergy_tags": ["小麦", "坚果"],
        "ingredients": [
            {"name": "全麦吐司", "amount": "2片（约60g）", "highlight": False},
            {"name": "花生酱", "amount": "1.5大勺（约25g）", "highlight": True, "note": "选无糖款更健康"},
            {"name": "香蕉", "amount": "半根（约60g）", "highlight": False},
            {"name": "蜂蜜", "amount": "1小勺（约5ml）", "highlight": True, "note": "可选，增加甜度"},
        ],
        "substitutions": [
            "花生酱 → 杏仁酱20g（同样坚果香）",
            "全麦吐司 → 贝果1个（对半切开，更有嚼劲）",
            "蜂蜜 → 枫糖浆5ml（风味更独特）",
        ],
        "steps": [
            "香蕉切成约5mm厚的圆片",
            "一片吐司均匀涂抹花生酱",
            "将香蕉片紧密铺在花生酱上",
            "淋上蜂蜜（可选），盖上另一片吐司",
            "对角线切开，完成！",
        ],
        "quick_steps": [
            "香蕉切薄片",
            "吐司涂花生酱→铺香蕉→淋蜂蜜→盖吐司→对切",
        ],
        "tips": [
            "花生酱选无糖无添加的纯花生酱，配料表只有花生",
            "隔夜备餐：做好后用保鲜膜包紧冷藏，早晨直接带走",
        ],
        "warnings": [
            "花生酱别涂太厚，1.5大勺足够，热量较高",
            "隔夜备餐不要加蜂蜜，会渗入吐司变软",
        ],
        "morning_tip": "能量满满，一上午都不饿～",
        "evening_tip": "饱腹抗饿，加班夜宵首选～",
    },
    {
        "name": "蒜香西蓝花炒虾仁",
        "emoji": "🍳",
        "category": "快手炒菜",
        "goals": ["减脂", "低卡", "增肌"],
        "sub_categories": ["低脂减脂餐"],
        "tags": ["减脂", "低卡", "免油炸", "饱腹", "高蛋白", "增肌"],
        "time": "12分钟",
        "calories": "约220kcal",
        "protein": "25g",
        "fullness": "★★★★☆",
        "scene": "早午餐/低脂减脂餐",
        "tools": ["平底锅", "砧板", "刀"],
        "allergy_tags": ["虾", "贝类"],
        "ingredients": [
            {"name": "虾仁", "amount": "100g", "highlight": False},
            {"name": "西蓝花", "amount": "150g（约小半棵）", "highlight": False},
            {"name": "蒜末", "amount": "3瓣（约10g）", "highlight": True, "note": "提香关键，易遗漏！"},
            {"name": "生抽", "amount": "1大勺（约15ml）", "highlight": True},
            {"name": "料酒", "amount": "1小勺（约5ml）", "highlight": False},
            {"name": "盐", "amount": "1小撮（约1g）", "highlight": False},
            {"name": "橄榄油", "amount": "1小勺（约5ml）", "highlight": False},
        ],
        "substitutions": [
            "虾仁 → 鸡胸肉丁120g（提前腌制10分钟更嫩）",
            "西蓝花 → 芦笋150g（去老根切段）",
            "料酒 → 姜汁5ml（去腥效果更好）",
        ],
        "steps": [
            "西蓝花掰成小朵，清水浸泡5分钟后洗净沥干",
            "烧一锅水，水开后加少许盐，西蓝花焯水1分钟捞出沥干",
            "虾仁加料酒、少许盐腌制2分钟",
            "平底锅小火加热橄榄油，爆香蒜末（约30秒）",
            "转中火放入虾仁翻炒至变色（约1.5分钟）",
            "加入西蓝花、生抽，大火快速翻炒均匀（约1分钟）",
            "尝味后可补少许盐，出锅！",
        ],
        "quick_steps": [
            "西蓝花焯水1分钟捞出",
            "虾仁+料酒腌2分钟",
            "小火爆香蒜末→炒虾仁至变色→加西蓝花+生抽大火翻匀",
        ],
        "tips": [
            "虾仁提前用厨房纸吸干水分，炒出来更弹嫩",
            "最后大火快炒时间要短，西蓝花保持脆嫩口感",
        ],
        "warnings": [
            "西蓝花焯水不要超过1分钟，否则变黄变软",
            "虾仁炒到刚好变色就盛出，过火会老",
            "蒜末小火爆香，大火会糊发苦",
        ],
        "morning_tip": "清爽高蛋白，轻盈开启新一天～",
        "evening_tip": "低卡高蛋白，晚间吃也无负担～",
    },
    {
        "name": "番茄鸡蛋炒面",
        "emoji": "🍳",
        "category": "快手炒菜",
        "goals": ["增肌", "饱腹"],
        "sub_categories": ["通勤便携"],
        "tags": ["饱腹", "高蛋白", "增肌"],
        "time": "15分钟",
        "calories": "约420kcal",
        "protein": "18g",
        "fullness": "★★★★★",
        "scene": "早午餐/通勤便携",
        "tools": ["炒锅/平底锅", "砧板", "刀", "锅铲"],
        "allergy_tags": ["鸡蛋", "小麦"],
        "ingredients": [
            {"name": "挂面/细面", "amount": "80g（约1人份）", "highlight": False},
            {"name": "番茄", "amount": "1个（约150g）", "highlight": False},
            {"name": "鸡蛋", "amount": "1个", "highlight": False},
            {"name": "生抽", "amount": "1.5大勺（约22ml）", "highlight": True},
            {"name": "老抽", "amount": "半小勺（约2.5ml）", "highlight": True, "note": "上色用，易遗漏！"},
            {"name": "白糖", "amount": "1小勺（约5g）", "highlight": True, "note": "提鲜去酸，关键！"},
            {"name": "葱花", "amount": "1大勺（约5g）", "highlight": False},
            {"name": "食用油", "amount": "1大勺（约15ml）", "highlight": False},
        ],
        "substitutions": [
            "挂面 → 荞麦面80g（更低GI，更饱腹）",
            "白糖 → 零卡糖3g（减脂友好）",
            "老抽 → 可省略（不影响味道，仅影响颜色）",
        ],
        "steps": [
            "番茄顶部划十字，开水烫30秒去皮，切成小块",
            "锅中烧水煮面至8成熟（比包装时间少1分钟），捞出过凉水沥干",
            "鸡蛋打散，锅中加半大勺油中火炒至凝固盛出",
            "锅中加剩余半大勺油，放入番茄块中火翻炒出汁（约2分钟）",
            "加入生抽、老抽、白糖，翻炒至酱汁浓稠",
            "放入面条和炒蛋，大火快速翻拌均匀（约1分钟）",
            "撒上葱花，出锅！",
        ],
        "quick_steps": [
            "番茄去皮切块",
            "煮面至8成熟捞出过凉水",
            "炒蛋盛出→炒番茄出汁→加生抽/老抽/糖→放面和蛋翻匀→撒葱花",
        ],
        "tips": [
            "番茄一定要炒出汁再调味，酱汁才浓郁",
            "面条过凉水是关键，否则炒出来粘成一坨",
        ],
        "warnings": [
            "面条不要煮全熟，8成熟捞出余温会继续加热",
            "白糖不能省，少了它番茄酸味压不住",
            "最后大火翻拌时间要短，1分钟足够，久了面会断",
        ],
        "morning_tip": "一碗暖胃炒面，满足感拉满～",
        "evening_tip": "热乎炒面暖胃又暖心～",
    },
    {
        "name": "醋溜土豆丝",
        "emoji": "🍳",
        "category": "快手炒菜",
        "goals": ["减脂", "低卡"],
        "sub_categories": ["宿舍无厨具", "低脂减脂餐"],
        "tags": ["减脂", "低卡", "免油炸", "极简5分钟"],
        "time": "10分钟",
        "calories": "约180kcal",
        "protein": "3g",
        "fullness": "★★★☆☆",
        "scene": "早午餐/宿舍无厨具/低脂减脂餐",
        "tools": ["平底锅/电热锅", "擦丝器/刀", "碗"],
        "allergy_tags": [],
        "ingredients": [
            {"name": "土豆", "amount": "1个（约200g）", "highlight": False},
            {"name": "干辣椒", "amount": "2个", "highlight": True, "note": "怕辣可减1个"},
            {"name": "花椒", "amount": "10粒（约1g）", "highlight": True, "note": "提香关键，易遗漏！"},
            {"name": "陈醋", "amount": "2大勺（约30ml）", "highlight": True, "note": "灵魂调料！"},
            {"name": "生抽", "amount": "1大勺（约15ml）", "highlight": False},
            {"name": "盐", "amount": "1小撮（约1g）", "highlight": False},
            {"name": "食用油", "amount": "1大勺（约15ml）", "highlight": False},
            {"name": "葱花", "amount": "1大勺（约5g）", "highlight": False},
        ],
        "substitutions": [
            "陈醋 → 米醋30ml（酸味更柔和）",
            "干辣椒 → 红椒丝15g（不辣增色）",
            "花椒 → 花椒粉1小撮（省去挑出步骤）",
        ],
        "steps": [
            "土豆去皮切成细丝（或用擦丝器），放入清水中浸泡5分钟去除淀粉，捞出沥干",
            "锅中加油中火烧热，放入花椒和干辣椒爆香（约30秒），挑出花椒",
            "大火放入土豆丝，快速翻炒1分钟",
            "沿锅边淋入陈醋（听到嗞啦声就对了），继续翻炒30秒",
            "加入生抽、盐，大火翻炒至土豆丝断生但仍脆爽（约1分钟）",
            "撒上葱花，出锅！",
        ],
        "quick_steps": [
            "土豆切丝泡水5分钟去淀粉沥干",
            "油热爆香花椒干辣椒→大火炒土豆丝1分钟→淋醋→加生抽盐翻匀→撒葱花",
        ],
        "tips": [
            "土豆丝泡水是灵魂步骤，不泡水炒出来粘糊糊",
            "醋要沿锅边淋入，遇热挥发产生醋香，直接浇菜上效果差",
        ],
        "warnings": [
            "土豆丝一定要沥干水分再下锅，带水下锅会溅油",
            "全程大火快炒，超过3分钟就变软塌不脆了",
            "花椒爆香后挑出来，吃到嘴里影响口感",
        ],
        "morning_tip": "酸爽开胃，一口就清醒～",
        "evening_tip": "清爽解腻，晚间吃零负担～",
    },
    {
        "name": "鸡胸肉西兰花糙米饭",
        "emoji": "🍳",
        "category": "快手炒菜",
        "goals": ["增肌", "减脂"],
        "sub_categories": ["低脂减脂餐"],
        "tags": ["减脂", "低卡", "免油炸", "高蛋白", "增肌"],
        "time": "20分钟",
        "calories": "约450kcal",
        "protein": "38g",
        "fullness": "★★★★★",
        "scene": "早午餐/低脂减脂餐",
        "tools": ["平底锅", "电饭煲", "砧板", "刀"],
        "allergy_tags": ["鸡蛋", "大豆"],
        "ingredients": [
            {"name": "糙米饭", "amount": "100g（熟重，约半碗）", "highlight": False},
            {"name": "鸡胸肉", "amount": "120g", "highlight": False},
            {"name": "西蓝花", "amount": "100g", "highlight": False},
            {"name": "生抽", "amount": "1大勺（约15ml）", "highlight": True},
            {"name": "橄榄油", "amount": "1小勺（约5ml）", "highlight": False},
            {"name": "黑胡椒碎", "amount": "1小撮（约0.5g）", "highlight": False},
            {"name": "盐", "amount": "1小撮（约0.5g）", "highlight": False},
        ],
        "substitutions": [
            "糙米饭 → 藜麦80g（蛋白质更高）",
            "鸡胸肉 → 豆腐120g（素食替代）",
            "西蓝花 → 菠菜150g（同样高纤维）",
        ],
        "steps": [
            "糙米提前浸泡30分钟（或用即食糙米），煮熟备用",
            "鸡胸肉切丁，加少许盐和黑胡椒腌制5分钟",
            "西蓝花掰小朵，焯水2分钟捞出沥干",
            "平底锅小火加热橄榄油，放入鸡胸肉丁煎至两面金黄（约4分钟）",
            "加入西蓝花、生抽，大火翻炒30秒",
            "糙米饭铺底，码上鸡胸肉和西蓝花，完成！",
        ],
        "quick_steps": [
            "糙米煮熟/即食糙米",
            "鸡胸肉切丁腌5分钟",
            "煎鸡胸肉4分钟→加西兰花+生抽大火炒30秒",
            "铺米饭装盘",
        ],
        "tips": [
            "鸡胸肉切丁比切片更容易熟透且不易老",
            "糙米提前一晚煮好冷藏，第二天直接用更省时间",
        ],
        "warnings": [
            "鸡胸肉一定要腌透，否则入味不均",
            "煎鸡胸肉不要大火，表面焦了里面还没熟",
        ],
        "morning_tip": "高蛋白低脂肪，增肌减脂首选～",
        "evening_tip": "营养均衡，吃完不怕胖～",
    },
    {
        "name": "隔夜燕麦杯",
        "emoji": "🌙",
        "category": "晚间营养加餐",
        "goals": ["减脂", "低卡", "增肌"],
        "sub_categories": ["隔夜可备餐", "宿舍无厨具"],
        "tags": ["减脂", "低卡", "免油炸", "极简5分钟", "饱腹", "增肌", "高蛋白"],
        "time": "5分钟（需冷藏4小时以上）",
        "calories": "约260kcal",
        "protein": "15g",
        "fullness": "★★★★☆",
        "scene": "晚间营养加餐/隔夜备餐/宿舍无厨具",
        "tools": ["密封罐/碗", "勺子"],
        "allergy_tags": ["乳制品", "坚果", "麸质"],
        "ingredients": [
            {"name": "即食燕麦片", "amount": "40g（约半杯）", "highlight": False},
            {"name": "牛奶", "amount": "100ml", "highlight": False},
            {"name": "希腊酸奶", "amount": "50g（约3大勺）", "highlight": True, "note": "增加浓稠口感"},
            {"name": "蜂蜜", "amount": "1小勺（约5ml）", "highlight": False},
            {"name": "蓝莓/草莓", "amount": "6-8颗", "highlight": False},
            {"name": "奇亚籽", "amount": "1小勺（约5g）", "highlight": True, "note": "增加饱腹感，易遗漏！"},
        ],
        "substitutions": [
            "牛奶 → 豆浆100ml（乳糖不耐友好）",
            "希腊酸奶 → 普通酸奶80g（口感略稀）",
            "蓝莓 → 香蕉半根切片（更甜更饱腹）",
            "奇亚籽 → 亚麻籽5g（同样高纤维）",
        ],
        "steps": [
            "密封罐中放入燕麦片、奇亚籽，搅拌均匀",
            "加入牛奶、蜂蜜，搅拌至燕麦完全浸润",
            "加入希腊酸奶，轻轻搅拌（保留层次感）",
            "盖上盖子，放入冰箱冷藏4小时以上（过夜最佳）",
            "食用前铺上蓝莓/草莓，完成！",
        ],
        "quick_steps": [
            "燕麦+奇亚籽拌匀→加牛奶蜂蜜搅匀→加酸奶→冷藏4h+→铺水果",
        ],
        "tips": [
            "前一晚做好，第二天早上直接吃，零等待",
            "可叠加多层：燕麦→牛奶→水果→酸奶，颜值更高",
        ],
        "warnings": [
            "奇亚籽不要超过1小勺，多了会吸水膨胀口感奇怪",
            "冷藏不要超过24小时，燕麦会过软",
            "宿舍党用保温杯也能做，常温静置6小时即可",
        ],
        "morning_tip": "昨晚备好的小确幸，今早直接享用～",
        "evening_tip": "提前备好，明天一早就有惊喜～",
    },
    {
        "name": "蜂蜜柠檬温水+全麦吐司",
        "emoji": "🌙",
        "category": "晚间营养加餐",
        "goals": ["减脂", "低卡"],
        "sub_categories": ["宿舍无厨具", "低脂减脂餐"],
        "tags": ["减脂", "低卡", "免油炸", "无蛋奶", "极简5分钟"],
        "time": "3分钟",
        "calories": "约160kcal",
        "protein": "4g",
        "fullness": "★★☆☆☆",
        "scene": "晚间营养加餐/宿舍无厨具/低脂减脂餐",
        "tools": ["杯子", "刀"],
        "allergy_tags": ["小麦"],
        "ingredients": [
            {"name": "全麦吐司", "amount": "1片（约30g）", "highlight": False},
            {"name": "蜂蜜", "amount": "1大勺（约15ml）", "highlight": False},
            {"name": "柠檬", "amount": "2-3片", "highlight": True, "note": "新鲜柠檬最佳"},
            {"name": "温水", "amount": "250ml", "highlight": False},
        ],
        "substitutions": [
            "蜂蜜 → 枫糖浆10ml（不同风味）",
            "全麦吐司 → 苏打饼干3片（约20g）",
            "柠檬 → 青柠2片（更清香）",
        ],
        "steps": [
            "杯中倒入温水（约60℃，不烫嘴即可）",
            "加入蜂蜜，搅拌至完全溶解",
            "放入柠檬片，轻轻搅拌",
            "全麦吐司直接食用或用热水杯外壁温热1分钟",
            "搭配享用，完成！",
        ],
        "quick_steps": [
            "温水+蜂蜜搅匀+放柠檬片",
            "配全麦吐司1片",
        ],
        "tips": [
            "水温不要超过70℃，会破坏蜂蜜营养",
            "柠檬片不要泡太久，超过15分钟会发苦",
        ],
        "warnings": [
            "晚间不要喝太多水，250ml刚好",
            "空腹不要喝柠檬水，胃酸多的同学注意",
        ],
        "morning_tip": "温暖一杯，唤醒身体～",
        "evening_tip": "轻盈收尾，安心入眠～",
    },
    {
        "name": "牛油果虾仁沙拉",
        "emoji": "🌙",
        "category": "晚间营养加餐",
        "goals": ["减脂", "低卡", "增肌"],
        "sub_categories": ["低脂减脂餐"],
        "tags": ["减脂", "低卡", "免油炸", "饱腹", "高蛋白", "增肌"],
        "time": "10分钟",
        "calories": "约280kcal",
        "protein": "20g",
        "fullness": "★★★★☆",
        "scene": "晚间营养加餐/低脂减脂餐",
        "tools": ["碗", "刀", "勺子"],
        "allergy_tags": ["虾", "贝类"],
        "ingredients": [
            {"name": "虾仁", "amount": "80g", "highlight": False},
            {"name": "牛油果", "amount": "半个（约70g）", "highlight": False},
            {"name": "小番茄", "amount": "5-6颗（约80g）", "highlight": False},
            {"name": "混合生菜", "amount": "1把（约50g）", "highlight": False},
            {"name": "柠檬汁", "amount": "1大勺（约15ml）", "highlight": True, "note": "沙拉汁+防氧化，双重作用！"},
            {"name": "橄榄油", "amount": "1小勺（约5ml）", "highlight": True},
            {"name": "黑胡椒碎", "amount": "1小撮（约0.5g）", "highlight": False},
            {"name": "盐", "amount": "1小撮（约0.5g）", "highlight": False},
        ],
        "substitutions": [
            "虾仁 → 鸡胸肉100g（水煮后撕丝）",
            "牛油果 → 奶油奶酪20g（抹在生菜上）",
            "小番茄 → 黄瓜半根切丁（更清爽）",
            "混合生菜 → 圆生菜3-4片（手撕即可）",
        ],
        "steps": [
            "虾仁水煮2分钟至变色，捞出过凉水沥干",
            "牛油果对半切开取半个，切成1cm方块，立即淋半大勺柠檬汁防氧化",
            "小番茄对半切开，混合生菜洗净沥干",
            "碗中放入生菜垫底，摆上虾仁、牛油果块、小番茄",
            "剩余柠檬汁加橄榄油、盐、黑胡椒调成沙拉汁，淋在沙拉上",
            "轻轻翻拌，完成！",
        ],
        "quick_steps": [
            "虾仁煮2分钟沥干",
            "牛油果切丁+淋柠檬汁防氧化",
            "生菜垫底→摆虾仁/牛油果/小番茄→淋柠檬汁+橄榄油+盐+胡椒",
        ],
        "tips": [
            "沙拉汁先调好再淋，比分别淋更均匀",
            "加几颗坚果（核桃碎/杏仁片）增加口感层次",
        ],
        "warnings": [
            "牛油果切好后立刻淋柠檬汁，5分钟内不变色",
            "虾仁不要煮超过2分钟，会老",
            "沙拉吃前再拌，提前拌会出水",
        ],
        "morning_tip": "清爽高蛋白，轻盈一整天～",
        "evening_tip": "低卡饱腹，晚间吃最安心～",
    },
    {
        "name": "香蕉蛋白奶昔",
        "emoji": "🌙",
        "category": "晚间营养加餐",
        "goals": ["增肌", "饱腹"],
        "sub_categories": ["宿舍无厨具", "通勤便携"],
        "tags": ["减脂", "低卡", "免油炸", "极简5分钟", "饱腹", "增肌", "高蛋白"],
        "time": "3分钟",
        "calories": "约230kcal",
        "protein": "30g",
        "fullness": "★★★☆☆",
        "scene": "晚间营养加餐/宿舍无厨具/通勤便携",
        "tools": ["搅拌杯/摇摇杯", "勺子"],
        "allergy_tags": ["乳制品"],
        "ingredients": [
            {"name": "香蕉", "amount": "1根（约120g）", "highlight": False},
            {"name": "牛奶", "amount": "200ml", "highlight": False},
            {"name": "蛋白粉", "amount": "1勺（约25g）", "highlight": True, "note": "增肌减脂必备"},
            {"name": "蜂蜜", "amount": "1小勺（约5ml）", "highlight": False},
            {"name": "冰块", "amount": "3-4块（可选）", "highlight": False},
        ],
        "substitutions": [
            "牛奶 → 豆浆200ml（乳糖不耐友好）",
            "蛋白粉 → 希腊酸奶100g（蛋白质略低但口感更顺滑）",
            "香蕉 → 芒果80g（不同风味）",
        ],
        "steps": [
            "香蕉掰成小段放入搅拌杯",
            "加入牛奶、蛋白粉、蜂蜜",
            "加入冰块（可选），盖紧杯盖",
            "用力搅拌/摇晃30秒至均匀顺滑",
            "倒入杯中，完成！",
        ],
        "quick_steps": [
            "香蕉+牛奶+蛋白粉+蜂蜜→搅拌30秒→完成",
        ],
        "tips": [
            "香蕉提前冷冻，打出来更浓稠像奶昔",
            "没有搅拌杯就用摇摇杯，香蕉先压成泥再摇",
        ],
        "warnings": [
            "蛋白粉不要用开水冲，会结块",
            "摇摇杯一定要盖紧，不然会喷",
        ],
        "morning_tip": "一杯下肚，能量满格～",
        "evening_tip": "运动后来一杯，修复又饱腹～",
    },
    {
        "name": "鸡蛋蔬菜卷饼",
        "emoji": "🥪",
        "category": "三明治",
        "goals": ["减脂", "增肌"],
        "sub_categories": ["通勤便携", "低脂减脂餐"],
        "tags": ["减脂", "饱腹", "高蛋白", "增肌"],
        "time": "10分钟",
        "calories": "约300kcal",
        "protein": "16g",
        "fullness": "★★★★☆",
        "scene": "早午餐/通勤便携/低脂减脂餐",
        "tools": ["平底锅", "砧板", "刀"],
        "allergy_tags": ["鸡蛋", "小麦"],
        "ingredients": [
            {"name": "全麦卷饼", "amount": "1张（约50g）", "highlight": False},
            {"name": "鸡蛋", "amount": "1个", "highlight": False},
            {"name": "生菜", "amount": "2-3片", "highlight": False},
            {"name": "胡萝卜", "amount": "1小段（约30g）", "highlight": False},
            {"name": "甜面酱/低脂沙拉酱", "amount": "1小勺（约5g）", "highlight": True, "note": "提味关键，易遗漏！"},
            {"name": "食用油", "amount": "1小勺（约5ml）", "highlight": False},
        ],
        "substitutions": [
            "全麦卷饼 → 越南米纸1张（需温水泡软，更低卡）",
            "甜面酱 → 番茄酱10g（酸甜口味）",
            "胡萝卜 → 黄瓜1小段（更清爽）",
        ],
        "steps": [
            "胡萝卜切细丝，生菜洗净沥干",
            "鸡蛋打散，平底锅刷油小火倒入蛋液，摊成薄蛋饼（约1.5分钟）",
            "蛋饼盛出，锅中放入卷饼两面加热至微热变软（约30秒）",
            "卷饼上涂酱，铺上生菜、蛋饼、胡萝卜丝",
            "从一端卷紧，斜刀切半，完成！",
        ],
        "quick_steps": [
            "胡萝卜切丝·生菜洗净",
            "摊薄蛋饼→卷饼加热→涂酱→铺菜蛋→卷紧切半",
        ],
        "tips": [
            "卷的时候先折底部再卷两侧，不容易散",
            "多加一张蛋饼口感更扎实",
        ],
        "warnings": [
            "蛋饼要摊薄，太厚卷不起来",
            "卷饼加热时间不要长，变硬就不好卷了",
        ],
        "morning_tip": "一手握着走，一手拿卷饼～",
        "evening_tip": "轻巧一卷，晚间刚刚好～",
    },
    {
        "name": "蒜蓉蒸茄子",
        "emoji": "🌙",
        "category": "晚间营养加餐",
        "goals": ["减脂", "低卡"],
        "sub_categories": ["宿舍无厨具", "低脂减脂餐"],
        "tags": ["减脂", "低卡", "免油炸", "无蛋奶"],
        "time": "15分钟",
        "calories": "约120kcal",
        "protein": "2g",
        "fullness": "★★☆☆☆",
        "scene": "晚间营养加餐/宿舍无厨具/低脂减脂餐",
        "tools": ["碗/盘子", "蒸锅/电饭锅"],
        "allergy_tags": [],
        "ingredients": [
            {"name": "长茄子", "amount": "1根（约200g）", "highlight": False},
            {"name": "蒜末", "amount": "4瓣（约15g）", "highlight": True, "note": "灵魂调料！"},
            {"name": "生抽", "amount": "2大勺（约30ml）", "highlight": True},
            {"name": "香醋", "amount": "1大勺（约15ml）", "highlight": True, "note": "提鲜解腻，易遗漏！"},
            {"name": "小米辣", "amount": "1个（可选）", "highlight": False},
            {"name": "葱花", "amount": "1大勺（约5g）", "highlight": False},
        ],
        "substitutions": [
            "长茄子 → 圆茄子半个（需切厚片）",
            "香醋 → 陈醋10ml（酸味更浓）",
            "小米辣 → 红椒碎5g（不辣增色）",
        ],
        "steps": [
            "茄子洗净，对半切开再切成长条，放入碗中",
            "蒸锅水开后放入茄子，大火蒸8分钟至软烂",
            "蒸茄子期间调汁：蒜末+生抽+香醋+小米辣搅匀",
            "茄子蒸好后取出，淋上调好的蒜蓉汁",
            "撒上葱花，完成！",
        ],
        "quick_steps": [
            "茄子切条→大火蒸8分钟→蒜末+生抽+香醋+小米辣调汁→淋汁撒葱花",
        ],
        "tips": [
            "蒸比炒更健康，茄子不吸油热量极低",
            "调汁时加几滴香油更香（可选）",
        ],
        "warnings": [
            "茄子一定要蒸透，筷子能轻松插入才算好",
            "蒸好后会出水，倒掉多余水分再淋汁",
            "蒜末不要蒸，生蒜淋上去更香",
        ],
        "morning_tip": "清爽开胃，轻盈无负担～",
        "evening_tip": "极低热量，晚间放心吃～",
    },
    {
        "name": "鸡蛋白蔬菜粥",
        "emoji": "🌙",
        "category": "晚间营养加餐",
        "goals": ["减脂", "低卡", "增肌"],
        "sub_categories": ["宿舍无厨具", "低脂减脂餐"],
        "tags": ["减脂", "低卡", "免油炸", "无蛋奶", "极简5分钟", "高蛋白", "增肌"],
        "time": "10分钟",
        "calories": "约180kcal",
        "protein": "18g",
        "fullness": "★★★☆☆",
        "scene": "晚间营养加餐/宿舍无厨具/低脂减脂餐",
        "tools": ["微波炉适用碗/电饭锅", "刀"],
        "allergy_tags": ["鸡蛋"],
        "ingredients": [
            {"name": "即食燕麦片", "amount": "30g（约3大勺）", "highlight": False},
            {"name": "鸡蛋白", "amount": "3个", "highlight": False},
            {"name": "菠菜", "amount": "30g", "highlight": False},
            {"name": "盐", "amount": "1小撮（约0.5g）", "highlight": False},
            {"name": "黑胡椒碎", "amount": "1小撮（约0.3g）", "highlight": False},
        ],
        "substitutions": [
            "鸡蛋白 → 嫩豆腐50g（素食替代）",
            "菠菜 → 任何绿叶蔬菜30g",
        ],
        "steps": [
            "即食燕麦片放入碗中，加150ml热水搅匀",
            "微波炉中火加热1.5分钟（或电饭锅煮3分钟）至燕麦粥浓稠",
            "鸡蛋白打散，淋在燕麦粥上，搅拌均匀",
            "菠菜洗净切碎，撒在粥上",
            "加盐和黑胡椒调味，完成！",
        ],
        "quick_steps": [
            "燕麦+热水搅匀→微波1.5分钟/电饭锅3分钟",
            "淋入打散的蛋白→撒菠菜碎→加盐胡椒",
        ],
        "tips": [
            "只取鸡蛋白热量更低，蛋白质不减",
            "可以加一点酱油调味，增加鲜味",
        ],
        "warnings": [
            "微波炉加热要盖盖子或留孔，否则会喷",
            "鸡蛋白一定要熟透，不要吃生的",
        ],
        "morning_tip": "清淡暖胃，高蛋白低热量～",
        "evening_tip": "睡前一杯，营养又安睡～",
    },
    {
        "name": "烤鸡胸肉藜麦碗",
        "emoji": "🍳",
        "category": "快手炒菜",
        "goals": ["增肌", "减脂"],
        "sub_categories": ["低脂减脂餐", "隔夜可备餐"],
        "tags": ["减脂", "低卡", "免油炸", "高蛋白", "增肌", "饱腹"],
        "time": "25分钟",
        "calories": "约400kcal",
        "protein": "40g",
        "fullness": "★★★★★",
        "scene": "早午餐/低脂减脂餐/隔夜备餐",
        "tools": ["烤箱/空气炸锅", "砧板", "刀", "碗"],
        "allergy_tags": [],
        "ingredients": [
            {"name": "鸡胸肉", "amount": "150g", "highlight": False},
            {"name": "藜麦", "amount": "50g（生重）", "highlight": False},
            {"name": "牛油果", "amount": "半个（约70g）", "highlight": False},
            {"name": "小番茄", "amount": "5-6颗（约80g）", "highlight": False},
            {"name": "柠檬汁", "amount": "1大勺（约15ml）", "highlight": True, "note": "腌肉去腥+调味"},
            {"name": "黑胡椒碎", "amount": "1小撮（约0.5g）", "highlight": False},
            {"name": "盐", "amount": "1小撮（约0.5g）", "highlight": False},
        ],
        "substitutions": [
            "鸡胸肉 → 鲷鱼/龙利鱼150g（海鲜替代）",
            "藜麦 → 糙米60g（更低成本）",
            "牛油果 → 营养酵母5g（增加风味）",
        ],
        "steps": [
            "藜麦洗净，加水（1:2比例）煮15分钟至发芽，捞出沥干",
            "鸡胸肉切条，加柠檬汁、盐、黑胡椒腌10分钟",
            "烤箱预热200℃，放入鸡胸肉烤15分钟（翻面一次）",
            "牛油果和小番茄切块",
            "碗中铺底放藜麦，码上鸡胸肉、牛油果、小番茄",
            "淋少许柠檬汁，完成！",
        ],
        "quick_steps": [
            "藜麦煮15分钟",
            "鸡胸肉腌10分钟→烤箱200℃烤15分钟",
            "切牛油果小番茄→摆盘",
        ],
        "tips": [
            "鸡胸肉切条比整块更容易熟透",
            "可以一次多烤几份，冷藏保存3天",
        ],
        "warnings": [
            "藜麦一定要煮透，没发芽的吃起来发苦",
            "烤鸡胸肉观察颜色，避免烤焦",
        ],
        "morning_tip": "高蛋白碗，能量续航一上午～",
        "evening_tip": "干净饮食，吃出健康来～",
    },
]

CATEGORIES = {
    "1": {"name": "🥪 三明治", "key": "三明治"},
    "2": {"name": "🍳 快手炒菜", "key": "快手炒菜"},
    "3": {"name": "🌙 晚间营养加餐", "key": "晚间营养加餐"},
}

DEMAND_TYPES = {
    "1": {"name": "📂 按品类", "desc": "三明治/快手炒菜/晚间加餐"},
    "2": {"name": "🥕 按食材", "desc": "用你现有的食材做"},
    "3": {"name": "🎯 按目标", "desc": "低卡/减脂/增肌"},
}

GOALS = {
    "1": {"name": "🔥 低卡", "key": "低卡", "desc": "热量≤250kcal"},
    "2": {"name": "💪 减脂", "key": "减脂", "desc": "低脂高纤维"},
    "3": {"name": "🏋️ 增肌", "key": "增肌", "desc": "高蛋白≥20g"},
}


def init_prefs():
    return {
        "favorites": [],
        "disliked_ingredients": [],
        "allergies": [],
        "common_ingredients": [],
        "last_used": None,
    }


def load_prefs():
    if not os.path.exists(MEMORY_DIR):
        os.makedirs(MEMORY_DIR, exist_ok=True)
    if os.path.exists(PREFS_FILE):
        with open(PREFS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return init_prefs()


def save_prefs(prefs):
    if not os.path.exists(MEMORY_DIR):
        os.makedirs(MEMORY_DIR, exist_ok=True)
    with open(PREFS_FILE, "w", encoding="utf-8") as f:
        json.dump(prefs, f, ensure_ascii=False, indent=2)


def get_time_period():
    hour = datetime.now().hour
    if 6 <= hour < 11:
        return "morning"
    elif 11 <= hour < 14:
        return "noon"
    else:
        return "evening"


def get_greeting():
    period = get_time_period()
    greetings = {
        "morning": "☀️ 早上好呀～新的一天从一份清爽轻食开始！",
        "noon": "🌤 中午好～来份快手简餐犒劳自己吧！",
        "evening": "🌙 晚上好～忙碌一天，用轻盈加餐犒劳自己～",
    }
    return greetings[period]


def check_allergy(recipe, prefs):
    allergy_issues = []
    for ing in recipe["ingredients"]:
        ing_name = ing["name"].lower()
        for allergy in prefs.get("allergies", []):
            if allergy.lower() in ing_name or ing_name in allergy.lower():
                allergy_issues.append(ing["name"])
    return allergy_issues


def check_disliked(recipe, prefs):
    disliked = []
    for ing in recipe["ingredients"]:
        ing_name = ing["name"].lower()
        for dislike in prefs.get("disliked_ingredients", []):
            if dislike.lower() in ing_name or ing_name in dislike.lower():
                disliked.append(ing["name"])
    return disliked


def filter_by_goal(recipes, goal_key):
    return [r for r in recipes if goal_key in r.get("goals", [])]


def filter_recipes(category=None, tag=None, sub_category=None, ingredients=None, goal=None, prefs=None):
    results = RECIPES[:]

    if prefs:
        results = [r for r in results if not check_allergy(r, prefs)]

    if category:
        results = [r for r in results if r["category"] == category]
    if tag:
        results = [r for r in results if tag in r["tags"]]
    if sub_category:
        results = [r for r in results if sub_category in r["sub_categories"]]
    if goal:
        results = [r for r in results if goal in r.get("goals", [])]
    if ingredients:
        ing_list = [i.strip() for i in ingredients.replace("，", ",").split(",") if i.strip()]
        matched = []
        for r in results:
            recipe_ings = {ing["name"] for ing in r["ingredients"]}
            overlap = len(set(ing_list) & recipe_ings)
            if overlap > 0:
                matched.append((r, overlap))
        matched.sort(key=lambda x: x[1], reverse=True)
        results = [m[0] for m in matched]

    return results


def display_recipe_full(recipe, prefs=None):
    period = get_time_period()
    tip = recipe["morning_tip"] if period == "morning" else recipe["evening_tip"]

    lines = []
    lines.append(f'{recipe["emoji"]}【{recipe["name"]}】')
    lines.append("")
    lines.append(f'【基础信息】{recipe["time"]}｜{recipe["calories"]}｜蛋白质{recipe["protein"]}｜饱腹指数{recipe["fullness"]}')
    lines.append(f'【目标】{"/".join(recipe.get("goals", []))}｜【场景】{recipe["scene"]}')
    lines.append("")
    lines.append(f'【所需厨具】{"、".join(recipe["tools"])}')
    lines.append("")

    allergy_warn = []
    if prefs:
        allergy_issues = check_allergy(recipe, prefs)
        if allergy_issues:
            allergy_warn = allergy_issues
            lines.append("【⚠️ 过敏提醒】")
            for a in allergy_issues:
                lines.append(f'  ⚠️ 含有「{a}」，你标注了过敏！')
            lines.append("")

    lines.append("【全部食材&精准用量】")
    for ing in recipe["ingredients"]:
        ing_name = ing["name"]
        if prefs and ing_name in prefs.get("disliked_ingredients", []):
            ing_name = f"❌{ing_name}（你不喜欢）"
        if ing.get("highlight"):
            note = f"——{ing['note']}" if ing.get("note") else ""
            lines.append(f'· ⭐{ing["name"]} {ing["amount"]}{note}')
        else:
            lines.append(f'· {ing["name"]} {ing["amount"]}')
    lines.append("")
    lines.append("【食材替代方案】")
    for sub in recipe["substitutions"]:
        lines.append(f"· {sub}")
    lines.append("")
    lines.append("【详细制作步骤】")
    for i, step in enumerate(recipe["steps"], 1):
        lines.append(f"{i}. {step}")
    lines.append("")
    lines.append("【口味搭配小技巧】")
    for tip_item in recipe["tips"]:
        lines.append(f"· {tip_item}")
    lines.append("")
    lines.append("【新手避坑指南】")
    for warn in recipe["warnings"]:
        lines.append(f"· ⚠️ {warn}")
    lines.append("")
    lines.append("【暖心小贴士】")
    lines.append(tip)

    return "\n".join(lines)


def display_recipe_quick(recipe, prefs=None):
    period = get_time_period()
    tip = recipe["morning_tip"] if period == "morning" else recipe["evening_tip"]

    lines = []
    lines.append(f'⚡ {recipe["name"]} ｜{recipe["time"]}｜{recipe["calories"]}｜蛋白{recipe["protein"]}')
    lines.append(f'【目标】{"/".join(recipe.get("goals", []))}')

    allergy_warn = []
    if prefs:
        allergy_issues = check_allergy(recipe, prefs)
        if allergy_issues:
            lines.append(f'【⚠️ 过敏】{"、".join(allergy_issues)}')

    ing_parts = []
    for ing in recipe["ingredients"]:
        ing_parts.append(f'{ing["name"]}{ing["amount"].split("（")[0]}')
    lines.append(f'【食材】{" · ".join(ing_parts)}')
    lines.append("")
    lines.append("【步骤】")
    for i, step in enumerate(recipe["quick_steps"], 1):
        lines.append(f"{i}. {step}")
    lines.append("")
    lines.append(tip)

    return "\n".join(lines)


def display_recipe_list(recipes, mode="full", prefs=None, title="菜谱列表"):
    if not recipes:
        print("\n  😅 暂时没有匹配的菜谱，换个条件试试～")
        return None

    print(f"\n  {title}（共 {len(recipes)} 道）")
    for i, r in enumerate(recipes, 1):
        warn_marker = ""
        if prefs:
            allergy = check_allergy(r, prefs)
            if allergy:
                warn_marker = " ⚠️"
        print(f"\n  {i}. {r['emoji']} {r['name']}{warn_marker} ｜{r['time']}｜{r['calories']}｜蛋白{r['protein']}")
        print(f"     目标：{'/'.join(r.get('goals', []))} ｜ 场景：{'、'.join(r['sub_categories'])}")

    print()
    choice = input("  输入编号查看菜谱（回车返回）：").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(recipes):
        return recipes[int(choice) - 1]
    return None


def toggle_favorite(recipe_name, prefs):
    if recipe_name in prefs["favorites"]:
        prefs["favorites"].remove(recipe_name)
        save_prefs(prefs)
        print(f'  🗑 已取消收藏「{recipe_name}」')
        return False
    else:
        prefs["favorites"].append(recipe_name)
        save_prefs(prefs)
        print(f'  ✅ 已收藏「{recipe_name}」！')
        return True


def handle_recipe_action(recipe, prefs, mode="full"):
    print()
    is_fav = recipe["name"] in prefs["favorites"]
    fav_label = "⭐ 已收藏" if is_fav else "☆ 收藏"
    fav_action = "取消收藏" if is_fav else "收藏"

    print(f"  📌 操作选项：")
    print(f"    1. {fav_action}")
    print(f"    2. 切换模式（当前：{'极简' if mode == 'quick' else '完整'}）")
    print(f"    0. 返回")

    action = input("\n  输入选项编号：").strip()

    if action == "1":
        toggle_favorite(recipe["name"], prefs)
    elif action == "2":
        new_mode = "quick" if mode == "full" else "full"
        return new_mode, True
    return mode, False


def demand_by_category(prefs, mode):
    print("\n" + "─" * 40)
    print("  📂 按品类选择")
    for k, v in CATEGORIES.items():
        print(f"    {k}. {v['name']}")
    print("    0. 返回")

    cat_choice = input("\n  选择品类：").strip()
    if cat_choice == "0":
        return mode

    if cat_choice in CATEGORIES:
        cat_key = CATEGORIES[cat_choice]["key"]
        results = filter_recipes(category=cat_key, prefs=prefs)
        recipe = display_recipe_list(results, mode, prefs, f"{CATEGORIES[cat_choice]['name']}菜谱")

        if recipe:
            print()
            if mode == "full":
                print(display_recipe_full(recipe, prefs))
            else:
                print(display_recipe_quick(recipe, prefs))

            new_mode, switched = handle_recipe_action(recipe, prefs, mode)
            if switched:
                mode = new_mode

    input("\n  按回车键返回...")
    return mode


def demand_by_ingredient(prefs, mode):
    print("\n" + "─" * 40)
    print("  🥕 按食材匹配")

    if prefs.get("common_ingredients"):
        print(f"  📋 常用食材：{'、'.join(prefs['common_ingredients'])}")

    user_input = input("  输入你有的食材（用逗号分隔）：").strip()
    if not user_input:
        print("  没有输入食材～")
        input("\n  按回车键返回...")
        return mode

    ing_list = [i.strip() for i in user_input.replace("，", ",").split(",") if i.strip()]
    for ing in ing_list:
        if ing not in prefs.get("common_ingredients", []):
            prefs.setdefault("common_ingredients", []).insert(0, ing)
            if len(prefs["common_ingredients"]) > 10:
                prefs["common_ingredients"] = prefs["common_ingredients"][:10]
            save_prefs(prefs)

    results = filter_recipes(ingredients=user_input, prefs=prefs)
    recipe = display_recipe_list(results, mode, prefs, f"食材匹配（{user_input}）")

    if recipe:
        print()
        if mode == "full":
            print(display_recipe_full(recipe, prefs))
        else:
            print(display_recipe_quick(recipe, prefs))

        new_mode, switched = handle_recipe_action(recipe, prefs, mode)
        if switched:
            mode = new_mode

    input("\n  按回车键返回...")
    return mode


def demand_by_goal(prefs, mode):
    print("\n" + "─" * 40)
    print("  🎯 按目标选择")
    for k, v in GOALS.items():
        print(f"    {k}. {v['name']}（{v['desc']}）")
    print("    0. 返回")

    goal_choice = input("\n  选择目标：").strip()
    if goal_choice == "0":
        return mode

    if goal_choice in GOALS:
        goal_key = GOALS[goal_choice]["key"]
        results = filter_by_goal(RECIPES, goal_key)
        results = [r for r in results if not check_allergy(r, prefs)]

        sub_choice = input("\n  进一步筛选场景？1:通勤便携 2:宿舍无厨具 3:减脂餐 0:跳过：").strip()
        if sub_choice == "1":
            results = [r for r in results if "通勤便携" in r["sub_categories"]]
        elif sub_choice == "2":
            results = [r for r in results if "宿舍无厨具" in r["sub_categories"]]
        elif sub_choice == "3":
            results = [r for r in results if "低脂减脂餐" in r["sub_categories"]]

        recipe = display_recipe_list(results, mode, prefs, f"{GOALS[goal_choice]['name']}菜谱")

        if recipe:
            print()
            if mode == "full":
                print(display_recipe_full(recipe, prefs))
            else:
                print(display_recipe_quick(recipe, prefs))

            new_mode, switched = handle_recipe_action(recipe, prefs, mode)
            if switched:
                mode = new_mode

    input("\n  按回车键返回...")
    return mode


def manage_prefs(prefs):
    while True:
        print("\n" + "─" * 40)
        print("  ⚙️ 偏好设置")
        print(f"    1. 🍽 忌口食材：{'、'.join(prefs.get('disliked_ingredients', [])) or '未设置'}")
        print(f"    2. ⚠️ 过敏食材：{'、'.join(prefs.get('allergies', [])) or '未设置'}")
        print(f"    3. ⭐ 收藏记录：{len(prefs.get('favorites', []))} 道")
        print(f"    4. 🥕 常用食材：{'、'.join(prefs.get('common_ingredients', [])) or '未设置'}")
        print("    0. 返回")

        choice = input("\n  选择设置项：").strip()

        if choice == "0":
            break
        elif choice == "1":
            print("\n  当前忌口：" + "、".join(prefs.get('disliked_ingredients', [])))
            print("  输入新增忌口食材（回车跳过，多个用逗号分隔）：")
            new_dislikes = input("  ").strip()
            if new_dislikes:
                for d in new_dislikes.replace("，", ",").split(","):
                    d = d.strip()
                    if d and d not in prefs.get("disliked_ingredients", []):
                        prefs.setdefault("disliked_ingredients", []).append(d)
                save_prefs(prefs)
                print(f"  ✅ 已更新忌口列表")
        elif choice == "2":
            print("\n  当前过敏：" + "、".join(prefs.get('allergies', [])))
            print("  输入新增过敏食材（回车跳过，多个用逗号分隔）：")
            new_allergies = input("  ").strip()
            if new_allergies:
                for a in new_allergies.replace("，", ",").split(","):
                    a = a.strip()
                    if a and a not in prefs.get("allergies", []):
                        prefs.setdefault("allergies", []).append(a)
                save_prefs(prefs)
                print(f"  ✅ 已更新过敏列表")
        elif choice == "3":
            favs = prefs.get("favorites", [])
            if not favs:
                print("\n  📭 收藏夹是空的～")
            else:
                print("\n  ⭐ 我的收藏：")
                for i, name in enumerate(favs, 1):
                    print(f"    {i}. {name}")
                del_choice = input("\n  输入编号删除（回车跳过）：").strip()
                if del_choice.isdigit() and 1 <= int(del_choice) <= len(favs):
                    removed = favs.pop(int(del_choice) - 1)
                    save_prefs(prefs)
                    print(f"  🗑 已移除「{removed}」")
        elif choice == "4":
            print("\n  当前常用：" + "、".join(prefs.get('common_ingredients', [])))
            print("  输入更新常用食材（回车跳过）：")
            new_common = input("  ").strip()
            if new_common:
                prefs["common_ingredients"] = [i.strip() for i in new_common.replace("，", ",").split(",") if i.strip()][:10]
                save_prefs(prefs)
                print(f"  ✅ 已更新常用食材")


def random_recommend(prefs, mode):
    results = filter_recipes(prefs=prefs)
    if not results:
        print("\n  😅 没有合适的菜谱～")
        return mode

    recipe = random.choice(results)
    print("\n  🎲 今日随机推荐！")

    if mode == "full":
        print(display_recipe_full(recipe, prefs))
    else:
        print(display_recipe_quick(recipe, prefs))

    new_mode, switched = handle_recipe_action(recipe, prefs, mode)
    if switched:
        mode = new_mode

    input("\n  按回车键返回...")
    return mode


def main():
    prefs = load_prefs()
    mode = "full"

    while True:
        print("\n" + "=" * 50)
        print(f"  {get_greeting()}")
        print("=" * 50)

        fav_count = len(prefs.get("favorites", []))
        mode_label = "📖 完整" if mode == "full" else "⚡ 极简"

        print(f"\n  📊 今日推荐模式：{mode_label}")
        if fav_count > 0:
            print(f"  ⭐ 收藏了 {fav_count} 道菜")
        print()

        print("  请选择需求类型：")
        for k, v in DEMAND_TYPES.items():
            print(f"    {k}. {v['name']} {v['desc']}")
        print()

        print("  ── 其他功能 ──")
        print("    4. 🎲 随机推荐")
        print("    5. ⚙️ 偏好设置")
        print("    6. 📖 切换模式")
        print("    0. 退出")
        print()

        choice = input("  请输入选项：").strip()

        if choice == "0":
            period = get_time_period()
            if period == "morning":
                print("\n  ☀️ 祝你今天吃得开心，元气满满！")
            elif period == "noon":
                print("\n  🌤 午餐愉快，下午继续加油！")
            else:
                print("\n  🌙 晚安，好好休息～明天继续好好吃饭！")
            break

        elif choice == "1":
            mode = demand_by_category(prefs, mode)

        elif choice == "2":
            mode = demand_by_ingredient(prefs, mode)

        elif choice == "3":
            mode = demand_by_goal(prefs, mode)

        elif choice == "4":
            mode = random_recommend(prefs, mode)

        elif choice == "5":
            manage_prefs(prefs)

        elif choice == "6":
            mode = "quick" if mode == "full" else "full"
            print(f"\n  已切换为{'⚡ 极简速览模式' if mode == 'quick' else '📖 完整详细模式'}")

        else:
            print("\n  请输入有效选项～")


if __name__ == "__main__":
    main()
