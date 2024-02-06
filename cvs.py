import requests
import time
import json
wh_80 = 'https://discord.com/api/webhooks/1204252040210026536/3sR48gVzmoaOXC6vplJ6JAEXn8e5TqM0sGgUxexL-n_nVU82mMWPtWmEcFgeJBnENXbs'
wh_60 = 'https://discord.com/api/webhooks/1204252084942405685/GMQfAfuOJ2McvErJ1Gt6zOYXmAb3e77nuiIkMvkayR4QjyNp1jAP8fT8MA0XNX7OkSaT'
wh_40 = 'https://discord.com/api/webhooks/1204252131977330688/fT7xJBuiDmS2MuATX5b8CEDJJ9z_Ks4WxnwTe2jkkqx2x0K9EZfxKsRY19w0sHSyhU4R'
wh_0 = 'https://discord.com/api/webhooks/1204252179691606036/QyueTUhvDRc3h92MB9Y3AxsyIV_gLWne-I7N1zPTUF5BUQifIyW9kVV_qTMuEtCRI1Q8'
wh_all = 'https://discord.com/api/webhooks/1204252247391731732/aDUCu0ljFvRbCHkzfQTo6LER8Tpz8WZO4CSYrjV5K7qGCI9hgUWi6vksVMMo45AmsP1e'


def embed(name, oldprice, price, plus_name, image, url, discount, discount2, offer, insto):
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
    if discount2 > 1:
        response = requests.post(wh_all, json=payload)
    if discount2 >= 80:
        response = requests.post(wh_80, json=payload)
    elif discount2 >= 60 and discount2 < 80:
        response = requests.post(wh_60, json=payload)
    elif discount2 >= 40 and discount2 < 60:
        response = requests.post(wh_40, json=payload)
        time.sleep(1)
    elif discount2  > 1 and discount2 < 40:
       response = requests.post(wh_0, json=payload)
       time.sleep(1)



for i in range(0, 120):
    url = 'https://www.cvs.com/shop-assets/proxy/search?pnp=true&normalizer=%22productIndex%22&normalizerArgs=%7B%7D&query=%22%22&skip=' + str((int(i) * 200)) + '&pageSize=200&orFields=%5B%22variants.subVariant.availability%22%5D&refinements=%5B%5D'

    headers = {
        'authority': 'www.cvs.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': 'aat2=on; bm_sz=5CB8198EF775300190C76DBB5EA110E4~YAAQLCTDF/YJCVqNAQAANKuecha4+sahiYXWE9wedk4m/SVdyvPwoFP5gtH8Q4Y6lbIukP5Zw57NJPOlTvO8jdWKGjRXjPgu+tbOS1Qdug3+WmNMvHKh39Nmpm+WR/lvLlXn/NNtXDaDO9jCVbgdW+n++H3q+Ad4kRUgkQb9qLGWXEjs9MtYA3CWBbjnbqDmf+KJd6eOjqEgX2W7wB+hMDSpkm90xZjmxYK/zefjchYJEe6IzxiJOdPXk4tTnNr8ixUzNBTKvQNXXIU8BUB5hp7zh0wERpRONdXfXP/lVfr9csXH7oJxLob2fctNwoC3bY368jKqOO7jet1l~3490867~3749424; ak_bmsc=A2B352DF9D53BEAEDC06A6BD9FB07DE6~000000000000000000000000000000~YAAQLCTDF/UJCVqNAQAANKuechbtpm7rq6VcshZFusDzUY2wQ7N62OmUeviTkLhc6KP/Ax+w9NjgLE7ZPAVALpmcwc52lsQw8fygybw1tGVZYe7/60XWji24dAaEODPKY0M0VWsxVM2ZZsuyf3WQZxrc0jP/jIO+MDPTvayP+sJ9mdf0c++5S+k0M4ViuPI3WINqEcbom+BMhNNfDucAlqrIkCkRqZdCbsKDuYVBmE2stC/DdJFG3WhaAUJMp6DdqT4U3vw5rBKZvTl4iQac+AtlbFiUhAPMroJh4DO9K9m+kCu5W0vvlamOGNJqZMt6Xt5rUSeZSibbYTbj9bE30OXPAwiqEJlIL9AcSliEFvRdE+zuh+9r/ixXTSij4/kLKQL9TtPqNwg=; acct_pe=p1; pe=p1; ccse=p1; mdpe=gr; mcpe=bl; mvpe=bl; rxe=i1; kcpe=e; aat1=off-p0; fspe=p1; hdnew=on; ga=g1; aat3=on; gb=g1; rxp=on; gc=g2; gr=g1; hmnew=on; imzn=on; imzfe=v1; mfep1=off; tphrm=off; s2c_transactionsphr=on; mca1=on; sub_cp_fmf=off; slistview=on; show_exception_status=on; sftg=on; sft_mfr_new=on; rxtiemm=on; rxm_demo_hide_LN=off; rxduan=on; rxdpromo=on; rxd_dot_bnr=on; rxd_bnr=on; rxdfixie=on; rxdanshownba=off; ps_i=off; pmexp=off; pfexp=off; plpui=on; ohexp=off; newauthflow=on; mc_videovisit=on; mc_hl7=on; mc_cloud_service=on; gbp_api_v2=on; gbi_cvs_coupons=true; footer_new_V1=on; easy_xfer=on; ecfl=on; drginf=on; dpp_sft=off; dpp_drug_dir=off; dpp_cdc=off; disable-app-dynamics=on; dashboard_v1=on; sab_displayads=on; cp_new_dash=off; buynow=off; acct_cgsb=on; adh_ps_refill=on; adh_ps_pickup=on; acct_sso_mig=on; acexp=off; aat4=off-p2; AMCVS_06660D1556E030D17F000101%40AdobeOrg=1; gpv_p10=www.cvs.com%2F; s_cc=true; _gcl_au=1.1.987798673.1707025020; AMCV_06660D1556E030D17F000101%40AdobeOrg=1176715910%7CMCIDTS%7C19758%7CMCMID%7C86316324070966822892157442957043498698%7CMCAAMLH-1707629819%7C7%7CMCAAMB-1707629819%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1707032220s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19765%7CvVersion%7C5.4.0; visid_incap_2490223=P+EOxAl2QkiNxBBXNBKnC3siv2UAAAAAQUIPAAAAAAD/Ip3biJmm7W3v9mJ5Yn/a; nlbi_2490223_2354313=fxh0e7C8tkuTXgX/QrA1IgAAAAC3/rt8rZRJlkQLAtAVThMj; incap_ses_1552_2490223=uZAANQ/KsE2mZeRMZdCJFXsiv2UAAAAAyEg91qW7/pC9qyZH1SBB7Q==; _uetsid=6b155420c31f11ee9c20cf3e3e8ef09f; _uetvid=6b15fd60c31f11ee83db7d3f874adaa1; kndctr_06660D1556E030D17F000101_AdobeOrg_cluster=va6; kndctr_06660D1556E030D17F000101_AdobeOrg_identity=CiY4NjMxNjMyNDA3MDk2NjgyMjg5MjE1NzQ0Mjk1NzA0MzQ5ODY5OFIQCJnp-pTXMRgBKgNWQTYwA_ABmen6lNcx; _fbp=fb.1.1707025020468.1660156645; incap_ses_486_2490223=szWfGFBwYTzZtGsVyp++Bnwiv2UAAAAAK9GvXWsWVGV0saGGOCynaA==; token_type=Bearer; access_token=eyJraWQiOiJJRi1jMkpKa2d4bEs4Zk82ZVRrdzdNWmxwQlJFRlh5bDRRX3RLMk4yT0l3IiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJ4LWFwcC1uYW1lIjoidGVhbWFwcF9hcHBfZ3Vlc3RfcmV0YWlsX29yZGVyc18xNjY0OTM0OTIwIiwic3ViIjoidGVhbWFwcF9hcHBfZ3Vlc3RfcmV0YWlsX29yZGVyc18xNjY0OTM0OTIwIiwiaXNzIjoiaHR0cHM6XC9cL2FwaS5jdnNoZWFsdGguY29tXC9vYXV0aFwvdjEiLCJ4LWdyaWQiOiJycnQtNzAzOTQ0OTQzODQ4MjgyNDM1Ny1jLWdlYTEtMjA5ODMtNTc3MDQyMC0zIiwieC1jYWNoZS1wcmVzZW50IjpmYWxzZSwieC1mbG93LXR5cGUiOiJndWVzdCIsImF1ZCI6Imd1ZXN0LWZsb3ciLCJzY29wZSI6InVybjpjdnNoZWFsdGg6Y2xpZW50LWV4cGVyaWVuY2U6bG9hZDp3cml0ZSB1cm46Y3ZzaGVhbHRoOmRldGFpbHM6d3JpdGUgdXJuOmN2c2hlYWx0aDpkaWdpdGFsY291bnNlbHF1aXpkZXRhaWxzOnN0YXR1czpyZWFkIHVybjpjdnNoZWFsdGg6ZGlnaXRhbGNvdW5zZWx2aWRlb2RldGFpbHM6c3RhdHVzOnJlYWQgdXJuOmN2c2hlYWx0aDpkaWdpdGFsY291bnNlbHhpZGRldGFpbHM6c3RhdHVzOnJlYWQgdXJuOmN2c2hlYWx0aDppdGVtczpzdWJzdGl0dXRpb25zOnJlYWQgdXJuOmN2c2hlYWx0aDpsaXN0OndyaXRlIHVybjpjdnNoZWFsdGg6bWVtYmVyLWV2ZW50czpzdWJtaXQ6Y3JlYXRlIHVybjpjdnNoZWFsdGg6bWZlOnNkZGVsaWdpYmlsaXR5OnN0b3Jlczp3cml0ZSB1cm46Y3ZzaGVhbHRoOnBoYXJtYWN5OmRydWdzYXZpbmdzOmNlbGVicmF0ZS1zYXZpbmdzOnJlYWQgdXJuOmN2c2hlYWx0aDpwaGFybWFjeTpkcnVnc2F2aW5nczpwcm9jZXNzLWRpc3Bvc2l0aW9uOndyaXRlIHVybjpjdnNoZWFsdGg6cGhhcm1hY3k6ZHJ1Z3NhdmluZ3M6c2F2aW5nczpyZWFkIHVybjpjdnNoZWFsdGg6cmV0YWlsOmxveWFsdHk6ZGFzaGJvYXJkOnJlYWQgdXJuOmN2c2hlYWx0aDpyZXRhaWw6bG95YWx0eTptZW1iZXJzaGlwOm1hbmFnZW1lbnQ6cmVhZCB1cm46Y3ZzaGVhbHRoOnJldGFpbDpsb3lhbHR5OnJlYWQgdXJuOmN2c2hlYWx0aDpyZXRhaWw6bG95YWx0eTp3cml0ZSB1cm46Y3ZzaGVhbHRoOnNkZDphZGRyZXNzOnYxOnJlYWQgdXJuOmN2c2hlYWx0aDpzZGQ6YWRkcmVzczp2MTp3cml0ZSIsIngtY2xpZW50LWZpbmdlcnByaW50LWlkIjoiZXlKamJHbGxiblJEYUdGeVlXTjBaWEpwYzNScFkzTWlPbnNpWW5KdmQzTmxjazVoYldVaU9pSk5hV055YjNOdlpuUWdSV1JuWlNJc0ltSnliM2R6WlhKTllXcHZjbFpsY25OcGIyNGlPaUl4TWpFaUxDSmljbTkzYzJWeVJuVnNiRlpsY25OcGIyNGlPaUl4TWpFdU1DNHdMakFpTENKdmNHVnlZWFJwYm1kVGVYTjBaVzBpT2lKWGFXNWtiM2R6SWl3aWIzTldaWEp6YVc5dUlqb2lNVEFpTENKMVlTSTZJazF2ZW1sc2JHRXZOUzR3SUNoWGFXNWtiM2R6SUU1VUlERXdMakE3SUZkcGJqWTBPeUI0TmpRcElFRndjR3hsVjJWaVMybDBMelV6Tnk0ek5pQW9TMGhVVFV3c0lHeHBhMlVnUjJWamEyOHBJRU5vY205dFpTOHhNakV1TUM0d0xqQWdVMkZtWVhKcEx6VXpOeTR6TmlCRlpHY3ZNVEl4TGpBdU1DNHdJaXdpWTJGdWRtRnpVSEpwYm5RaU9pSXhaR00wTXpWa1pURmhNR1UwWkRVNFlqSXdZVGswTTJReU1XWXpZVE5pTlNKOWZRPT0iLCJ4LWxvYiI6Imd1ZXN0LWZsb3ciLCJleHAiOjE3MDcwMjU5MjAsImlhdCI6MTcwNzAyNTAyMCwieC11c2VyLWNvbnRleHQtdHlwZSI6Imd1ZXN0IiwianRpIjoiMzJhZmVkNGEtZGE3Ni00MzAwLWJlZGItOGU0YjQwZDZmMmRjIn0.BT1D3SrmWQcDe5TqshjUjzwR-cxsSdw-TisJwGozCP-KOwQ9fDiCTLjEORwd5hVVrtJk5zDttiqVHCk20fYnWCMhh6W1p6gKxmuPjO-JGMWmEhk3DwCo4SAsBo3BMHbhmZfJj55qHGg5Ju_0WWEJAP_rmosbV36MStXjEMCFpv5cOW4GHhSjsO5ouhLEGjo6QiWHrVVkf7MQ16DLnToxBWCI6to0kGD88KIccZbwTJy-Bg-VOmvoYkKIRSNz-TxRtSVPDBlaJ6OrLyzx_Q337qNP0m8ryQKMZQGk4rCbboZNK24YZWKIUH7SyNzk4ZW8naeY2-KCWxMjyHC71cr9Zg; fpcuid=1dc435de1a0e4d58b20a943d21f3a3b5; incap_ses_1543_2490223=wQVheGZ0ZkG0H6F+XNZpFXwiv2UAAAAAY0VmLU+HIf3JdpWciENAhQ==; gpv_e5=homepage; mt.cem=; _br_uid_2=uid%3D9231727608296%3Av%3D15.0%3Ats%3D1707025021088%3Ahc%3D1; mdLogger=false; kampyle_userid=d5f5-cee3-19ad-c07e-93dc-4048-d72f-784d; kampyleUserSession=1707025021594; kampyleUserSessionsCount=1; kampyleSessionPageCounter=1; kampyleUserPercentile=39.131668195208704; QuantumMetricSessionID=c9027822bd6c6200577ee39ea55f380e; QuantumMetricUserID=649c646d3e8229dbfc851ded764fa909; QuantumMetricSessionLink=https://cvs.quantummetric.com/#/users/search?autoreplay=true&qmsessioncookie=c9027822bd6c6200577ee39ea55f380e&ts=1706981823-1707068223; ADRUM=s=1707025065901&r=https%3A%2F%2Fwww.cvs.com%2F; nlbi_2490223_2638546=YefyHwus+TITzRYwQrA1IgAAAAAF7z9D6IhnsO6/ip4nUR9W; incap_ses_1813_2490223=aVzXM4EisUFPNjRR7hEpGaoiv2UAAAAA9WLBslVf3dI7byk7d5jHQQ==; bab_atb=off1; RT="z=1&dm=cvs.com&si=21c26107-04ff-4022-9ed0-d313a1bc3ede&ss=ls72md7r&sl=1&tt=330&bcn=%2F%2F173bf10e.akstat.io%2F&ld=33z&hd=128v"; incap_ses_1700_2490223=edV6LGkgG2J3KDBymp2XF6oiv2UAAAAAfJebJyb2ZfxNTq4SweP+sw==; incap_ses_1533_2490223=CDfFXQCw+VBY3Iq5A1BGFasiv2UAAAAAWdmWPURI4FUByyt6ptkV+g==; nlbi_2490223_2556230=v7gEVnR443afY15zQrA1IgAAAACeVRMzcd14sUJcRqsDq8Fl; SameSite=None; incap_ses_1245_2490223=9KJMFkNF6VA3o2oFHSJHEa0iv2UAAAAAxnxepRwVR72LgUrBCNEfUw==; __gads=ID=5788eb0f427b1398:T=1707025069:RT=1707025069:S=ALNI_MZNSTvp6WcOCs9X37OSVAHJTcTx0A; __gpi=UID=00000a0b602c4854:T=1707025069:RT=1707025069:S=ALNI_MZIQzlLcKsVtDTRyADtTNAnmSW-Zg; __eoi=ID=cdadd611cf7b3ac2:T=1707025069:RT=1707025069:S=AA-AfjbBGU1-VBN-6efXQcRhvJ8-; akavpau_vp_www_cvs_com_crm=1707025490~id=4e7940c86d2731c1e27332e250c68319; mp_cvs_mixpanel=%7B%22distinct_id%22%3A%20%2218d729eb2549d5-0d55b68528e3b4-4c657b58-1fa400-18d729eb2559ba%22%2C%22bc_persist_updated%22%3A%201707025019478%7D; ADRUM_BTa="R:38|g:36c24254-9cfd-4b82-a7e7-418a0df69e3e|n:cvsdigitalapm-prd_9f526f5a-9f54-4cd6-9a06-a600191db4a6"; bm_sv=601E12CF9D490A7E9334B41E80966F87~YAAQLCTDF1ESCVqNAQAAIIafchbrFFrXDLbdkexiOmWNn5DkRTBmbkHV66PKLPn6lDE9imlkfPYK0TNAjmj1wb84I52swfUfQoBFYvVAwHwG5U9jpsQOF1JE+SCNrRsIgvq8yqG3NVNrM50B5ZihhQQvaRD6HwlAFQkKes9hCbWu3a/NjoVvGPjrRc8VtMYOGy0RznZ49tLkgigun/ECI92iPvgJiVjnGNSZCtN5aSRGvcYXFP+rid+S7CcySA==~1; cto_bundle=3q0e9V80ck52QlFsNTQxQ1FaMktNRHZCQXZ1MjNYeGVQTHRncW54QWlnZ205YnJqbW94clVNRzVjTTR2QmZKaXFoZWNOeVo2aVJXS01zUHp3SDNWZWpMV2pQMHNjamFEWmk2M25uMXh6VDJDNjdNVGViV3BnZEN1NjFQVFVoNXMwdzFIMVBPSkJBT1Jta1FpaVE5V0RwbnNCb0ElM0QlM0Q; akavpau_www_cvs_com_general=1707025495~id=ba274abf3f6bc55dd5550644837e6579; _abck=AF42E39BB20AC35D17DE9653A87ECBD3~0~YAAQLCTDF3YSCVqNAQAA54ufcgum2D3K0czcAmdfwrzhH3pVI+wD517M0nMg1WYS07IJSmCMAp6zLfVwDxU7wWa3Xo3Fzt3sbSSVqfXk4HUu8xzr4pxCKYq3CAA21Wc5tb94xKWjXBM4OeXn/2A1cQ+7QdK6lcDdfChPtT4bp6n6grI2kjIoVl00TeCDRA6s8hVWj1fErRUjoqM9OgrmM3/dNx514uJh65L/IVCCQRpN0NLAinwcnFS6R6pLxtbjSvKYqAs1LoV9GvCWY++3pBKawM9WKzI4e0fO7+L5ip9qlIlWkKf2uSDGkVAFlrjSLsmUXg+7t+LKUMcKfd1TI+Eg7gUYEeX1uqyZ5UvO8GcY7PBZCKk/8LqAHwxlP0oOIWW5DMRolvreUonn0F0WTVVJaKW2kw==~-1~-1~-1; nlbi_2490223_2147483392=fD7TH+YSs2nphRDzQrA1IgAAAAAoowCVI9O6TvTIVzyPqqAS; incap_ses_441_2490223=VMpNA5i4tCGv9og3VsAeBrIiv2UAAAAAQ6QIr1TAKtclpBuBz/7NDQ==; reese84=3:MVpKGWBdc6VgWGaqM4Ez6w==:JuBVDhKytr8EIDEHvpkk3XrZf4inVBw80fnbAIphOHW3TC3NfxXzPxcKmBgTWvCpxTKOJCJEFpIudaoFVuoCHhqR2pG3m4SZF85DkPg4ptEjqQ/wpZavsYMaiaLPsIwkxPRnH6Qmd8N8i0uVZc1DtlAog3vh6/4jswLSKwBOkJEYlccm6LO2c5C/tiBZwR7v3WP8c12tDns9Wzx/7u/7xyWDjflVu4CJCLqaMRzzQpkg2/HjvQKtpWIu0vbaMxie/pDPwRvi09ICHKDGfjiAdHldB2i+js9PSbKel+8v6zQSkoUtMeyrYPp/Pqgyolmd1pg1bjbU+V7QbZj5mlRRdf1tLTG6Ubmd4xxnJtka3wbxlhlyPymre0ufU+g0zNot+t+7HjvylAG4MVZJwkSJC3Ku4cgTseBZyiiT4j5feyYjWUUQLRXuNsI8uliXIRtJK6lNn/CIccN48U/AKSB4ig==:4DMZLzwnPn5bbwpRlx6r1ruiSPj9ECwG1YmDAd0svTU=; utag_main=v_id:018d729eaee5001f50b9dc4754b60507d001407500bd0$_sn:1$_ss:0$_pn:3%3Bexp-session$_st:1707026890898$ses_id:1707025018597%3Bexp-session$vapi_domain:cvs.com$_se:35',
        'referer': 'https://www.cvs.com/search?page=2',
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    }

    response = requests.get(url, headers=headers)


    data = json.loads(response.text)
    # Extract product information
    for product in data['products']:

        
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
                    

            embed(name, oldprice, price, plus_name, image, url, discount, discount2, offer, instock)

        


