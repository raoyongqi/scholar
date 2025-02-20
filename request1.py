import requests

session = requests.Session()
url = "https://scholar.google.com/scholar?hl=en&q=Geo-location+prediction"
url = "https://scholar.google.com/scholar?hl=en&q=Geo-location+prediction"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
cookies = {
    "NID": "521=KJbuIFP1BZqKG9W_Jm1SFW6tzaSsKvGJO2jedwaqo_vFDOc5G2cPpsvUU8Poenzk_xXTMcLFQJMRawSNneEZRYyVsUPtb3L724ZgV-Va4uJ5OSN0R4IPGYPLIwTqSs2Ed1nmqespbDU_kJjb25wDEUKt_4RHfexlG-sNBOu08TQBPb5oFKZv7-5uRl8Fn7X0UwWlvAYuM59mbJCumk3-IUi0ySGip71yCRoNhCf-x2vvAYA4_ftvJtfsRhMrSFTIhfYrQoe0F3VEc9cusSxBebpfFUD5V1o3B3s_yL16lWKelVGj5ycPLv12Psi6joI0I0XW0ScMrv3uomKKsdv7xqwC4Tf-H6PTsIqx8LaML-iM9iLe0Uwmwc-2ZNo-fOt1A7AmVPRC7xzdtGk95ekfDe6AlupWDHXS59PqtD5g_4vY1YHU7elYqYvx9aStQ_jGzfiplsUaHlhMVa2IZIaJ4c3l7HBXAdR6R1vsx2IZJEm0s1bYmh2Iv8VOKXlD-xBOaQ7sphPMMysQELj5seUQCE4cITFzaRQxWzA5Yo36Au_zxHLQSyopPRCx94xk2kpMRusxw72jOrhQTbxkw-RJV1I7-d96SnX8OxXH2mUswolnE4RnU8WhOpxz2jAJVVeTl8Jqhdj7AAFTx-kAnlW0lUmBEEfwY5_o",
    "GSP": "LM=1731372499:S=zmfR3R8AqxyqCWNp"
}

response = requests.get(url, headers=headers, cookies=cookies)


if "gs_captcha_ccl" in response.text:
    print("触发 CAPTCHA，请手动访问以下网址：")
    print(response.url)  # 可能是 Google Scholar 验证页面
    with open("captcha_page.html", "w", encoding="utf-8") as f:
        f.write(response.text)
else:
    print("请求成功，未触发 CAPTCHA。")
