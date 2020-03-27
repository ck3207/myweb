import os

import requests
from django.conf import settings

class Download:
    """Deload package from https://scm.hundsun.com/"""
    URL = "https://scm.hundsun.com/pkgManage/pkg/downloadFile.htm?"
    URL_PREFIX = "[pkg]/pkg/杭州云纪"
    def __init__(self, file_path, headers):
        self.file_path = file_path
        self.headers = headers
        self.headers["Connection"] = "keep-alive"
        self.headers["Referer"] = "https://scm.hundsun.com/pkgManage//pkg/doPkgList.htm"
        # self.headers["Pragma"] = "no-cache"
        # self.headers["Sec-Fetch-Dest"] = "iframe"
        # self.headers["Sec-Fetch-Mode"] = "navigate"
        # self.headers["Sec-Fetch-Site"] = "same-origin"
        # self.headers["Sec-Fetch-User"] = "?1"
        # self.headers["Upgrade-Insecure-Requests"] = "1"
        # self.headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        # self.headers["Accept-Encoding"] = "gzip, deflate, br"
        # self.headers["Host"] = "scm.hundsun.com"
        # self.headers["Cache-Control"] = "no-cache"
        # self.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        self.basename = os.path.basename(file_path)
        
    def to_unicode(self):
        """Transfer file_path to unicode.
        Attention: when transfer Chinese characters  to unicode, you should add %25 before each Chinese character.
        """
        url = ""
        for character in Download.URL_PREFIX+self.file_path:
            if self.is_chinese_character(character):
                url += str(character.encode('unicode_escape'))
            else:
                url += character
        return url.replace("b'\\\\", "%25").replace("'", "")
        
    def is_chinese_character(self, character):
        """Whether the character is Chinese character or not."""
        if character >= u'\u4e00' and character<=u'\u9fa5':
            return True
        else:
            return False

    def get_download_url(self):
        return Download.URL+self.to_unicode()+"&serverType=test"
        
    def download(self, save_path):
        # url = self.get_download_url()
        # print("Download URL:\n", url)
        print(self.headers)
        data = {"downloadPath": self.to_unicode(),
                "serverType": "test"}
        print(data)
        try:
            r = requests.get(url=Download.URL, headers=self.headers, verify=False, params=data, stream=True)
            with open(file=os.path.join(save_path, self.basename), mode="wb") as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            f.close()
            print("Download Successfully in the directory:{0}".format(os.path.dirname(os.path.join(save_path, self.basename))))
        except Exception as e:
            print("Download File Failed From URL:{0}".format(url))
            print(str(e))
        return
        
if __name__ == "__main__":
    download = Download(file_path=r'/VIPSTU/test/FSP/h5-fans-cnpsec/SVN29984-h5-fans-cnpsec-20200326-09.47.29-offline.zip', 
    headers={"Cookie": "JSESSIONID=6DD60DE7EB0DB518E789DB34F46556E2"})
    download.download("../../static/download")