import hashlib
import os
import shutil
from pathlib import Path

"""
두 파일 디렉터리를 동기화하는 코드(sync_two_files 함수)
- 두 파일 디렉터리를 원본(source)과 사본(destination) 이라고 부름
- 다음의 세 가지 조건을 만족해야 함
    1) 원본에 파일이 있지만 사본에 없으면 파일을 원본에서 사본으로 복사한다.
    2) 원본에 파일이 있지만 사본에 있는 (내용이 같은) 파일과 이름이 다르면
        사본의 파일 이름을 원본 파일 이름과 같게 변경한다.
    3) 사본에 있지만 원본에는 없다면 사본의 파일을 삭제한다.


1. 주어진 함수를 활용하여 sync_two_files 함수를 채우고 설명해주세요.
2. 각 함수에 type hint 를 넣어주세요.
3. 함수 determine_actions 의 test 코드를 작성해주세요.
참고 : https://docs.python.org/3/library/shutil.html
"""

def sync_two_files(src, dest) :
    # TODO
    ...


BLOCKSIZE = 65536


def hash_file(path):
    hasher = hashlib.sha1()
    with path.open("rb") as file:
        buf = file.read(BLOCKSIZE)
        while buf:
            hasher.update(buf)
            buf = file.read(BLOCKSIZE)
    return hasher.hexdigest()


def make_hashes_from_paths(root):
    hashes = {}
    for folder, _, files in os.walk(root):
        for fn in files:
            hashes[hash_file(Path(folder) / fn)] = fn
    return hashes


def determine_actions(source_hashes, dest_hashes, source_folder, dest_folder):
    for sha, filename in source_hashes.items():
        if sha not in dest_hashes:
            sourcepath = Path(source_folder) / filename
            destpath = Path(dest_folder) / filename
            yield "COPY", sourcepath, destpath

        elif dest_hashes[sha] != filename:
            olddestpath = Path(dest_folder) / dest_hashes[sha]
            newdestpath = Path(dest_folder) / filename
            yield "MOVE", olddestpath, newdestpath

    for sha, filename in dest_hashes.items():
        if sha not in source_hashes:
            yield "DELETE", Path(dest_folder) / Path(filename), None