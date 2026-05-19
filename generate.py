#!/usr/bin/env python3
"""
ksp-url-redirect 用 HTMLファイル一括生成スクリプト
使い方: このファイルを ~/ksp-url-redirect/ に置いて python3 generate.py を実行
"""
import os

entries = [
    ("yusei_sugai_j", "須貝 優成", "https://docs.google.com/spreadsheets/d/1-wzHT1q9aTmfSv44wAiz5BcSAB34ECwYHMOyop14ng0/edit?gid=645461266#gid=645461266"),
    ("souta_kimura_j", "木村 蒼汰", "https://docs.google.com/spreadsheets/d/1HiJ62Tr_2ce0bPPbx0lfk24UOsA9wx_Bt-_tWFk23Qw/edit?gid=645461266#gid=645461266"),
    ("kuto_sirai_j", "白井 空翔", "https://docs.google.com/spreadsheets/d/1S2W71w5JV5E7TAoSXUWzlKYzWz8Jn6eDq-lMPPlqm64/edit?gid=645461266#gid=645461266"),
    ("saiga_siga_j", "志賀 冴駕", "https://docs.google.com/spreadsheets/d/1SQC73ejvuPaqJ9XptFacRy7qPffGYSDB4vbcnWQmtQQ/edit?gid=645461266#gid=645461266"),
    ("kiiti_tutsumi_j", "堤 喜一", "https://docs.google.com/spreadsheets/d/1ddRs517OeJJ_YQ7wiAB-QsR8b9ANUKLLp1z1sTfxces/edit?gid=645461266#gid=645461266"),
    ("ibuki_katou_j", "加藤 命絆", "https://docs.google.com/spreadsheets/d/1shKWQXeQjz8WsnYa_vnOkEn44g4i-SetrkHS-htrDNM/edit?gid=645461266#gid=645461266"),
    ("rentarou_hirayama_j", "平山 蓮太郎", "https://docs.google.com/spreadsheets/d/1TGDmS9nZEme8crdRd46AwDlshtgcPyPozVB0vZeorrE/edit?gid=645461266#gid=645461266"),
    ("rui_otaki_j", "大滝 琉偉", "https://docs.google.com/spreadsheets/d/17Xz5JnuebOcDejvLggWw8Edj9N7e2uPqKZST4_sKnD8/edit?gid=645461266#gid=645461266"),
    ("gaku_satou_j", "佐藤 岳", "https://docs.google.com/spreadsheets/d/1GhpEWBPFZdEWIAoTE1FXGmRpBOWtQaHTiXcvWiXFgDI/edit?gid=645461266#gid=645461266"),
    ("enisi_katou_j", "加藤 縁", "https://docs.google.com/spreadsheets/d/1Ztycvl0eznvOpMVqmkot8F5d9Lfd-QF8YhAVGNH3PJw/edit?gid=645461266#gid=645461266"),
    ("yusei_matsumoto_j", "松本 悠晴", "https://docs.google.com/spreadsheets/d/1mrvvn10PnLhniCiGCyK_k0v9zMCRe5W_Zzx_ROKaeTw/edit?gid=645461266#gid=645461266"),
    ("futo_tonsyo_j", "頓所 楓斗", "https://docs.google.com/spreadsheets/d/1z5Oad99f1JKRHs1k6GSWz5Utd8yp3mMXBgEtEZnEFuE/edit?gid=645461266#gid=645461266"),
    ("rai_satou_j", "佐藤 萊", "https://docs.google.com/spreadsheets/d/1bFCwARvoZ5UhMvgzCDq2wWw1B5mENqfcPj_k5GJBYbE/edit?gid=645461266#gid=645461266"),
    ("ryo_satou_j", "佐藤 遼", "https://docs.google.com/spreadsheets/d/1S1FRpgnMSxCzK6MEEdDQ8B-bs1E0bDEjtJW4lTVwKHo/edit?gid=645461266#gid=645461266"),
    ("koto_satou_j", "佐藤 寿乙", "https://docs.google.com/spreadsheets/d/13ZITz83USaG0OM9qHYF23giSDcw2vYmbas4MhpRRAXA/edit?gid=645461266#gid=645461266"),
    ("masaki_kenmoti_j", "剣持 優樹", "https://docs.google.com/spreadsheets/d/18ZbTFY5bVoJ5ng8ofPHpz-fCh3iKA2FGi_A0gwws62M/edit?gid=645461266#gid=645461266"),
    ("ren_itou_j", "伊藤 蓮", "https://docs.google.com/spreadsheets/d/1vOGZDXWLMnp6-Z8jDu7dyTDiT4BBhaJpUoUyLglka2U/edit?gid=645461266#gid=645461266"),
    ("touma_kosinaka_j", "越中 斗麻", "https://docs.google.com/spreadsheets/d/1-JQyHLd41f8RUHiXkny838bYhJ1YHfrlzekG2vyGvyI/edit?gid=645461266#gid=645461266"),
    ("rino_inoue_j", "井上 莉乃", "https://docs.google.com/spreadsheets/d/1lVLyust2inRnOdM3JfpVP-4bE24N12WxZGx4aXbbaLs/edit?gid=645461266#gid=645461266"),
    ("syouma_yagi_j", "八木 翔慎", "https://docs.google.com/spreadsheets/d/1h0sVh-YkaJIJjKJpw97bg2sffhDrZm_FNsHecHYzt1g/edit?gid=645461266#gid=645461266"),
    ("soutarou_hasegawa_j", "長谷川 颯太朗", "https://docs.google.com/spreadsheets/d/1qpwG_bz7r8evGloUJWKnIp65BypGOeD95dn6ECAzAho/edit?gid=645461266#gid=645461266"),
    ("rikuto_mibo_j", "三母 莉空斗", "https://docs.google.com/spreadsheets/d/1SWxIB-lTAsiF0Zt6iKkcJgND5gTIgmod9RIex3fpnK0/edit?gid=645461266#gid=645461266"),
    ("hikaru_kimura_j", "木村 光", "https://docs.google.com/spreadsheets/d/1VQC6621AkOtKE8x1yzcmzCUmJTxD5kqZx97rflXFSEw/edit?gid=645461266#gid=645461266"),
    ("ryusyou_ahiko_j", "阿彦 龍昇", "https://docs.google.com/spreadsheets/d/1ndyQDIv4wKqBEUssOC0-2y68aAEjXokeJvKjO3EDG0c/edit?gid=926763381#gid=926763381"),
    ("yusei_sugai_y", "須貝 優成", "https://docs.google.com/spreadsheets/d/1H--2dghzekZNJHoi-G3hr37BAu2CuMwj4xjArKmN1vc/edit?gid=443745982#gid=443745982"),
    ("souta_kimura_y", "木村 蒼汰", "https://docs.google.com/spreadsheets/d/161t0N15jtnOd3-dzgyEIOmovSXSTz-7I_D9SH8Qob1I/edit?gid=443745982#gid=443745982"),
    ("kuto_sirai_y", "白井 空翔", "https://docs.google.com/spreadsheets/d/1FThAEa3aBPke76UXbmPICps62-IrkWScdSDA2Lfp_Xo/edit?gid=443745982#gid=443745982"),
    ("saiga_siga_y", "志賀 冴駕", "https://docs.google.com/spreadsheets/d/1HuwQPYy4j4IAbHIf6sHLAQIEoWf7sZ1nePF2CT5ySQs/edit?gid=443745982#gid=443745982"),
    ("kiiti_tutsumi_y", "堤 喜一", "https://docs.google.com/spreadsheets/d/13vnAl1ewEeiwotDCX5bm2DaUEhCFNRF9uPfoyK93u1k/edit?gid=443745982#gid=443745982"),
    ("ibuki_katou_y", "加藤 命絆", "https://docs.google.com/spreadsheets/d/17t8VNuTVR_5qUJAkM5kEuxI2LjJdeMyxvAcN5okbOgY/edit?gid=443745982#gid=443745982"),
    ("rentarou_hirayama_y", "平山 蓮太郎", "https://docs.google.com/spreadsheets/d/1B0l-D2Or09vqg3lFn22dbAzo0sI0ZCTyggh-rHUhIVo/edit?gid=443745982#gid=443745982"),
    ("rui_otaki_y", "大滝 琉偉", "https://docs.google.com/spreadsheets/d/1qRdd09jK81Rf6CXEPM9OOYQfh9oQK-m1pQK-5m_iwrQ/edit?gid=443745982#gid=443745982"),
    ("gaku_satou_y", "佐藤 岳", "https://docs.google.com/spreadsheets/d/1oeLlyR92nOn4hDaD81QHMVi9GTTm4POohx1utL72c3Y/edit?gid=443745982#gid=443745982"),
    ("enisi_katou_y", "加藤 縁", "https://docs.google.com/spreadsheets/d/1tv63g36tw85IyUf6jM4uM0-fIUB8Kjz5xxkqhwZIJZs/edit?gid=443745982#gid=443745982"),
    ("yusei_matsumoto_y", "松本 悠晴", "https://docs.google.com/spreadsheets/d/1SzZNkd9xmWCBzd-iA2toUktvHDY_vfF-24qewW-aglU/edit?gid=443745982#gid=443745982"),
    ("futo_tonsyo_y", "頓所 楓斗", "https://docs.google.com/spreadsheets/d/11Y15EQFQxlO7Gk0Pf-VoOYB6Pk7BTLQf0fRBRVimP-c/edit?gid=443745982#gid=443745982"),
    ("rai_satou_y", "佐藤 萊", "https://docs.google.com/spreadsheets/d/1T648E-fRF0_rj8VtotKEvv7n9crg60-5RKLa3zq9HF4/edit?gid=443745982#gid=443745982"),
    ("ryo_satou_y", "佐藤 遼", "https://docs.google.com/spreadsheets/d/1DAohe6Pky3PgBB_9hXs18KbDx0-ZSfNHaX3fjJnoqfw/edit?gid=443745982#gid=443745982"),
    ("koto_satou_y", "佐藤 寿乙", "https://docs.google.com/spreadsheets/d/1-Eoc-9yp9cr8Gb8i2meTGw45AJixIgcwHUZ17Iz1NHA/edit?gid=443745982#gid=443745982"),
    ("masaki_kenmoti_y", "剣持 優樹", "https://docs.google.com/spreadsheets/d/1V9ov-iFXMaGOjjHwh5cw4SpyvWD_ACt-VQf1mrnpHzM/edit?gid=443745982#gid=443745982"),
    ("ren_itou_y", "伊藤 蓮", "https://docs.google.com/spreadsheets/d/1-wEDu8Z_7LxGkFXxJHdUQY8284ME4MGZssmFmEvPEVI/edit?gid=1236064095#gid=1236064095"),
    ("touma_kosinaka_y", "越中 斗麻", "https://docs.google.com/spreadsheets/d/1qYzxx2Pz6y3WoZUU3IJcx1281XyEOVmUGSrmkrQgKUQ/edit?gid=1236064095#gid=1236064095"),
    ("rino_inoue_y", "井上 莉乃", "https://docs.google.com/spreadsheets/d/1IzYel1MKKJDf0fTmBWNC6LxkmNNZdZIVexpnAxqWB-o/edit?gid=392572476#gid=392572476"),
    ("syouma_yagi_y", "八木 翔慎", "https://docs.google.com/spreadsheets/d/1wSGebGbUTsznPKvl-WxO7t24wi6khcUgqWFXKaok4mk/edit?gid=954401899#gid=954401899"),
    ("soutarou_hasegawa_y", "長谷川 颯太朗", "https://docs.google.com/spreadsheets/d/1DoJ7CirYgfyypsU3w5YH8fh-r5kvZF8d9slyQqU4Ydc/edit?gid=954401899#gid=954401899"),
    ("rikuto_mibo_y", "三母 莉空斗", "https://docs.google.com/spreadsheets/d/1IjSynSl_oRJarKgXoWpvpI_rfY7ZfGSgQj1is6gheGk/edit?gid=954401899#gid=954401899"),
    ("hikaru_kimura_y", "木村 光", "https://docs.google.com/spreadsheets/d/1mjd8ut1-NBGNBj6PH37TLoK-0MUnVoabINhuDhE_unY/edit?gid=954401899#gid=954401899"),
    ("ryusyou_ahiko_y", "阿彦 龍昇", "https://docs.google.com/spreadsheets/d/1XOn6V5q97QgPIR-99tuekFJ-pOZGqOldPLhdl2pxxB8/edit?gid=297477625#gid=297477625"),
    ("jeido_hasegawa_j", "長谷川 じぇいど", "https://docs.google.com/spreadsheets/d/15-ETMg5ou7a4eTUO0uKLvqUsw8nuGEynSl8oWntWD-A/edit"),
    ("hikaru_tomita_j", "冨田 光", "https://docs.google.com/spreadsheets/d/1qyHohycJZW0goax4qVlNIo-vR2ROSZ-3NzL0jhrxLww/edit?usp=drive_link"),
    ("rai_sato_j", "佐藤 萊", "https://docs.google.com/spreadsheets/d/1mMfGwHmC41t4qAPBmDPZ733MVEVEBjg-ktwZs2eIcuQ/edit?usp=drive_link"),
    ("sotaro_hasegawa_j", "長谷川 颯太朗", "https://docs.google.com/spreadsheets/d/1Rs-5F2MNU2YIFzDSTC7R7-7CHtZ3BCaqyBR8k3w2574/edit?usp=drive_link"),
    ("masato_enndo_j", "遠藤 雅士", "https://docs.google.com/spreadsheets/d/1fyaG5iAUVfEBCs-rMLKGzmqrAb-4qNdRNBEbqExoFwo/edit?usp=drive_link"),
    ("oribiasimon_j", "オリビアシモン", "https://docs.google.com/spreadsheets/d/1BQvHFe-3MuvPRTBRU4VTBOFqfc5tQyEfsM2ne6Knrqk/edit?usp=drive_link"),
    ("masaki_oota_j", "大田 雅貴", "https://docs.google.com/spreadsheets/d/1h3KD3wf-nat_GpLfxPKU4QuN_MBx72zzfSMd5Aas2yI/edit?usp=drive_link"),
    ("mituki_oota_j", "大田 深月", "https://docs.google.com/spreadsheets/d/18h8IpHOrxRlaIWQKJRRrMtsh2Um9FwPUnAJB8q8DK08/edit?usp=drive_link"),
    ("iori_goto_j", "後藤 伊織", "https://docs.google.com/spreadsheets/d/1LLz3mHGSSQrkFI6qH49l3Dg2WF3gNqNaO5JNGcFDWX0/edit?usp=drive_link"),
    ("nana_yokoyama_j", "横山 叶愛", "https://docs.google.com/spreadsheets/d/1X4Qubn_yKQKfFR1iaS3zFTW84yqW09_zlRZfYb487Wo/edit?usp=drive_link"),
    ("yusinn_ahnano_j", "花野 優心", "https://docs.google.com/spreadsheets/d/1YPO_E1dJfXaggKebv60ZluR1S6POBEwyEbEPEN6gLZk/edit?usp=drive_link"),
    ("haruma_oomura_j", "大村 陽雅", "https://docs.google.com/spreadsheets/d/1SmbvLKF3LiF8aVhzckvmtQlwWWl_wh0_Z0Gn8Ifsluw/edit?usp=drive_link"),
    ("rikeino_j", "リ ケイノ", "https://docs.google.com/spreadsheets/d/1xQijQpzWBT6yGRMKD_Fb-ifPp5W4JqZqC5kX4iktW8s/edit?usp=drive_link"),
    ("rintaro_honnma_j", "本間 稟大郎", "https://docs.google.com/spreadsheets/d/1LPJ1bZYPmpL1IG2sHnDOQzDztdgeIHLavPBqT1SJR5Q/edit?usp=drive_link"),
    ("yuto_saito_j", "齋藤 悠斗", "https://docs.google.com/spreadsheets/d/161oHX9Ix9-wV4xToQUZV27bdludj-uNla4fLw-I1oWE/edit?usp=drive_link"),
    ("minato_koike_j", "小池 湊斗", "https://docs.google.com/spreadsheets/d/1kMFrLyJpubMcgMH1HEJ-C579WWXXIysR7gvJHbdD8Aw/edit?usp=drive_link"),
    ("reina_sato_j", "佐藤 玲奈", "https://docs.google.com/spreadsheets/d/1R3j2_JwDP-DFXBKO6ahdNT5K-bxb2j9L6nNMhoOtKbU/edit?usp=drive_link"),
    ("mahiro_itagaki_j", "板垣 真裕", "https://docs.google.com/spreadsheets/d/1m619vARNIn5dYvZksjQcdD-4t8FNamaWvze8acVlkMM/edit?usp=drive_link"),
    ("aoi_tokita_j", "時田 蒼", "https://docs.google.com/spreadsheets/d/1V8967liMpMUW_rqx5rkeTGQsiUPLw-dc7uS9TtVezCI/edit?usp=drive_link"),
    ("haru_komata_j", "小俣 晴", "https://docs.google.com/spreadsheets/d/1ESYfsIo7P-GrQ0cO1fg_a5teCBH9U9Kl0kJQgPKfO1s/edit?usp=drive_link"),
    ("jeido_hasegawa_y", "長谷川 じぇいど", "https://docs.google.com/spreadsheets/d/17oUzcL1z8mSI0Qc3HkOCvMK_W6zAn5LGxji5KsgFqgk/edit?usp=drive_link"),
    ("hikaru_tomita_y", "冨田 光", "https://docs.google.com/spreadsheets/d/1jgYwIXCqpvb5vLcOFKSr2v2Sfgoqg0MoKmT-nrmKj6w/edit?usp=drive_link"),
    ("rai_sato_y", "佐藤 萊", "https://docs.google.com/spreadsheets/d/1Z0A0P2M2au19-oECjgYGeq6Z5XpHas_OsQHbh8gToxo/edit?usp=drive_link"),
    ("sotaro_hasegawa_y", "長谷川 颯太朗", "https://docs.google.com/spreadsheets/d/1xNxl9sPAu4eN04-N0dbgejgxfzMOQz7tS4ExSCSd6dI/edit?usp=drive_link"),
    ("masato_enndo_y", "遠藤 雅士", "https://docs.google.com/spreadsheets/d/1F0zHTRbCZAOEkSULMkKOwIKMrTUKUBg-ac2j9pf5j8U/edit?usp=drive_link"),
    ("oribiasimon_y", "オリビアシモン", "https://docs.google.com/spreadsheets/d/16z1sYFMjTvqoZHxkLPRbcAsuwOLmrhDivNbB3hhBZms/edit?usp=drive_link"),
    ("masaki_oota_y", "大田 雅貴", "https://docs.google.com/spreadsheets/d/1n2KAMeFitf6RxxtlB8QVOPWuX798W2bkfieRSshNT8A/edit?usp=drive_link"),
    ("mituki_oota_y", "大田 深月", "https://docs.google.com/spreadsheets/d/1pnvwUR9euDT0NsBcAGjxvT-Blktlc-ICMGziupqekBw/edit?usp=drive_link"),
    ("iori_goto_y", "後藤 伊織", "https://docs.google.com/spreadsheets/d/1Jou2Nt0omGQkdormpt6Rxz6C184StSAUK95GEeH8RcE/edit?usp=drive_link"),
    ("nana_yokoyama_y", "横山 叶愛", "https://docs.google.com/spreadsheets/d/1tBsEhHspBmmF-LeKiED8267Q8q4o8IeBypv27de_RPc/edit?usp=drive_link"),
    ("yusinn_ahnano_y", "花野 優心", "https://docs.google.com/spreadsheets/d/1ByhNKPueF_WvSCyo19lhp0tv5gIVorOnQUUezjBJ6mo/edit?usp=drive_link"),
    ("haruma_oomura_y", "大村 陽雅", "https://docs.google.com/spreadsheets/d/1PX5KD4Zt3Gwk2_KBPvLdm5kaNGza07ykPnTZw7jaqcU/edit?usp=drive_link"),
    ("rikeino_y", "リ ケイノ", "https://docs.google.com/spreadsheets/d/1XycEkxhLy_dXPgzCObJxGVbzpZBsf8b_GWxW9if72u8/edit?usp=drive_link"),
    ("rintaro_honnma_y", "本間 稟大郎", "https://docs.google.com/spreadsheets/d/1KBErRG5ZFu0Bnyc2sP1XHMMWBxf0QrsTSsBAzcaCIsU/edit?usp=drive_link"),
    ("yuto_saito_y", "齋藤 悠斗", "https://docs.google.com/spreadsheets/d/1dEQera5ukLGvz7XYfIKynEokFNvPBCeYO3ADj4L98q8/edit?usp=drive_link"),
    ("minato_koike_y", "小池 湊斗", "https://docs.google.com/spreadsheets/d/1HsNF7uSjRIDeHLm2laJhMAbsuA9L8dEk8kdxckg_k2Q/edit?usp=drive_link"),
    ("reina_sato_y", "佐藤 玲奈", "https://docs.google.com/spreadsheets/d/1Qq1PaboQclmpObUVopCexY2CW7MDUkZFoBT3_ozHtfs/edit?usp=drive_link"),
    ("mahiro_itagaki_y", "板垣 真裕", "https://docs.google.com/spreadsheets/d/1VpbMilSQf5w7Qvp9W8EH_HI-GownLkz7DFjsqVaBbo8/edit?usp=drive_link"),
    ("aoi_tokita_y", "時田 蒼", "https://docs.google.com/spreadsheets/d/1m_Bf080fcmeFiP-l8yXHiUlGafspf7In5grrsYGqqaM/edit?usp=drive_link"),
    ("haru_komata_y", "小俣 晴", "https://docs.google.com/spreadsheets/d/17Ia708nknP2nZKToJi3sifwLkA9dPHGdA3i7UUVR5ec/edit?usp=drive_link"),
]

TEMPLATE = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0;url={url}">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>実績記録表 - {name}</title>
</head>
<body style="font-family:sans-serif;text-align:center;padding:40px 20px;color:#333;background:#f8f9fa;margin:0">
<div style="background:#fff;border-radius:12px;padding:32px 24px;max-width:400px;margin:0 auto;box-shadow:0 2px 8px rgba(0,0,0,0.1)">
<div style="font-size:18px;margin-bottom:16px">{name}さんの実績記録表を開いています...</div>
<p>自動的に移動しない場合は下のボタンをタップしてください。</p>
<a href="{url}" style="display:inline-block;background:#1a73e8;color:#fff;text-decoration:none;padding:14px 32px;border-radius:8px;font-size:16px;font-weight:bold">実績記録表を開く</a>
</div>
</body>
</html>"""

count = 0
for code, name, url in entries:
    os.makedirs(code, exist_ok=True)
    with open(os.path.join(code, "index.html"), "w", encoding="utf-8") as f:
        f.write(TEMPLATE.format(name=name, url=url))
    count += 1

print(f"✅ {count}件のリダイレクトファイルを生成しました")
