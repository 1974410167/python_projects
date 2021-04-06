
import hashlib
a='e4393642bfa6f03e683a05ff95c9593ad51b63c1'
list=[hashlib.md5(),hashlib.sha1(),hashlib.sha3_224(),hashlib.sha3_256(),hashlib.sha3_384(),hashlib.sha3_512(),hashlib.sha224(),hashlib.sha256(),hashlib.sha384(),hashlib.sha512()]
for i in list:
    md=i
    md.update("HYuan.5637".encode("utf-8"))
    if a in md.hexdigest():
        print(f"a in {md}")
    print(f"{md}-->{len(md.hexdigest())}--{md.hexdigest()}")
