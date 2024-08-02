import requests
import json
import time
from datetime import timedelta
wh_80 = 'https://discord.com/api/webhooks/1204252040210026536/3sR48gVzmoaOXC6vplJ6JAEXn8e5TqM0sGgUxexL-n_nVU82mMWPtWmEcFgeJBnENXbs'
wh_60 = 'https://discord.com/api/webhooks/1204252084942405685/GMQfAfuOJ2McvErJ1Gt6zOYXmAb3e77nuiIkMvkayR4QjyNp1jAP8fT8MA0XNX7OkSaT'
wh_40 = 'https://discord.com/api/webhooks/1204252131977330688/fT7xJBuiDmS2MuATX5b8CEDJJ9z_Ks4WxnwTe2jkkqx2x0K9EZfxKsRY19w0sHSyhU4R'
wh_0 = 'https://discord.com/api/webhooks/1204252179691606036/QyueTUhvDRc3h92MB9Y3AxsyIV_gLWne-I7N1zPTUF5BUQifIyW9kVV_qTMuEtCRI1Q8'

cookies = {
    'aat1': 'off-p0',
    'ga': 'g1',
    'gb': 'g1',
    'gc': 'g2',
    'gr': 'g1',
    'mdLogger': 'false',
    'kampyle_userid': 'd5f5-cee3-19ad-c07e-93dc-4048-d72f-784d',
    'QuantumMetricUserID': '649c646d3e8229dbfc851ded764fa909',
    'aat2': 'on',
    'aat4': 'off-p2',
    'acexp': 'on',
    'acct_sso_mig': 'on',
    'adh_ps_pickup': 'on',
    'adh_ps_refill': 'on',
    'acct_cgsb': 'on',
    'cdt_ds': 'on',
    'acct_untieRx': 'off',
    'acc_ca_newreg': 'on',
    'bfp_new': 'on',
    'buynow': 'off',
    'cp_new_dash': 'off',
    'sab_displayads': 'on',
    'dashboard_v1': 'on',
    'disable-app-dynamics': 'on',
    'dpp_cdc': 'off',
    'dpp_drug_dir': 'off',
    'dpp_sft': 'off',
    'drginf': 'on',
    'ecfl': 'on',
    'easy_xfer': 'on',
    'footer_new_V1': 'on',
    'gbi_cvs_coupons': 'true',
    'gbp_api_v2': 'on',
    'mc_cloud_service': 'on',
    'mc_hl7': 'on',
    'mc_videovisit': 'on',
    'newauthflow': 'on',
    'newPDP': 'on',
    'ngsw': 'off',
    'ohexp': 'off',
    'plpui': 'on',
    'rx-pref-i90': 'on',
    'pmexp': 'off',
    'ps_i': 'off',
    'rxdanshownba': 'off',
    'rxdfixie': 'on',
    'rxd_bnr': 'on',
    'rxd_dot_bnr': 'on',
    'rxdpromo': 'on',
    'rxduan': 'on',
    'rxm_demo_hide_LN': 'off',
    'rxtiemm': 'on',
    'sft_mfr_new': 'on',
    'sftg': 'on',
    'show_exception_status': 'on',
    'slistview': 'on',
    'sub_cp_fmf': 'off',
    'switchExpAPI': 'on',
    'tphrm': 'off',
    'sd_ma': 'on',
    'mca1': 'on',
    'rbh1': 'off',
    's2c_transactionsphr': 'on',
    'mfep1': 'off',
    'imzfe': 'v1',
    'imzn': 'on',
    'rxp': 'on',
    'aat3': 'on',
    'hdnew': 'on',
    'fspe': 'p1',
    'kcpe': 'e',
    'rxe': 'i1',
    'mvpe': 'gr',
    'mcpe': 'gr',
    'mdpe': 'gr',
    'ccse': 'p1',
    'pe': 'p1',
    'acct_pe': 'p1',
    'ak_bmsc': 'CCBA05F4D0F489AE9CF749E6565EA66B~000000000000000000000000000000~YAAQBZUzuI2APOWQAQAA1bp1DBh8/XkckIN1GQc7kUgMjsUUozdGvKGQYJdskWw5jbX4RdTEl6rfSMKNCEAEWq/ipB8JJMhS66vk6OxGSZaeHHsJQ/4Wsnqw5W2QJWQdPwkTZJk7TYlJb5S6Um7SkInmtysKMgDktQEHb7yjSDwnF1wOaIGSRr1rdobXSiOHMNGqsdWd0UXoTPaF2kaxdsx1k6J/YIl2jag22++5FHFOXpbRB0yMSzIlLgK2piglp/xSoKnN0kNcWwalVxF6GktxDjQuwEnHbncsQzjZvGrvD3NpwkS0+2TgVmerTtI0FDUu3n5GarrAUNA8I6tUrEwidcHHIXKRwQ/OancnKgSA/wnk+QdRYbQWFlSzncRM6+9wnHeRog==',
    'utag_main_v_id': '018d729eaee5001f50b9dc4754b60507d001407500bd0',
    'utag_main__sn': '1',
    'utag_main__ss': '0%3Bexp-session',
    'utag_main_ses_id': '1707025018597%3Bexp-session',
    'utag_main_vapi_domain': 'cvs.com',
    'utag_main__pn': '20%3Bexp-session',
    'AMCVS_06660D1556E030D17F000101%40AdobeOrg': '1',
    's_cc': 'true',
    '_gcl_au': '1.1.1989876051.1722490926',
    'kampyleUserSession': '1722490925780',
    'kampyleUserSessionsCount': '5',
    'kampyleUserPercentile': '65.91362588066244',
    '_fbp': 'fb.1.1722490925836.28472638472144199',
    '_uetsid': 'c92423d04fc811ef99020ba518baa091',
    '_uetvid': '6b15fd60c31f11ee83db7d3f874adaa1',
    'visid_incap_2490223': 'pjAK3XDWQlOV8Jz9lBeDWTEgq2YAAAAAQUIPAAAAAACSNgWk5ZsPx9JMHeOOnlmy',
    'incap_ses_1443_2490223': '0NsaYsaSQCsF/vx19JAGFDEgq2YAAAAAqzuf7jdiAeKeA3lvCjf0RQ==',
    'incap_ses_8215_2490223': 'vY7wOfoCBD6T5baRFYsBcjAgq2YAAAAA085d+zOiLAMJkPtjlG1D3w==',
    'token_type': 'Bearer',
    'access_token': 'eyJraWQiOiJRR0hnM0NTeUVhaGdrZ1RpTVZ3RHhrRy1yT0RPSlpGamI2NzBUOWxXSXBzIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJ4LWFwcC1uYW1lIjoidGVhbWFwcF9hcHBfZ3Vlc3RfcmV0YWlsX29yZGVyc18xNjY0OTM0OTIwIiwic3ViIjoidGVhbWFwcF9hcHBfZ3Vlc3RfcmV0YWlsX29yZGVyc18xNjY0OTM0OTIwIiwiaXNzIjoiaHR0cHM6XC9cL2FwaS5jdnNoZWFsdGguY29tXC9vYXV0aFwvdjEiLCJ4LWdyaWQiOiJycnQtMTAxNDMzNjUwMjMzMTY3MDQxOS1jLWdlYTEtNjIwMS0xNjMwMzEwMC0yIiwieC1jYWNoZS1wcmVzZW50IjpmYWxzZSwieC1mbG93LXR5cGUiOiJndWVzdCIsImF1ZCI6Imd1ZXN0LWZsb3ciLCJ4LWNsaWVudC1pZCI6IjZUaWlkb1JqcFFHM3VTaktVMzNsZ3E5N01BdVZCdHB6Iiwic2NvcGUiOiJvcGVuaWQiLCJ4LWNsaWVudC1maW5nZXJwcmludC1pZCI6ImV5SmpiR2xsYm5SRGFHRnlZV04wWlhKcGMzUnBZM01pT25zaVluSnZkM05sY2s1aGJXVWlPaUpGWkdkbElpd2lZbkp2ZDNObGNrMWhhbTl5Vm1WeWMybHZiaUk2SWpFeU55SXNJbUp5YjNkelpYSkdkV3hzVm1WeWMybHZiaUk2SWpFeU55NHdMakF1TUNJc0ltOXdaWEpoZEdsdVoxTjVjM1JsYlNJNklsZHBibVJ2ZDNNaUxDSnZjMVpsY25OcGIyNGlPaUl4TUNJc0ltTmhiblpoYzFCeWFXNTBJam9pTVdSak5ETTFaR1V4WVRCbE5HUTFPR0l5TUdFNU5ETmtNakZtTTJFellqVWlMQ0pqYUdGdWJtVnNJam9pVjBWQ0lpd2lkV0VpT2lKTmIzcHBiR3hoTHpVdU1DQW9WMmx1Wkc5M2N5Qk9WQ0F4TUM0d095QlhhVzQyTkRzZ2VEWTBLU0JCY0hCc1pWZGxZa3RwZEM4MU16Y3VNellnS0V0SVZFMU1MQ0JzYVd0bElFZGxZMnR2S1NCRGFISnZiV1V2TVRJM0xqQXVNQzR3SUZOaFptRnlhUzgxTXpjdU16WWdSV1JuTHpFeU55NHdMakF1TUNJc0ltTmhiblpoYzFCeWFXNTBYMjlzWkNJNklqazJOemM1T0RsaE16RXlNRGMzTm1OaE16TTBOR1psTW1ReFlXVmhaR0kzTldZeVkyUXhPR1kxTWpZME5HRTNZV0poTUdFek56a3lZamhtTXpVNU1XRWlMQ0ppYm1Od0lqb2lUV2xqY205emIyWjBJRVZrWjJVaUxDSmliWFpqY0NJNklqRXlOeUlzSW1KMlkzQWlPaUl4TWpjdU1DNHdMakFpTENKdmMyTndJam9pVjJsdVpHOTNjeUlzSW05emRtTndJam9pTVRBaWZYMD0iLCJ4LWxvYiI6Imd1ZXN0LWZsb3ciLCJleHAiOjE3MjI0OTE4MjksImlhdCI6MTcyMjQ5MDkyOSwieC11c2VyLWNvbnRleHQtdHlwZSI6Imd1ZXN0IiwianRpIjoiMTZkOGVhYmYtOTllYi00MzIzLWFmODMtYzBlODJlYjNiZjFhIn0.FJ6OVBifao1PyVW3m1JfhAIE4evn8I6VQMF5_7Sfj8z9CS0GJhpvjVtOGF7J_FFc7Le7DL1u1pnl1ljjV8T5vAKCXJ15zoBaBk7meVLH8Aq2OpgS8x0uBvGbwCtp8hrUT5K-TwZ3Cx6LSRnvjCQkmGPBLc73qcE2xFuqbA-dOH9cykEN98mmoHf03sqsogyp8C2CdSMlB5a-TAUn4mFZEunhRz0lHwX8-XUeET_4X2Tak88tJKueEEbGqRPjVac6DBUTukB_wNB2WC1ew53MSMZMMYFartqHzs61AePQ_lh-6gs2TuvEq1_XAdjf8knrH34bv55OoqPAk0gVrArxSw',
    'fpcuid': '1dc435de1a0e4d58b20a943d21f3a3b5',
    'utag_main__st': '1722492726356%3Bexp-session',
    'utag_main__se': '116%3Bexp-session',
    'gpv_e5': 'homepage',
    'kndctr_06660D1556E030D17F000101_AdobeOrg_cluster': 'va6',
    'kndctr_06660D1556E030D17F000101_AdobeOrg_identity': 'CiY4NjMxNjMyNDA3MDk2NjgyMjg5MjE1NzQ0Mjk1NzA0MzQ5ODY5OFIQCJnp-pTXMRgBKgNWQTYwA_ABhoXX45Ay',
    'incap_ses_6520_2490223': 'ec0pNPrDjlqtIrdJjrF7WjEgq2YAAAAA7kcAjYQZhe/pIHsYQjE8TQ==',
    'incap_ses_132_2490223': 'DUtRT+1pxSoxeNbCZvXUATEgq2YAAAAAaSr0x1qbhq9r5vaDKZh2ww==',
    'QuantumMetricSessionID': 'c96289509d500db95ae0d4190f73587d',
    'QuantumMetricSessionLink': 'https://cvs.quantummetric.com/#/replay/cookie:c96289509d500db95ae0d4190f73587d?ts=1722447727-1722534127',
    'AMCV_06660D1556E030D17F000101%40AdobeOrg': '1176715910%7CMCIDTS%7C19937%7CMCMID%7C86316324070966822892157442957043498698%7CMCAAMLH-1723095725%7C7%7CMCAAMB-1723095725%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1722498125s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19944%7CvVersion%7C5.4.0',
    'nlbi_2490223_2638546': 'IdhqRPK1bB/ZbYp5QrA1IgAAAACTQF99/zRpI5T2THQVRpfU',
    'incap_ses_418_2490223': '5FjhSFssuR7KBtP/5AjNBYQgq2YAAAAALpW2R+C7ExI33iSxZfpkWQ==',
    'bab_atb': 'off2-p0',
    'RT': '"z=1&dm=cvs.com&si=2ccad6a8-d677-4147-8b43-11429f517e4c&ss=lzaumf8g&sl=1&tt=vb&bcn=%2F%2F173bf110.akstat.io%2F&ld=1dn&hd=1u9k"',
    'incap_ses_1441_2490223': 'QUahRgJ5diWDgPkr93X/E4Ygq2YAAAAA0kOmaKUmxgKqmhlBn7/CJw==',
    'incap_ses_512_2490223': 'caDcXg6scU9YoZ2GZf0aB4Ygq2YAAAAAaDxp+2j8qrQ/6UWcFqnHQQ==',
    'incap_ses_6524_2490223': 'y90LLyP4YkAANk7diOeJWoUgq2YAAAAAUd3GDr8QUqoBHM9d9psasQ==',
    'reese84': '3:X71qFK//OgNXz204GMb8ZA==:ZBwxqcDMMvv0nUY8BUT/J9itkzUoTcwkyv5rP8iko3h3hb4iqzwRRRYwnRAmwHp3Mu1AUqaDCB5/5hTw/SlKhcrOYM4bp/SYmaUWPBwOVydFTif8ckTuLNSecqDQJa7NWdQrbQfBn75nrU8oFCSb572U+zLz6qSG1eb3HFXQ2pbeENEYW53PxlKzbksUucU/sUDqARB9Py9g9pnoLvbeZTqAN8iKW6TwVgZZ+bLFaXHaDs/N2IFJXGxwq60RoPQLPhFzWZD+Vt79iAM6uBwU/2AcEEROe8/Z6Ao/b7H+fUozFul+cAws+89cXMX6gem5zYFIdHAyxRtRWk+rc78ArxevHG12hUqNjctdjSead2E0itWYVfRX6v8HYC3Vazt1z6bh2tbYnvIN07RMh8eJ+o7DzmoiOMGNFkRfeKDPRQE9uXDAMuNDi7poDgrWBG0Tf0W1DsiYZXRz+9OrI8YwwQ==:QnU/RAzcnbwUZHZ9CWGjp8Wsl89Z0ZckMdKYE6okewc=',
    '__gads': 'ID=5788eb0f427b1398:T=1707025069:RT=1722491015:S=ALNI_MZNSTvp6WcOCs9X37OSVAHJTcTx0A',
    '__gpi': 'UID=00000a0b602c4854:T=1707025069:RT=1722491015:S=ALNI_MZIQzlLcKsVtDTRyADtTNAnmSW-Zg',
    '__eoi': 'ID=cdadd611cf7b3ac2:T=1707025069:RT=1722491015:S=AA-AfjbBGU1-VBN-6efXQcRhvJ8-',
    'nlbi_2490223_2556230': 'xNwaIRyPPS7yzsoSQrA1IgAAAACbCdnxhNo7zvk/JxBNT2+9',
    '_abck': 'AF42E39BB20AC35D17DE9653A87ECBD3~0~YAAQBZUzuImTPOWQAQAADxR3DAxBnqxDaXgXVXE1dY8SwS0prrkEWb4rTrYlVaBRBhqDYaGE+ZgXkrCE+xzA2CJrKewjZV9zx3R8jTcTXv8ZWnMIGVEVM/rgUSx5yGSukDisYxM71/WCudsdTCc6YO3lgbNY/U5NNUl5gsZvfmcm12T3yHouU3Z0NEAHdi1rnX+BCgaF9KTQMnrwtS2vQNM8oGc3qDzUcfK44/7MSP9lUdhECdXMXZu05gcwZZEczKxRObhQMOqsT4+R5lRiULMmnvDm3vgHx9DsMFiWACYjFFKrnZa0jgrwS6olVuXLyMSgQZpKvHAss6gzFD6gtBlpdOikrv+f21LEoKlzPDNq/EIyN8ae6eDNUs/lFr/0HC8ltlRS/XdLyf1G0PUrWQjRXZspnSvpiGJxHH7ZsGPEz3A1nxDFwizFMwvlRytca8Ujo6TlqisqV5RYVhyJ5bmO~-1~-1~-1',
    'gpv_p10': 'www.cvs.com%2Fsearch',
    'br_breadcrumb': 'undefined',
    'category_id': 'undefined',
    '_br_uid_2': 'uid%3D9231727608296%3Av%3D15.0%3Ats%3D1707025021088%3Ahc%3D8',
    'kampyleSessionPageCounter': '2',
    'ADRUM': 's~1722491021131&r~aHR0cHMlM0ElMkYlMkZ3d3cuY3ZzLmNvbSUyRnNlYXJjaCUzRmhhc2glM0QxNDYwMzQ5NTU5',
    'akavpau_vp_www_cvs_com_crm': '1722491444~id=6bdcb127029e9c6b1972ba302e2e525a',
    'bm_sz': 'BF56D65FE763D723AF9D648C8B4280E1~YAAQBZUzuKWUPOWQAQAAGjZ3DBjiy1cFpH1lEIre2ZixJXyON3XVEOjUrW1/iHQOYc6FiYStjBlmGYK6IU29dSeQllYJpYGci3MCf2A74/tpP0JaZ8vO1p24zGtx0NnrYiuCWThnH+0adytj7AlrcjzAam6xtIZ1JOccWkna8Q8pMQbI9dXOr12FOCCSoQohlOqCvKY2K1yjCJnATHQC6de1v0YB9NJ9Cimv55NyXGvmJAcnRWanzimTh5ytrtrS0L+hAOauEW736SFI6/Lcj6P2+1XQ/GMSaedPCYcXdMTMUFehSYuYl40MhvPb9Jo/N+8F1Yfb+spBwlHgkhY+hZa439ohDHG1p70rnh/KNFi4ZULwsWmnT3r7RO9XHeFqghE3gvTtxwNGRQ5HTfeYE5hp8eh49YM1mR9FR33VQquaGg==~3420464~3290675',
    'nlbi_2490223_2354313': 'CGzMd1ojwAHRdrrPQrA1IgAAAAAcS0vKPZq8OLB+vUGnsw1e',
    'akavpau_www_cvs_com_general': '1722491445~id=639fd3059ab74bdcb72377e958a9c470',
    'nlbi_2490223_2147483392': 'J83bbQJ8ghemMjwCQrA1IgAAAADo849CSD7nUXB3dBp4qHS2',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Aug+01+2024+01%3A43%3A42+GMT-0400+(Eastern+Daylight+Time)&version=202402.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0011%3A1%2CC0012%3A1%2CC0013%3A1&AwaitingReconsent=false',
    'cto_bundle': 'bEAa1F80ck52QlFsNTQxQ1FaMktNRHZCQXZyZ2Q0Z2dVbUZoWTc2WEl6YmY4RVJscjM5bzlrWmxjOERaUjd5ajhsUUdFbCUyRnhxd2dLQVpveWo1MzZsU1V3ZWk0NFBRVUxKZzF5ZTBocXdSUE95T2thRzU0c0lud3RuODd4UUFxT3ZJQks1bTVMa1g1Q2VqME5DY2Z5Y1FmaEludyUzRCUzRA',
    'utag_main': 'v_id:01910c7700e8001f1917bc39d2b30507d002907500bd0$_sn:1$_se:19$_ss:0$_st:1722492822977$ses_id:1722491011305%3Bexp-session$_pn:2%3Bexp-session$vapi_domain:cvs.com',
    'mp_cvs_mixpanel': '%7B%22distinct_id%22%3A%20%2218d729eb2549d5-0d55b68528e3b4-4c657b58-1fa400-18d729eb2559ba%22%2C%22bc_persist_updated%22%3A%201707025019478%7D',
    'bm_sv': '3207835614E0220DE7CFA438D7F2B371~YAAQBZUzuEaVPOWQAQAAyD93DBhktvaZKm/h95SD4xhuDZjaKHH8J97PZf3yuXTPPXisctHbU2m1qp5960vwZ8RKJvviFois5yst5aydOyqUfOj+pPfGlXQrltgAExeoripIMc+6ZShPMWuYdlMXPF5Nl1l5Dymscfr5dR1yROvyhYMX/844cDuTBYKgWbyFi2VXeojf76rLBppUh6E3DNJnWV7qwuAyuzI7H21PfdXbFnZkxGiV/nk2TJsEXw==~1',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'adrum': 'isAjax:true',
    # 'cookie': 'aat1=off-p0; ga=g1; gb=g1; gc=g2; gr=g1; mdLogger=false; kampyle_userid=d5f5-cee3-19ad-c07e-93dc-4048-d72f-784d; QuantumMetricUserID=649c646d3e8229dbfc851ded764fa909; aat2=on; aat4=off-p2; acexp=on; acct_sso_mig=on; adh_ps_pickup=on; adh_ps_refill=on; acct_cgsb=on; cdt_ds=on; acct_untieRx=off; acc_ca_newreg=on; bfp_new=on; buynow=off; cp_new_dash=off; sab_displayads=on; dashboard_v1=on; disable-app-dynamics=on; dpp_cdc=off; dpp_drug_dir=off; dpp_sft=off; drginf=on; ecfl=on; easy_xfer=on; footer_new_V1=on; gbi_cvs_coupons=true; gbp_api_v2=on; mc_cloud_service=on; mc_hl7=on; mc_videovisit=on; newauthflow=on; newPDP=on; ngsw=off; ohexp=off; plpui=on; rx-pref-i90=on; pmexp=off; ps_i=off; rxdanshownba=off; rxdfixie=on; rxd_bnr=on; rxd_dot_bnr=on; rxdpromo=on; rxduan=on; rxm_demo_hide_LN=off; rxtiemm=on; sft_mfr_new=on; sftg=on; show_exception_status=on; slistview=on; sub_cp_fmf=off; switchExpAPI=on; tphrm=off; sd_ma=on; mca1=on; rbh1=off; s2c_transactionsphr=on; mfep1=off; imzfe=v1; imzn=on; rxp=on; aat3=on; hdnew=on; fspe=p1; kcpe=e; rxe=i1; mvpe=gr; mcpe=gr; mdpe=gr; ccse=p1; pe=p1; acct_pe=p1; ak_bmsc=CCBA05F4D0F489AE9CF749E6565EA66B~000000000000000000000000000000~YAAQBZUzuI2APOWQAQAA1bp1DBh8/XkckIN1GQc7kUgMjsUUozdGvKGQYJdskWw5jbX4RdTEl6rfSMKNCEAEWq/ipB8JJMhS66vk6OxGSZaeHHsJQ/4Wsnqw5W2QJWQdPwkTZJk7TYlJb5S6Um7SkInmtysKMgDktQEHb7yjSDwnF1wOaIGSRr1rdobXSiOHMNGqsdWd0UXoTPaF2kaxdsx1k6J/YIl2jag22++5FHFOXpbRB0yMSzIlLgK2piglp/xSoKnN0kNcWwalVxF6GktxDjQuwEnHbncsQzjZvGrvD3NpwkS0+2TgVmerTtI0FDUu3n5GarrAUNA8I6tUrEwidcHHIXKRwQ/OancnKgSA/wnk+QdRYbQWFlSzncRM6+9wnHeRog==; utag_main_v_id=018d729eaee5001f50b9dc4754b60507d001407500bd0; utag_main__sn=1; utag_main__ss=0%3Bexp-session; utag_main_ses_id=1707025018597%3Bexp-session; utag_main_vapi_domain=cvs.com; utag_main__pn=20%3Bexp-session; AMCVS_06660D1556E030D17F000101%40AdobeOrg=1; s_cc=true; _gcl_au=1.1.1989876051.1722490926; kampyleUserSession=1722490925780; kampyleUserSessionsCount=5; kampyleUserPercentile=65.91362588066244; _fbp=fb.1.1722490925836.28472638472144199; _uetsid=c92423d04fc811ef99020ba518baa091; _uetvid=6b15fd60c31f11ee83db7d3f874adaa1; visid_incap_2490223=pjAK3XDWQlOV8Jz9lBeDWTEgq2YAAAAAQUIPAAAAAACSNgWk5ZsPx9JMHeOOnlmy; incap_ses_1443_2490223=0NsaYsaSQCsF/vx19JAGFDEgq2YAAAAAqzuf7jdiAeKeA3lvCjf0RQ==; incap_ses_8215_2490223=vY7wOfoCBD6T5baRFYsBcjAgq2YAAAAA085d+zOiLAMJkPtjlG1D3w==; token_type=Bearer; access_token=eyJraWQiOiJRR0hnM0NTeUVhaGdrZ1RpTVZ3RHhrRy1yT0RPSlpGamI2NzBUOWxXSXBzIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJ4LWFwcC1uYW1lIjoidGVhbWFwcF9hcHBfZ3Vlc3RfcmV0YWlsX29yZGVyc18xNjY0OTM0OTIwIiwic3ViIjoidGVhbWFwcF9hcHBfZ3Vlc3RfcmV0YWlsX29yZGVyc18xNjY0OTM0OTIwIiwiaXNzIjoiaHR0cHM6XC9cL2FwaS5jdnNoZWFsdGguY29tXC9vYXV0aFwvdjEiLCJ4LWdyaWQiOiJycnQtMTAxNDMzNjUwMjMzMTY3MDQxOS1jLWdlYTEtNjIwMS0xNjMwMzEwMC0yIiwieC1jYWNoZS1wcmVzZW50IjpmYWxzZSwieC1mbG93LXR5cGUiOiJndWVzdCIsImF1ZCI6Imd1ZXN0LWZsb3ciLCJ4LWNsaWVudC1pZCI6IjZUaWlkb1JqcFFHM3VTaktVMzNsZ3E5N01BdVZCdHB6Iiwic2NvcGUiOiJvcGVuaWQiLCJ4LWNsaWVudC1maW5nZXJwcmludC1pZCI6ImV5SmpiR2xsYm5SRGFHRnlZV04wWlhKcGMzUnBZM01pT25zaVluSnZkM05sY2s1aGJXVWlPaUpGWkdkbElpd2lZbkp2ZDNObGNrMWhhbTl5Vm1WeWMybHZiaUk2SWpFeU55SXNJbUp5YjNkelpYSkdkV3hzVm1WeWMybHZiaUk2SWpFeU55NHdMakF1TUNJc0ltOXdaWEpoZEdsdVoxTjVjM1JsYlNJNklsZHBibVJ2ZDNNaUxDSnZjMVpsY25OcGIyNGlPaUl4TUNJc0ltTmhiblpoYzFCeWFXNTBJam9pTVdSak5ETTFaR1V4WVRCbE5HUTFPR0l5TUdFNU5ETmtNakZtTTJFellqVWlMQ0pqYUdGdWJtVnNJam9pVjBWQ0lpd2lkV0VpT2lKTmIzcHBiR3hoTHpVdU1DQW9WMmx1Wkc5M2N5Qk9WQ0F4TUM0d095QlhhVzQyTkRzZ2VEWTBLU0JCY0hCc1pWZGxZa3RwZEM4MU16Y3VNellnS0V0SVZFMU1MQ0JzYVd0bElFZGxZMnR2S1NCRGFISnZiV1V2TVRJM0xqQXVNQzR3SUZOaFptRnlhUzgxTXpjdU16WWdSV1JuTHpFeU55NHdMakF1TUNJc0ltTmhiblpoYzFCeWFXNTBYMjlzWkNJNklqazJOemM1T0RsaE16RXlNRGMzTm1OaE16TTBOR1psTW1ReFlXVmhaR0kzTldZeVkyUXhPR1kxTWpZME5HRTNZV0poTUdFek56a3lZamhtTXpVNU1XRWlMQ0ppYm1Od0lqb2lUV2xqY205emIyWjBJRVZrWjJVaUxDSmliWFpqY0NJNklqRXlOeUlzSW1KMlkzQWlPaUl4TWpjdU1DNHdMakFpTENKdmMyTndJam9pVjJsdVpHOTNjeUlzSW05emRtTndJam9pTVRBaWZYMD0iLCJ4LWxvYiI6Imd1ZXN0LWZsb3ciLCJleHAiOjE3MjI0OTE4MjksImlhdCI6MTcyMjQ5MDkyOSwieC11c2VyLWNvbnRleHQtdHlwZSI6Imd1ZXN0IiwianRpIjoiMTZkOGVhYmYtOTllYi00MzIzLWFmODMtYzBlODJlYjNiZjFhIn0.FJ6OVBifao1PyVW3m1JfhAIE4evn8I6VQMF5_7Sfj8z9CS0GJhpvjVtOGF7J_FFc7Le7DL1u1pnl1ljjV8T5vAKCXJ15zoBaBk7meVLH8Aq2OpgS8x0uBvGbwCtp8hrUT5K-TwZ3Cx6LSRnvjCQkmGPBLc73qcE2xFuqbA-dOH9cykEN98mmoHf03sqsogyp8C2CdSMlB5a-TAUn4mFZEunhRz0lHwX8-XUeET_4X2Tak88tJKueEEbGqRPjVac6DBUTukB_wNB2WC1ew53MSMZMMYFartqHzs61AePQ_lh-6gs2TuvEq1_XAdjf8knrH34bv55OoqPAk0gVrArxSw; fpcuid=1dc435de1a0e4d58b20a943d21f3a3b5; utag_main__st=1722492726356%3Bexp-session; utag_main__se=116%3Bexp-session; gpv_e5=homepage; kndctr_06660D1556E030D17F000101_AdobeOrg_cluster=va6; kndctr_06660D1556E030D17F000101_AdobeOrg_identity=CiY4NjMxNjMyNDA3MDk2NjgyMjg5MjE1NzQ0Mjk1NzA0MzQ5ODY5OFIQCJnp-pTXMRgBKgNWQTYwA_ABhoXX45Ay; incap_ses_6520_2490223=ec0pNPrDjlqtIrdJjrF7WjEgq2YAAAAA7kcAjYQZhe/pIHsYQjE8TQ==; incap_ses_132_2490223=DUtRT+1pxSoxeNbCZvXUATEgq2YAAAAAaSr0x1qbhq9r5vaDKZh2ww==; QuantumMetricSessionID=c96289509d500db95ae0d4190f73587d; QuantumMetricSessionLink=https://cvs.quantummetric.com/#/replay/cookie:c96289509d500db95ae0d4190f73587d?ts=1722447727-1722534127; AMCV_06660D1556E030D17F000101%40AdobeOrg=1176715910%7CMCIDTS%7C19937%7CMCMID%7C86316324070966822892157442957043498698%7CMCAAMLH-1723095725%7C7%7CMCAAMB-1723095725%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1722498125s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19944%7CvVersion%7C5.4.0; nlbi_2490223_2638546=IdhqRPK1bB/ZbYp5QrA1IgAAAACTQF99/zRpI5T2THQVRpfU; incap_ses_418_2490223=5FjhSFssuR7KBtP/5AjNBYQgq2YAAAAALpW2R+C7ExI33iSxZfpkWQ==; bab_atb=off2-p0; RT="z=1&dm=cvs.com&si=2ccad6a8-d677-4147-8b43-11429f517e4c&ss=lzaumf8g&sl=1&tt=vb&bcn=%2F%2F173bf110.akstat.io%2F&ld=1dn&hd=1u9k"; incap_ses_1441_2490223=QUahRgJ5diWDgPkr93X/E4Ygq2YAAAAA0kOmaKUmxgKqmhlBn7/CJw==; incap_ses_512_2490223=caDcXg6scU9YoZ2GZf0aB4Ygq2YAAAAAaDxp+2j8qrQ/6UWcFqnHQQ==; incap_ses_6524_2490223=y90LLyP4YkAANk7diOeJWoUgq2YAAAAAUd3GDr8QUqoBHM9d9psasQ==; reese84=3:X71qFK//OgNXz204GMb8ZA==:ZBwxqcDMMvv0nUY8BUT/J9itkzUoTcwkyv5rP8iko3h3hb4iqzwRRRYwnRAmwHp3Mu1AUqaDCB5/5hTw/SlKhcrOYM4bp/SYmaUWPBwOVydFTif8ckTuLNSecqDQJa7NWdQrbQfBn75nrU8oFCSb572U+zLz6qSG1eb3HFXQ2pbeENEYW53PxlKzbksUucU/sUDqARB9Py9g9pnoLvbeZTqAN8iKW6TwVgZZ+bLFaXHaDs/N2IFJXGxwq60RoPQLPhFzWZD+Vt79iAM6uBwU/2AcEEROe8/Z6Ao/b7H+fUozFul+cAws+89cXMX6gem5zYFIdHAyxRtRWk+rc78ArxevHG12hUqNjctdjSead2E0itWYVfRX6v8HYC3Vazt1z6bh2tbYnvIN07RMh8eJ+o7DzmoiOMGNFkRfeKDPRQE9uXDAMuNDi7poDgrWBG0Tf0W1DsiYZXRz+9OrI8YwwQ==:QnU/RAzcnbwUZHZ9CWGjp8Wsl89Z0ZckMdKYE6okewc=; __gads=ID=5788eb0f427b1398:T=1707025069:RT=1722491015:S=ALNI_MZNSTvp6WcOCs9X37OSVAHJTcTx0A; __gpi=UID=00000a0b602c4854:T=1707025069:RT=1722491015:S=ALNI_MZIQzlLcKsVtDTRyADtTNAnmSW-Zg; __eoi=ID=cdadd611cf7b3ac2:T=1707025069:RT=1722491015:S=AA-AfjbBGU1-VBN-6efXQcRhvJ8-; nlbi_2490223_2556230=xNwaIRyPPS7yzsoSQrA1IgAAAACbCdnxhNo7zvk/JxBNT2+9; _abck=AF42E39BB20AC35D17DE9653A87ECBD3~0~YAAQBZUzuImTPOWQAQAADxR3DAxBnqxDaXgXVXE1dY8SwS0prrkEWb4rTrYlVaBRBhqDYaGE+ZgXkrCE+xzA2CJrKewjZV9zx3R8jTcTXv8ZWnMIGVEVM/rgUSx5yGSukDisYxM71/WCudsdTCc6YO3lgbNY/U5NNUl5gsZvfmcm12T3yHouU3Z0NEAHdi1rnX+BCgaF9KTQMnrwtS2vQNM8oGc3qDzUcfK44/7MSP9lUdhECdXMXZu05gcwZZEczKxRObhQMOqsT4+R5lRiULMmnvDm3vgHx9DsMFiWACYjFFKrnZa0jgrwS6olVuXLyMSgQZpKvHAss6gzFD6gtBlpdOikrv+f21LEoKlzPDNq/EIyN8ae6eDNUs/lFr/0HC8ltlRS/XdLyf1G0PUrWQjRXZspnSvpiGJxHH7ZsGPEz3A1nxDFwizFMwvlRytca8Ujo6TlqisqV5RYVhyJ5bmO~-1~-1~-1; gpv_p10=www.cvs.com%2Fsearch; br_breadcrumb=undefined; category_id=undefined; _br_uid_2=uid%3D9231727608296%3Av%3D15.0%3Ats%3D1707025021088%3Ahc%3D8; kampyleSessionPageCounter=2; ADRUM=s~1722491021131&r~aHR0cHMlM0ElMkYlMkZ3d3cuY3ZzLmNvbSUyRnNlYXJjaCUzRmhhc2glM0QxNDYwMzQ5NTU5; akavpau_vp_www_cvs_com_crm=1722491444~id=6bdcb127029e9c6b1972ba302e2e525a; bm_sz=BF56D65FE763D723AF9D648C8B4280E1~YAAQBZUzuKWUPOWQAQAAGjZ3DBjiy1cFpH1lEIre2ZixJXyON3XVEOjUrW1/iHQOYc6FiYStjBlmGYK6IU29dSeQllYJpYGci3MCf2A74/tpP0JaZ8vO1p24zGtx0NnrYiuCWThnH+0adytj7AlrcjzAam6xtIZ1JOccWkna8Q8pMQbI9dXOr12FOCCSoQohlOqCvKY2K1yjCJnATHQC6de1v0YB9NJ9Cimv55NyXGvmJAcnRWanzimTh5ytrtrS0L+hAOauEW736SFI6/Lcj6P2+1XQ/GMSaedPCYcXdMTMUFehSYuYl40MhvPb9Jo/N+8F1Yfb+spBwlHgkhY+hZa439ohDHG1p70rnh/KNFi4ZULwsWmnT3r7RO9XHeFqghE3gvTtxwNGRQ5HTfeYE5hp8eh49YM1mR9FR33VQquaGg==~3420464~3290675; nlbi_2490223_2354313=CGzMd1ojwAHRdrrPQrA1IgAAAAAcS0vKPZq8OLB+vUGnsw1e; akavpau_www_cvs_com_general=1722491445~id=639fd3059ab74bdcb72377e958a9c470; nlbi_2490223_2147483392=J83bbQJ8ghemMjwCQrA1IgAAAADo849CSD7nUXB3dBp4qHS2; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Aug+01+2024+01%3A43%3A42+GMT-0400+(Eastern+Daylight+Time)&version=202402.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0011%3A1%2CC0012%3A1%2CC0013%3A1&AwaitingReconsent=false; cto_bundle=bEAa1F80ck52QlFsNTQxQ1FaMktNRHZCQXZyZ2Q0Z2dVbUZoWTc2WEl6YmY4RVJscjM5bzlrWmxjOERaUjd5ajhsUUdFbCUyRnhxd2dLQVpveWo1MzZsU1V3ZWk0NFBRVUxKZzF5ZTBocXdSUE95T2thRzU0c0lud3RuODd4UUFxT3ZJQks1bTVMa1g1Q2VqME5DY2Z5Y1FmaEludyUzRCUzRA; utag_main=v_id:01910c7700e8001f1917bc39d2b30507d002907500bd0$_sn:1$_se:19$_ss:0$_st:1722492822977$ses_id:1722491011305%3Bexp-session$_pn:2%3Bexp-session$vapi_domain:cvs.com; mp_cvs_mixpanel=%7B%22distinct_id%22%3A%20%2218d729eb2549d5-0d55b68528e3b4-4c657b58-1fa400-18d729eb2559ba%22%2C%22bc_persist_updated%22%3A%201707025019478%7D; bm_sv=3207835614E0220DE7CFA438D7F2B371~YAAQBZUzuEaVPOWQAQAAyD93DBhktvaZKm/h95SD4xhuDZjaKHH8J97PZf3yuXTPPXisctHbU2m1qp5960vwZ8RKJvviFois5yst5aydOyqUfOj+pPfGlXQrltgAExeoripIMc+6ZShPMWuYdlMXPF5Nl1l5Dymscfr5dR1yROvyhYMX/844cDuTBYKgWbyFi2VXeojf76rLBppUh6E3DNJnWV7qwuAyuzI7H21PfdXbFnZkxGiV/nk2TJsEXw==~1',
    'priority': 'u=1, i',
    'referer': 'https://www.cvs.com/search?searchTerm=all',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
}
start_time = time.time()
for page in range(0, 126):
    time.sleep(30)

    try:
        params = {

            'pageSize': '200',
            'skip': page * 200,

        }
        response = requests.get('https://www.cvs.com/shop-assets/proxy/bffv2/plp-search', params=params, cookies=cookies, headers=headers)
        result = response.json()  # Parse JSON response

        output_file_path = "cvs.json"

        with open(output_file_path, 'w') as f:
            json.dump(result, f, indent=4)

        for product in result['products']:

            try:

                
                for variant in product['variants']:
                    title = variant['gbi_title']
                    default_sku = variant['id']
                    price = variant['price']['value']
                    original_price = variant['originalPrice']['value']
                    product_url = variant['url']  
                    first_image_url = variant['images'][0]['uri']
                    variant_coupons = variant.get('cvsCoupons', [])
                    instock = variant['BRInventory']
                    
                    name = title
                    oldprice = original_price
                    plus_name = name.replace(" ", "+")
                    image = first_image_url
                    url = 'https://www.cvs.com' + variant['url']
                    discount2 = int(((float(original_price) - float(price)) / float(original_price)) * 100)
                    discount = str(discount2) + '%'
                    cpn_nbrs = [coupon['cpnNbr'] for coupon in variant_coupons]
                    cpn_nbrs = cpn_nbrs[:10]
                    offer = ', '.join(cpn_nbrs)

                    if cpn_nbrs == []:
                        cpn_nbrs = 'None'

                    if instock == 'in stock':

                        embed = {
                        "title": name,  "url": url, "thumbnail": { "url": image }, 
                        "author": 
                            {"name": "Bob's CVS Bot" },
                        "fields": [
                            {"name": "__Original Price:__", "value": '$' + oldprice, "inline": True },
                            {"name": "__New Price:__", "value": '$' + price, "inline": True },
                            {"name": "__Discount:__", "value": discount, "inline": True },
                            {"name": "__Coupons:__", "value": offer, "inline": True },
                            {"name": "__Useful Links:__", "value": f'[Amazon Search](https://www.amazon.com/s?k={plus_name})' + '\n' + instock, "inline": False }],
                            "color": 0xCC0000}
                    
                        payload = {
                            "content": "", "embeds": [embed], "username": "Bob's CVS Bot" }
                        if discount2 >= 80:
                            response = requests.post(wh_80, json=payload)
                        elif discount2 >= 60 and discount2 < 80:
                            response = requests.post(wh_60, json=payload)
                        elif discount2 >= 40 and discount2 < 60:
                            response = requests.post(wh_40, json=payload)

            except:
                continue 
        
    except:
        continue
                        
end_time = time.time()
elapsed_time = end_time - start_time
minutes = int(elapsed_time // 60)
seconds = elapsed_time % 60
formatted_time = f"{minutes} minutes {seconds:.1f} seconds"
status = "https://discord.com/api/webhooks/1268442790803669003/UHQMixUzhk3J_K-8Gj2MXroMra-jedGC3XBKEAP05XNKtNSQULtRGgAd_8o-sSMv_fia"
embed = {
"title": 'CVS Bot',
"author": 
    {"name": "Bob's CVS Bot" },
"fields": [
    {"name": "__Time To Finish:__", "value": str(formatted_time), "inline": True }],
    "color": 0xF88F33}
payload = {
    "content": "", "embeds": [embed], "username": "Bob's CVS Bot" }
response = requests.post(status, json=payload)
