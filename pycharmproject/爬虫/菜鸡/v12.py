from urllib import request
if __name__=="__main__":
    url="https://qzone.qq.com/"

    headers={
        "Cookie":"_qpsvr_localtk=0.04673153193630464; ptisp=cm; pgv_si=s2186895360; uin=; skey=; pgv_info=ssid=s7313572927; rv2=80E3076ACFB7506C59C69D74514DBDA1BC8BF57D9AB5ABC0D0; property20=9C0AD851B8F148F1D5902FC68EBD11AA328B18884A62EBAE117638823CF761ED95F97358365CAE6A; LW_uid=M1x5R4k0m7W1F9D7a941H358i1; pgv_pvid_new=o1974410167_ccb3734163; tvfe_boss_uuid=6194a581860db2dd; LW_pid=e8cd3319acb4fc31eda1be9697562811; pgv_pvid=7440610048; o_cookie=1909874106; ptcz=267bcc919c7e9b0b6ce5610c0a545108df84c2551d2c9f02d20a76e69cb62c1e; ied_qq=o1974410167; pgv_pvi=8349175808; uin_cookie=o1974410167; pac_uid=1_1974410167; _qz_referrer=localhost:63342; ue_uk=fc9f22a5f8c46c6b0f65b1e27a770c28; LW_TS=1551362375; ue_skey=d3c0bd5ea1796b666d84a3dcb11c11f4; LW_sid=h1c5p598v2d6n9g5v1M2Q1r626; _ga=GA1.2.1416718613.1554264956; RK=A+rtvkLAPl; LW_PsKey=6ee469095b137f0f16d0a3972027519c; ptui_loginuin=1909874106; eas_sid=o1w50400B741E9g798C5G3K7z2; ue_ts=1553774510; ue_uid=2f589692f9693781559f4d41cf886e24; pt_login_sig=MsMHOYE*NxITMZ8vvnTxar2sthGfVDcARmWj4Cygw6bKOdnzFXYiq5qJEGzM4nmt; pt_clientip=69d4759ec03ea5c3; pt_serverip=42e50af498103ef8; pt_local_token=168530038; uikey=dd240fae84f31a0901ede6175823e0837443184f3ce28802398892810a9633ba; confirmuin=0; ptdrvs=YgoM4ifsw27Rk0rbj0UZh-1LEDZPZFHzKge*RpL291PLWLnKqbdgWg__; ptvfsession=6488b1efdecf76d9fdda19eb053e55db205cf1d27373251ee6d6b270afad9c8051893ae55b0e0fc5d695a184658b1e314a9f21a794c3ea1a; qrsig=kXbkbHJlEfFURtSj6CJqMtRxCDI0DLE5c41GKU3xPGseg*FRSe-vjg0MQ4uRjEqG; dev_mid_sig=7621c51c59449a88ce1792d701e52178471d2771599fcf775a46e9ab2550148a5cea61da254504aa; clientuin=1974410167; ETK=; ptnick_1974410167=2e; pt2gguin=o1974410167; pt_recent_uins=502c511ba583adcbfe65d58f29786e44f467514a1c885aea4367be2c6f43ec585f39df4578a651324ae88b9070dc43799697074f8e108cdd; pt_guid_sig=53e98abc5572879ae5b23addf8a9ebd3698d9ec49438220649d9a8c029f6fef6"

    }

    rsp=request.Request(url,headers=headers)
    rsq=request.urlopen(rsp)
    html=rsq.read().decode()

    with open("rsp.html","w") as f:
        f.write(html)